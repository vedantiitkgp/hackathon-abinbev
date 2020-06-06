from django.apps import AppConfig
import pandas
import json

from mid import mediatorCall

class ApiConfig(AppConfig):
    name = 'api'

class Moderator(AppConfig):
	name = 'moderator'

	def moderator(msg):
		qa=mediatorCall(msg)
		output=qa.run_query(msg)
		return output
