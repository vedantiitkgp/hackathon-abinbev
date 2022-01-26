import requests
import json


class token_generator:
    def __init__(self):
        self.client_id = '1000.WUCIMHQUFCB7SAA017YPAKHNM24MZV'
        self.client_secret = '158ced95cf806c905046819742ec9ea6c972708efb'
        self.grant_type = 'refresh_token'

        self.timelog_token = 'a7b02ce9a5518308ea2e26705d3c9de4'

        self.expense_refresh_token = '1000.e9c0fbb57bd7e1378e566664af108423.4cf3d0cc0c00e940b73219ace76a6e99'
        self.expense_organization_id = '60004975410'

        self.desk_refresh_token = '1000.69429abdcd7bfb9376aac4d6a77fdfdd.9b7729b3079fe4a0ebea5f1bc191b7b6'
        self.desk_organization_id = '60004975412'
        self.desk_scope = 'Desk.settings.READ,Desk.basic.READ,Desk.tickets.ALL,Desk.contacts.READ'

    def expense(self):
        url = 'https://accounts.zoho.in/oauth/v2/token?refresh_token='+self.expense_refresh_token + \
            '&client_id='+self.client_id+'&client_secret=' + \
            self.client_secret+'&grant_type='+self.grant_type
        response = requests.post(url)
        response_json = json.loads(response.text)
        oauth_token = response_json['access_token']
        return {'access_token': oauth_token, 'organization_id': self.expense_organization_id}

    def ticket(self):
        url = 'https://accounts.zoho.in/oauth/v2/token?refresh_token='+self.desk_refresh_token+'&grant_type=' + \
            self.grant_type+'&client_id='+self.client_id+'&client_secret=' + \
            self.client_secret+'&scope='+self.desk_scope
        response = requests.post(url)
        response_json = json.loads(response.text)
        oauth_token = response_json['access_token']
        return {'access_token': oauth_token, 'organization_id': self.desk_organization_id}

    def timelog(self):
        return self.timelog_token
