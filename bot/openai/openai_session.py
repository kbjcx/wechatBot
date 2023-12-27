from bot.session_manager import Session
from common.log import logger

class OpenAISession(Session):
    def __init__(self, session_id, system_prompt=None, model="text-davinci-003"):
        super().__init__(session_id, system_prompt)
        self.model = model
        self.reset()
        
    