# mini-heartbeat

I wrote this to have a raspberry pi send a heartbeat occasionally to a slack channel.

## Usage

Run:

    $ git clone https://github.com/nickodell/mini-heartbeat
    $ cd mini-heartbeat
    $ ./install.sh

You'll need to create the channel #heartbeat, or change hb.py to a different channel. Then, you need to generate an API key, and put it in the file 'creds.'

Then run:

    $ ./run.sh

Output:

    $ tail log
    {'args': {'token': '[snip]'}, 'ok': True}
    Sending This is 'host' with local IP of [snip], and public IP of [snip] ([snip].co.comcast.net)
    {'message': {'type': 'message', 'username': 'host bot', 'icons': {'image_64': 'https://slack.global.ssl.fastly.net/d4bf/img/emoji_2015_2/apple/1f916.png', 'emoji': ':robot_face:'}, 'subtype': 'bot_message', 'ts': '1462977283.249294', 'text': "This is 'host' with local IP of [snip], and public IP of [snip] ([snip].comcast.net)"}, 'channel': '[snip]', 'ok': True, 'ts': '1462977283.249294'}

You may want to add run.sh to your crontab to make the bot run regularly. 

## Dependencies

This project should install the dependencies if you run install.sh, but if that doesn't work, you need Python 3.x, slackclient, and websocket-client.
