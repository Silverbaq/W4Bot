class Streamer(object):
    def __init__(self, user_login):
        self.user_login = user_login
        self.anounce = True
        self.stream_started = True

    def should_be_anounced(self, online):
        if self.anounce and online:
            self.anounce = False
            self.stream_started = True
            return True
        elif self.anounce is False and online:
            return False
        elif self.anounce and not online:
            return False
        elif self.anounce is False and not online:
            self.anounce = True
            self.stream_started = False
            return True
