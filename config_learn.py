# coding=utf-8
"""This is a test python programm"""
# * if __name__ == "__main__":
# !
# ?
# TODO
# @param

import configparser

# * config read
config = configparser.ConfigParser()
config.read("config.ini")

a = config.get("website", "url")
print(a)

# # * config write
# config = configparser.ConfigParser()

# config.add_section("database")

# config.set("database", "host", "localhost")
# config.set("database", "port", "3306")
# config.set("database", "user", "root")
# config.set("database", "password", "password")


# with open("config.ini", "a") as f:
#     config.write(f)
