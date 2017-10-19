# BLURT

Installation

You'll need Python as this is a Python program.

Install the Slack client using:

pip install slackclient

Then create a bot:

Slack Real Time Messaging (RTM) API

Slack grants programmatic access to their messaging channels via a web API. Go to the Slack web API page and sign up to create your own Slack team. You can also sign into an existing account where you have administrative privileges.

Use the sign in button on the top right corner of the Slack API page.

After you have signed in go to the Bot Users page(https://api.slack.com/bot-users).

Name your bot "blurt" then click the “Add bot integration” button.

Add a bot integration named blurt.

The page will reload and you will see a newly-generated access token. You can also change the logo to a custom design. For example, I gave this bot the Full Stack Python logo.

Copy and paste the access token for your new Slack bot.

Click the "Save Integration" button at the bottom of the page. Your bot is now ready to connect to Slack's API.

A common practice for Python developers is to export secret tokens as environment variables. Export the Slack token with the name SLACK_BOT_TOKEN:

export SLACK_BOT_TOKEN='your slack token pasted here'

Nice, now we are authorized to use the Slack API as a bot.

There is one more piece of information we need to build our bot: our bot's ID. Next we will write a short script to obtain that ID from the Slack API.
Obtaining Our Bot’s ID

It is finally time to write some Python code! We'll get warmed up by coding a short Python script to obtain StarterBot's ID. The ID varies based on the Slack team.

We need the ID because it allows our application to determine if messages parsed from the Slack RTM are directed at StarterBot. Our script also tests that our SLACK_BOT_TOKEN environment variable is properly set.

Create a new file named print_bot_id.py and fill it with the following code.

import os
from slackclient import SlackClient


BOT_NAME = 'blurt'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)

Our code imports the SlackClient and instantiates it with our SLACK_BOT_TOKEN, which we set as an environment variable. When the script is executed by the python command we call the Slack API to list all Slack users and get the ID for the one that matches the name "starterbot".

We only need to run this script once to obtain our bot’s ID.

python print_bot_id.py

The script prints a single line of output when it is run that provides us with our bot's ID.

Use the Python script to print the Slack bot's ID in your Slack team.

Copy the unique ID that your script prints out. Export the ID as an environment variable named BOT_ID.

(starterbot)$ export BOT_ID='bot id returned by script'

The script only needs to be run once to get the bot ID. We can now use that ID in our Python application that will run blurt.

