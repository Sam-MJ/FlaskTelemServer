import os


class Config(object):
    GREETINGS = "Hello!"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "default-key-for-devs"
