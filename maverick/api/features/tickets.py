import requests

class ticket_func:
	def __init__(self):
		#SCOPE = Desk.settings.READ,Desk.basic.READ,Desk.tickets.ALL,Desk.contacts.READ
		self.baseurl = "https://desk.zoho.in/api/v1"
		self.orgid = "60004833729"
		self.token = "1000.b63eaf9bf2e61351a4a704674076e069.2936d9ad0762837da03362d6fffb97ff"
		
		self.headers = {'orgId': self.orgid, 'Authorization': 'Zoho-oauthtoken '+self.token}
		# self.customerId = '26154000000064365'
		# self.deptId = '26154000000010772'

	def create_ticket(self, customerId, deptIdtitle):
		title = title.replace('"', '')
		data = {'subject': title, 'departmentId': deptId, 'contactId': customerId}
		response = requests.post(self.baseurl+'/tickets', json = data, headers = self.headers)
		output = {'msg': response.text, 'data': None}
		return output
	
	def show_tickets(self):
		response = requests.get(self.baseurl+'/tickets', headers = self.headers)
		return {'msg': None, 'data': pd.DataFrame(json.loads(response.text)['data'])[['id', 'ticketNumber', 'email', 'phone', 'subject', 'status', 'createdTime']]}

	def close_ticket(self, ticketId):
		data = {'ids': [ticketId]}
		response = requests.post(self.baseurl+'/closeTickets', json=data, headers=self.headers)
		msg = 'Ticket Closed' if response.status_code == 200 else 'Some error while processing.'
		return {'msg': msg, 'data': None}

	def show_customers(self):
		response = requests.get(self.baseurl + '/contacts', headers=self.headers)
		return {'msg': None, 'data': pd.DataFrame(json.loads(response.text)['data'])[['id', 'firstName', 'lastName', 'email', 'type']]}

	def show_departments(self):
		response = requests.get(self.baseurl + '/departments', headers=self.headers)
		return {'msg': None, 'data': pd.DataFrame(json.loads(response.text)['data'])[['id', 'name', 'description']]}