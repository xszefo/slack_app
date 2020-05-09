#!/usr/bin/python
import os
import requests


token = os.getenv('SLACK_BOT_USER_TOKEN').strip()
url = 'https://slack.com/api/conversations.list?token={}'.format(token)

response = requests.get(url)
x = response.json()

if response.status_code == 200:
	for channel in x['channels']:
		name = channel['name_normalized']
		is_member = channel['is_member']
		channel_id = channel['id']
		print '{} = {} | Is bot a member: {}'.format(name, channel_id, is_member)
