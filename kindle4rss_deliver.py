import requests
from pyquery import PyQuery as pq
def kindle4rss_deliver():
    sess = requests.session()
    pay_load = {
        "email_address": "sptj1993@126.com",
        "password": "sptj1993",
        "persistent": "True"
    }
    login_url = "https://kindle4rss.com/login/"
    sess.get(login_url)
    sess.post(login_url, data=pay_load)
    send_url = "https://kindle4rss.com/send_now/"
    sess.post(send_url)
    logout_url = "https://kindle4rss.com/logout/"
    logout_page = sess.get(logout_url)
    return "delivered"

if __name__ == "__main__":
    print(kindle4rss_deliver())
