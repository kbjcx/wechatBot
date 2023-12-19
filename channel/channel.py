"""
Message sending channel abstract class
"""


class Channel(object):
    NOT_SUPPORT_REPLYTYPE = []

    def startup(self):
        '''
        init channel
        '''
        raise NotImplementedError

    def handle_text(self, msg):
        '''
        process when received message
        '''
        raise NotImplementedError

    def send(self, reply: Reply, context: Context):
        pass
