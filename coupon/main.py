
import time
import requests

scheduler_time = "2022-06-23 01:38"



requestUrls = ['https://a.jd.com/indexAjax/getCoupon.html?callback=jQuery4210242&key=0271DFD6890D3B60ACB8BA8A9E49BEB1664AD13489F04377920C94803702498714239DEE84DADDC95AA8BD5EF3464CAD158CA130532CCF95784707DDD6EDCE43A11403D4981984F0688DE092042C546AD7456D7A4F8CCF2C4B6E027C314240AB5447131954E5451C87FAEA4E0395DFB39F707A5FBC72ACDBDB8CC33210D03204ED3B1D211CA8AEFD7ED6DB98FE53FB62D2021691830F1B5E6494623C6161DF31&type=1&_=1655918157865']
refers = ['https://a.jd.com/']
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'

def getCookie():
    with open("coupon/cookie.txt") as f:
        cookies = {}
        for line in f.read().split(";"):
            name,value = line.strip().split("=",1)
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






 








