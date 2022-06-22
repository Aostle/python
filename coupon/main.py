
import time
import requests

scheduler_time = "2022-06-22 20:00"



requestUrls = []
refers = []
user_agent = ''

def getCookie():
    with open("cookie.txt") as f:
        cookies = {}
        for line in f.read().split(";"):
            name,value = line.strip.split("=",1)
            cookies[name] = value
        return cookies

headers  = {}
headers['User-Agent'] = user_agent

def getCoupon():
    print("waitting......")
    while True:
        now = time.strftime("%Y-%m-%d %H:%M",time.localtime())
        if now == scheduler_time:
            for i in range(len(requestUrls)):
                headers['Referer'] = refers[i]
                r = requests.get(requestUrls[i],headers=headers,cookies=getCookie())
                print(r.text)
            break

if __name__== '__main__':
    getCoupon()






 








