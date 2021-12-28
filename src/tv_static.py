# Jacob Miske
# GNU 3
# Televsion Static is a python program to track changes to html static sites over time
import time
import requests
from time import sleep
import datetime


def get_sites_to_check():
    sites_list = []
    with open("../sites.txt", mode="r") as sites_txt:
        for line in sites_txt:
            sites_list.append(line.rstrip())
    return sites_list

def get_html_from_url(url_string: str):
    print(requests.get(url = url_string).text)

def set_html_to_log():


if __name__ == "__main__":
   print("Static Site checker started")
   while True:
       a = get_sites_to_check()
       print(a)
       get_html_from_url(url_string=a[1])
       # Wait one hour
       # sleep(60 * 60)
   