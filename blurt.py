# Built by Yusuf Dilawar

import os
import time
import markovify
from slackclient import SlackClient


# Blurt's ID as an environment variable
BOT_ID = "**********"

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "/"
text = ""
# instantiate Slack & Twilio clients
slack_client = SlackClient("**********")


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


def handle_command(channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    f = open("new2.txt")
    text_model = markovify.Text(f.read())
    reply = text_model.make_short_sentence(130)
    lines = open('new2.txt', 'r').readlines()
    lines_set = set(lines)
    out = open('new2.txt', 'w')
    try:
        out.write((slack_client.api_call("channels.info", channel='C6S115KUG'))["channel"]["latest"]["text"])
        out.write((slack_client.api_call("channels.info", channel='C0BB7JZ7H'))["channel"]["latest"]["text"])
        out.write((slack_client.api_call("channels.info", channel='C132BSJ3U'))["channel"]["latest"]["text"])
        out.write((slack_client.api_call("channels.info", channel='C0BB7JZ71'))["channel"]["latest"]["text"])
        out.write((slack_client.api_call("channels.info", channel='C20HTQX8B'))["channel"]["latest"]["text"])
    except:
        pass
    for line in lines_set:
        out.write(line)
    slack_client.api_call("chat.postMessage", channel=channel,
                            text=reply, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:

                # return text after the @ mention, whitespace removed
                return output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    if slack_client.rtm_connect():
        print("blurt connected and running!")
        while True:
            channel = parse_slack_output(slack_client.rtm_read())
            if channel:
                handle_command(channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")


