# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from odoo import models, fields, api


class sms_mak_hta(models.Model):
    _inherit = 'mailing.mailing'
    
    
#     mailing_type = fields.Selection(selection_add=[
#         ('sms_bulkgate', 'SMS')
#     ], ondelete={'sms_bulkgate': 'set default'})

    def get_info_to_send_sms(self):
        
        liste_contact = []
        contacts = self.contact_list_ids.contact_ids
        for cont in contacts:
            liste_contact.append(cont.mobile)
        
        message = self.body_plaintext
        
        return liste_contact,message
    
    def listToString(self,liste):
 
        # initialize an empty string
        contacts = ""

        for lt in liste:
            contacts += str(lt)+';'

        # return string
        return contacts
    
    def send_sms_(self,number,text):
        api_url = 'https://portal.bulkgate.com/api/1.0/simple/promotional'
        
        data = {
            "application_id": "28307",
            "application_token": "cHHmmA3y7M88XFoj40qYeWEgMlLQjxTi49DgI4MRsiMBSqahmV",
            "number": number,
            "text": text,
            "sender_id": "gText",
            "sender_id_value": "AFRIMEDIS",
            "country": "ci",

        }
        return requests.post(api_url, json=data)
    
    
    def send_sms_schedule(self,number,text,date_schedule):
        api_url = 'https://portal.bulkgate.com/api/1.0/simple/promotional'
        
        data = {
            "application_id": "28307",
            "application_token": "cHHmmA3y7M88XFoj40qYeWEgMlLQjxTi49DgI4MRsiMBSqahmV",
            "number": number,
            "text": text,
            "sender_id": "gText",
            "sender_id_value": "AFRIMEDIS",
            "country": "ci",
            "schedule":date_schedule,

        }
        return requests.post(api_url, json=data)
    
    

    
    def action_send_sms_now(self):
        for sms in self:
            
            get_info = sms.get_info_to_send_sms()
            contact = sms.listToString(get_info[0])
            messages = get_info[1]
            send_sms = sms.send_sms_(contact,messages)
            
            sms.write({
                'state': 'done',
                'sent_date': fields.Datetime.now(),
                # send the KPI mail only if it's the first sending
            })
        
        return True
        
    
    def action_launch_sms(self):
        self.write({'schedule_type': 'now'})
        return self.action_put_in_queue_send_sms()
    
    def action_schedule_send_sms(self):
        self.ensure_one()
        if self.schedule_date:
            return self.action_put_in_queue_send_sms()
        else:
            action = self.env["ir.actions.actions"]._for_xml_id("sms_mak_hta.send_sms_schedule_date_action")
            action['context'] = dict(self.env.context, default_mass_mailing_id=self.id)
            return action
        
    def action_put_in_queue_send_sms(self):
        self.write({'state': 'in_queue'})
        cron = self.env.ref('sms_mak_hta.sms_mass_mailing_queue')
        cron._trigger(
            schedule_date or fields.Datetime.now()
            for schedule_date in self.mapped('schedule_date')
        )
        
        
    @api.model
    def _process_sms_end_queue(self):
        mass_mailings = self.search([('state', 'in', ('in_queue', 'sending')), '|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            user = mass_mailing.write_uid or self.env.user
            mass_mailing = mass_mailing.with_context(**user.with_user(user).context_get())
            if len(mass_mailing._get_remaining_recipients()) > 0:
                mass_mailing.state = 'sending'
                mass_mailing.action_send_sms_now()
            else:
                mass_mailing.write({
                    'state': 'done',
                    'sent_date': fields.Datetime.now(),
                    # send the KPI mail only if it's the first sending
                    
                })
