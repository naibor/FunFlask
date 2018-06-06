class Configration(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY  = b'\x0b1k\x9e\x8b\x95\xf4;\xa7\xb5\xcc\xc8\xed\xb4e\xa0' 

class Development(Configration):
    DEBUG = True

class Testing(Configration):
    DEBUG= True

class Staging(Configration):
    DEBUG = True

class Production(Configration):
    DEBUG = False


