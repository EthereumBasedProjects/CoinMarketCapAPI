slack_token = 'xoxb-96219606007-IB1odIQltboGSjjKhmARM2yM'
slack_channel = 'btcalert'
slack_icon_emoji = ''
slack_user_name = ''

import requests
import json

import logging
import os

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=slack_token)
logger = logging.getLogger(__name__)

# ID of the channel you want to send the message to
channel_id = "btcalert"


def post_message_to_slack(text, blocks = None):
  try:
      # Call the chat.postMessage method using the WebClient
      result = client.chat_postMessage(
          channel=channel_id, 
          text=text
      )
      logger.info(result)

  except SlackApiError as e:
      logger.error(f"Error posting message: {e}")

