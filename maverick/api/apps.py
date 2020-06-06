from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

class Moderator(AppConfig):
	name = 'moderator'

	def moderator(msg):
		##Add the moderator function here
		return msg