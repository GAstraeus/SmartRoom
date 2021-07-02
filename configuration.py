import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TUYA_CLIENT_ID = config['TUYA']['CLIENT_ID']
TUYA_CLIENT_SECRET = config['TUYA']['CLIENT_SECRET']
