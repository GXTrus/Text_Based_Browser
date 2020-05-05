import os
import sys
from collections import deque


class TextBasedBrowser:

    def __init__(self):
        self.nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''
        self.bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
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
        with open(f'{self.dir_for_file}/{file_name}', 'w', encoding='utf-8') as file:
            file.write(file_data)

    def ask_site(self):
        while True:
            sites = ['bloomberg.com', 'bloomberg', 'nytimes.com', 'nytimes']
            enter_site = input().strip()
            if enter_site == 'back':
                return 'back'
            elif enter_site == 'exit':
                return 'exit'
            elif enter_site in sites:
                return enter_site
            else:
                return 'error'

    def check_read_file(self, filename):
        try:
            with open(f'{self.dir_for_file}/{filename}', 'r', encoding='utf-8') as file:
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
        site_short = site.rstrip(".com")
        file_name = 'self.' + site.replace('.', '_')
        if site == site_short:
            check = self.check_read_file(site_short)
            if check == 'no file':
                print("Error: Incorrect URL\n")
            else:
                print(check)
                return
        else:
            self.create_file(site_short, eval(file_name))
            print(eval(file_name))


browser = TextBasedBrowser()
browser.work()
