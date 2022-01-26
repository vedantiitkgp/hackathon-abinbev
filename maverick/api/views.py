from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .apps import Moderator, Webhook

# Create your views here.


class MessagesView(APIView):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            response = Moderator.moderator(request.data['message'])
            return Response(response, status=status.HTTP_200_OK)


@csrf_exempt
def WebHookView(request):
    req = json.loads(request.body)
    intent = req.get('queryResult').get('intent').get('displayName')
    params = dict(req.get('queryResult').get('parameters'))
    if req.get('queryResult').get('outputContexts'):
        params['flight_todo'] = req.get('queryResult').get('queryText')
        params['flight_place'] = req.get('queryResult').get('outputContexts')[
            0].get('parameters').get('geo-city')
        params['news_cat'] = req.get('queryResult').get('outputContexts')[
            0].get('parameters').get('category')
    resp = Webhook.moderator(intent, params)
    # fulfillmentText = {'fulfillmentText': resp}
    response = {
        "payload": resp,
    }
    return JsonResponse(response, safe=False)
