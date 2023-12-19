# encoding:utf-8

from enum import Enum


class ReplyType(Enum):
    TEXT = 1
    VOICE = 2
    IMAGE = 3
    IMAGE_URL = 4
    VIDEO_URL = 5
    FILE = 6
    CARD = 7  # 微信名片
    InviteRoom = 8  # 邀请好友进群
    INFO = 9
    ERROR = 10
    TEXT_ = 11  # 强制文本
    VIDEO = 12
    MINIAPP = 13  # 小程序

    def __str__(self):
        return self.name


class Reply(object):
    def __init__(self, type: ReplyType = None, content=None):
        self.type = type
        self.content = content

    def __str__(self):
        return "Reply(type={}, content={})".format(self.type, self.content)
