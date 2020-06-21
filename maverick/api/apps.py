from django.apps import AppConfig
import pandas
import json

from .mid import mediatorCall

class ApiConfig(AppConfig):
    name = 'api'

class Moderator(AppConfig):
	name = 'moderator'

	def moderator(msg):
		# qa=mediatorCall(msg)
		# output=qa.run_query()
		# return output
		try:
			qa=mediatorCall(msg)
			output=qa.run_query()
			return output
		except:
			return {'msg':"I don't know what to make of it. Please refer to ReadMe.", 'data': None}
