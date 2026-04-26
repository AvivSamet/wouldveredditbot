import os
import praw.models

import re
from dotenv import load_dotenv
import pickle

load_dotenv()

SECRET = os.environ.get("SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

        


if __name__ == '__main__':
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        user_agent='wouldvebot by u/thefantasticphantasm',
        username=USERNAME,
        password=PASSWORD
    )
    for comment in reddit.subreddit('all').stream.comments():
        if comment.author is not None and comment.author.name != reddit.user.me().name:
            if regex_match := re.search(r"(would|could|should) of ", comment.body):
                print(f"Found {regex_match[1]}")
                comment.reply(f'Hi! I just wanted to let you know that you said "{regex_match[1]} of" when the correct spelling is "{regex_match[1]}\'ve" which is actually a contraction of "{regex_match[1]} have." Hope this helps!\n\n_I am a bot, and this action was performed automatically._')
