from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

from .apps import Moderator

# Create your views here.
class MessagesView(APIView):
	
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			reply = Moderator.moderator(request.data['message'])
			response = {'data': reply}
			return Response(response, status=status.HTTP_200_OK)