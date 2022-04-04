import requests
import json
import sys
import socket

filename = sys.argv[3]

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))

image_url = "http://" + get_ip_address()  + "/media/" + str(filename)

webhook = "https://hooks.slack.com/services/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"
payload = {"text": image_url, "channel": "#krmitko", "username": "Ptace", "icon_emoji": ":bird:",
"blocks": [
    	{
    		"type": "section",
    		"block_id": "section567",
    		"text": {
    			"type": "mrkdwn",
    			"text": "<" + image_url + "|Nekdo je v krmitku!>"
    		},
    		"accessory": {
    			"type": "image",
    			"image_url": image_url,
    			"alt_text": "Ptacek!"
    		}
    	}
    ]
}

send_slack_message(payload, webhook)
