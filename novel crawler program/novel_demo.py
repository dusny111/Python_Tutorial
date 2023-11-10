# coding=utf-8
"""This is a test python programm"""
# * if __name__ == "__main__":
# !
# ?
# TODO
# @param

import configparser

# import requests


if __name__ == "__main__":
    # * read config
    config = configparser.ConfigParser()
    config.read(".*/config.ini")

    # * get config varibles
    url_target = config.get("website", "url_target")
    print(url_target)
