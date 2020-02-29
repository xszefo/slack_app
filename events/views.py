# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from slackclient import SlackClient

import os


# Create your views here.
class Events(APIView):
    def post(self, request, *args, **kwargs):
        SLACK_VERIFICATION_TOKEN = os.getenv('SLACK_VERIFICATION_TOKEN')
        SLACK_BOT_USER_TOKEN = os.getenv('SLACK_BOT_USER_TOKEN')
        slack_message = request.data

        print slack_message

        Client = SlackClient(SLACK_BOT_USER_TOKEN)

        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            print "Error! Wrong token\nOur: {}\nReceived: {}\n".format(SLACK_VERIFICATION_TOKEN, slack_message.get('token'))
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message, status=status.HTTP_200_OK)
        
        # greet bot
        if 'event' in slack_message:
            event_message = slack_message.get('event')

            # process user's message
            user = event_message.get('user')                      
            text = event_message.get('text')                      
            channel = event_message.get('channel')                
            
            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message' or user == 'UU7ERFFNW':     
                return Response(status=status.HTTP_200_OK)        


            bot_text = 'Hi <@{}> :wave:'.format(user)           
            if 'hi' in text.lower():                              
                Client.api_call(method='chat.postMessage', channel=channel, text=bot_text)                    
                return Response(status=status.HTTP_200_OK)

            elif 'uptime' in text.lower():
                bot_text = os.system('uptime')
                Client.api_call(method='chat.postMessage', channel=channel, text=bot_text)                    
                return Response(status=status.HTTP_200_OK)
            elif '@UU7ERFFNW' in text:
                Client.api_call(method='chat.postMessage', channel=channel, text='<@UU7ERFFNW> at your service, how can I help?')                    
                return Response(status=status.HTTP_200_OK)
            
            #else:
            #    bot_text = '{}? Ale o co kaman?'.format(text)
            #    Client.api_call(method='chat.postMessage', channel=channel, text=bot_text)                    
            #    return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)

