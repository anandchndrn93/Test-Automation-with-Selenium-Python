import configparser


class CommonUtil:

    def readPropertyFile(self):
        config = configparser.RawConfigParser()
        config.read(self)
        return config

    