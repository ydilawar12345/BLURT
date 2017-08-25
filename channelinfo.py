# Built by Yusuf Dilawar
from slackclient import SlackClient

slack_client = SlackClient("**********")  #"SLACK_API_TOKEN"


slack_client.api_call("channels.list")


def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


if __name__ == "__main__":
    channels = list_channels()
    if channels:
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
    else:
        print("Unable to authenticate.")
