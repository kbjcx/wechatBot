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