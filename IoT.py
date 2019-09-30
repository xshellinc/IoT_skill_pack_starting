# -*- Coding: utf-8 -*-

import os
import subprocess
import datetime
from time import sleep

def main():
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%Y/%m/%d %H:%M:%S') + "Hello World from IoT device")
    print(os.environ.get('LANG'))
    #print(os.environ.get('RemoteENV'))


if __name__ == '__main__':
    while True:
        main()
        sleep(5)
