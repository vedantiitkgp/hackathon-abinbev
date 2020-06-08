import requests
import json

class token_generator:
    def __init__(self):
        self.client_id = '1000.8CLIDJMH9YE6BK0V8O9DKKEB5MA0GV'
        self.client_secret = 'ff89f2642fb39bfebb36258588ebb8db7b723aa5bb'
        self.grant_type = 'refresh_token'

        self.timelog_token = 'b2bc80833497cb560a9b35c3843acc06'
        
        self.expense_refresh_token = '1000.48595a9e216f9a876b0e5f94f02da1d6.55b7ed50588f1077e3cdbe687e991e44'
        self.expense_organization_id = '60004846601'
        
        self.desk_refresh_token = '1000.f86e9e1627f427b74549d83e7ff62584.44824e45ee735ae54af18307720a24cf'
        self.desk_organization_id = '60004846602'
        self.desk_scope = 'Desk.settings.READ,Desk.basic.READ,Desk.tickets.ALL,Desk.contacts.READ'

    def expense(self):
        url = 'https://accounts.zoho.in/oauth/v2/token?refresh_token='+self.expense_refresh_token+'&client_id='+self.client_id+'&client_secret='+self.client_secret+'&grant_type='+self.grant_type    
        response = requests.post(url)
        response_json = json.loads(response.text)
        oauth_token = response_json['access_token']
        return {'access_token':oauth_token,'organization_id':self.expense_organization_id}
    
    def ticket(self):
        url = 'https://accounts.zoho.in/oauth/v2/token?refresh_token='+self.desk_refresh_token+'&grant_type='+self.grant_type+'&client_id='+self.client_id+'&client_secret='+self.client_secret+'&scope='+self.desk_scope
        response = requests.post(url)
        response_json = json.loads(response.text)
        oauth_token = response_json['access_token']
        return {'access_token':oauth_token,'organization_id':self.desk_organization_id}

    def timelog(self):
        return self.timelog_token