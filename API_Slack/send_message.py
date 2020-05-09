#!/usr/bin/python
import os
import requests

def send_message(message, channel_id):
	channel = '"channel": "{}"'.format(channel_id)
	text = '"text": "{}"'.format(message)
	data = '{'+channel+','+text+'}'

	url = 'https://slack.com/api/chat.postMessage'
	token = os.getenv('SLACK_BOT_USER_TOKEN').strip()
	token_bearer = "Bearer {}".format(token)
	headers = {
		'Content-type': 'application/json',
		'Authorization': token_bearer
	}

	response = requests.post(url, headers=headers, data=data)

	if response.status_code == 200:
		return True
	else:
		return False


def main():
	channels = {
		'crypto_prices': 'G013QFWC5Q9'
		}

	message = 'TEST'
	result = send_message(message, channels['crypto_prices'])
	print 'Result: {}'.format(result)

if __name__ == '__main__':
	main()
