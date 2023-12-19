"""
Auto-replay chat robot abstract class
"""

from bridge.context import Context
from bridge.reply import Reply


class Bot(object):
    def reply(self, query, context: Context = None) -> Reply:
        """
        auto reply content
        :param query: received message
        :param context:
        :return:
        """
        raise NotImplementedError
