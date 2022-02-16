import inspect
import logging
import requests


class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)# filehandler object
        logger.setLevel(logging.INFO)
        return logger

    def getDefaultHeaders(self):
        headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "76676730ecmsh13ec1ab3f993394p17df12jsn244d98d47a21"
        }
        return headers

    def getRequest(self, url, headers, params):
        response = requests.request("GET", url=url, headers=headers, params=params)
        return response
