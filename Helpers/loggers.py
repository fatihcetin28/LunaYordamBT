import logging


def openYordamLogger():
    logga = logging.getLogger("OpenYordamLogger")
    logga.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s-%(asctime)s-%(message)s", datefmt="%d/%m/%Y-%H:%M:%S"
    )
    file_handler = logging.FileHandler("opening.log")
    file_handler.setFormatter(formatter)
    logga.addHandler(file_handler)
    return logga


def OduncVerLogger():
    logga = logging.getLogger("OduncLogger")
    logga.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s-%(asctime)s-%(message)s", datefmt="%d/%m/%Y-%H:%M:%S"
    )
    file_handler = logging.FileHandler("odunc.log")
    file_handler.setFormatter(formatter)
    logga.addHandler(file_handler)
    return logga


def IadeAlLogger():
    logga = logging.getLogger("IadeLogger")
    logga.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s-%(asctime)s-%(message)s", datefmt="%d/%m/%Y-%H:%M:%S"
    )
    file_handler = logging.FileHandler("iade.log")
    file_handler.setFormatter(formatter)
    logga.addHandler(file_handler)
    return logga


def UyariLogger():
    logga = logging.getLogger("UyariLogger")
    logga.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s-%(asctime)s-%(message)s", datefmt="%d/%m/%Y-%H:%M:%S"
    )
    file_handler = logging.FileHandler("uyari.log")
    file_handler.setFormatter(formatter)
    logga.addHandler(file_handler)
    return logga
