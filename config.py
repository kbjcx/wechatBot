# encoding:utf-8

import json
import logging
import os
import pickle

from common.log import logger

avaiable_config = {
    "openai_api_key": "",
    "openai_api_base": "https://api.openai.com/v1",
    "proxy": "",
    # chatgpt model
    "model": "gpt-3.5-turbo",
    # how to trigger the bot
    "single_chat_prefix": ["bot"],
    "single_chat_reply_prefix": "[bot] ",
    
}