import os
import sys
from collections import deque

import requests


class TextBasedBrowser:

    def __init__(self):
        self.history = deque()
        self.dir_for_file = 'dir'

    def create_dir(self):
        args = sys.argv
        if len(args) == 2:
            self.dir_for_file = args[1]
        try:
            os.mkdir(self.dir_for_file)
        except FileExistsError:
            pass

    def create_file(self, file_name, file_data):
        with open(f'{self.dir_for_file}/{file_name}.txt', 'w', encoding='utf-8') as file:
            file.write(file_data)

    def ask_site(self):
        while True:
            enter_site = input().strip()
            if enter_site == 'back':
                return 'back'
            elif enter_site == 'exit':
                return 'exit'
            else:
                return enter_site

    def check_read_file(self, filename):
        try:
            with open(f'{self.dir_for_file}/{filename}.txt', 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return 'no file'

    def back_history(self):
        if len(self.history) > 1:
            self.history.pop()
            previous = self.history.pop()
            self.work_with_site(previous)

    def work(self):
        self.create_dir()
        while True:
            site = self.ask_site()
            if site == 'exit':
                return
            elif site == 'back':
                self.back_history()
            elif site == 'error':
                print('error')
            else:
                self.history.append(site)
                self.work_with_site(site)

    def work_with_site(self, site):
        cutter = site.rfind('.', -5)
        if cutter != -1:
            site_short = site[:cutter]
            text_site = self.get_content(site)
            self.create_file(site_short, text_site)
            print(text_site)
        else:
            site_short = site
            check = self.check_read_file(site_short)
            if check == 'no file':
                print("Error: Incorrect URL\n")
                return
            else:
                print(check)

    def get_content(self, url):
        full_url = "http://" + url
        return requests.get(full_url).text


browser = TextBasedBrowser()
browser.work()
