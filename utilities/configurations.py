import configparser


def get_endpoint():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
