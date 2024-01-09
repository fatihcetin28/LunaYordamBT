import logging


def openYordamLogger():
    logga = logging.getLogger('OpenYordam')
    logga.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler('opening.log')
    file_handler.setFormatter(formatter)
    logga.addHandler(file_handler)
    return logga