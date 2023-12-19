from config import conf, load_config

def run():
    # load config
    load_config()
    
    # create channel
    channel_name = conf().get("channel_type", "wx")
    
    