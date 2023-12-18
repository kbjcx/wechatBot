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
    "single_chat_prefix": ["bot"], # 私聊时的触发前缀
    "single_chat_reply_prefix": "[bot] ", # 私聊bot回复的消息前缀
    "single_chat_reply_suffix": "", # 私聊bot回复的消息后缀
    "group_chat_prefix": ["@bot"], # 群聊时的触发前缀
    "group_chat_reply_prefix": "", # 群聊时自动回复的前缀
    "group_chat_reply_suffix": "", # 群聊时自动回复的后缀
    "group_chat_keyword": [], # 群聊时自动回复的关键字
    "group_at_off": False, # 群聊时是否关闭at bot的功能
    "group_name_white_list": [], # 允许触发bot的群名
    "group_name_keyword_white_list": [], # 允许触发bot的群名关键字
    "group_chat_in_one_session": [],  # 支持会话上下文共享的群名称
    "nick_name_black_list": [],  # 用户昵称黑名单
    "group_welcome_msg": "",  # 配置新人进群固定欢迎语，不配置则使用随机风格欢迎
    "trigger_by_self": False,  # 是否允许机器人触发
    "text_to_image": "dall-e-3",  # 图片生成模型，可选 dall-e-2, dall-e-3
    "image_create_prefix": ["画"],  # 开启图片回复的前缀
    "concurrency_in_session": 1,  # 同一会话最多有多少条消息在处理中，大于1可能乱序
    "image_create_size": "256x256",  # 图片大小,可选有 256x256, 512x512, 1024x1024
    "group_chat_exit_group": False, 
    "expires_in_seconds": 3600,  # 无操作会话的过期时间
    "character_desc": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流", # chatgpt人格描述
    "conversation_max_tokens": 1000,  # 支持上下文记忆的最多字符数
    "rate_limit_chatgpt": 20,  # chatgpt的调用频率限制
    "rate_limit_dalle": 50,  # openai dalle的调用频率限制
    # chatgpt api参数设置 https://platform.openai.com/docs/api-reference/chat/create
    "temperature": 0.9, # 0-1之间的浮点数，值越高，模型越倾向于随机性
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "request_timeout": 180,  # chatgpt请求超时时间，openai接口默认设置为600，对于难问题一般需要较长时间
    "timeout": 120,  # chatgpt重试超时时间，在这个时间内，将会自动重试
    # 语音设置
    "speech_recognition": True,  # 是否开启语音识别
    "group_speech_recognition": False,  # 是否开启群组语音识别
    "voice_reply_voice": False,  # 是否使用语音回复语音，需要设置对应语音合成引擎的api key
    "always_reply_voice": False,  # 是否一直使用语音回复
    "voice_to_text": "openai",  # 语音识别引擎，支持openai,baidu,google,azure
    "text_to_voice": "openai",  # 语音合成引擎，支持openai,baidu,google,pytts(offline),azure,elevenlabs
    "text_to_voice_model": "tts-1",
    "tts_voice_id": "alloy",
    # baidu 语音api配置， 使用百度语音识别和语音合成时需要
    "baidu_app_id": "",
    "baidu_api_key": "",
    "baidu_secret_key": "",
    # 服务时间限制，目前支持itchat
    "chat_time_module": False,  # 是否开启服务时间限制
    "chat_start_time": "00:00",  # 服务开始时间
    "chat_stop_time": "24:00",  # 服务结束时间
    # 翻译api
    "translate": "baidu",  # 翻译api，支持baidu
    # baidu翻译api的配置
    "baidu_translate_app_id": "",  # 百度翻译api的appid
    "baidu_translate_app_key": "",  # 百度翻译api的秘钥
    # itchat的配置
    "hot_reload": False,  # 是否开启热重载
    # wechaty的配置
    "wechaty_puppet_service_token": "",  # wechaty的token
    # chatgpt指令自定义触发词
    "clear_memory_commands": ["#清除记忆"],  # 重置会话指令，必须以#开头
    # channel配置
    "channel_type": "wx",  # 通道类型
    "subscribe_msg": "",  # 订阅消息
    "debug": False,  # 是否开启debug模式，开启后会打印更多日志
    "appdata_dir": "",  # 数据目录
    # 插件配置
    "plugin_trigger_prefix": "$",  # 规范插件提供聊天相关指令的前缀，建议不要和管理员指令前"#"冲突
    # 是否使用全局插件配置
    "use_global_plugin_config": False,
}

class Config(dict):
    def 