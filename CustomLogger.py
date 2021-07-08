import logging

def GetLogger(loggerName="app"):
    # Gets or creates a logger
    logger = logging.getLogger(loggerName)  

    # set log level
    logger.setLevel(logging.WARNING)

    # define file handler and set formatter
    fileHandler = logging.FileHandler('{0}.log'.format(loggerName))
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(module)s : %(message)s')
    fileHandler.setFormatter(formatter)

    # add file handler to logger
    if len(logger.handlers)==0:
        logger.addHandler(fileHandler)
    return logger