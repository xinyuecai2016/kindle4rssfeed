import web
import os, sys, pytz, time ,datetime
from kindle4rss_deliver import kindle4rss_deliver
urls = (
    '/', 'index'
)
def is_the_right_time_to_deliver():
    tz = pytz.timezone('Asia/Shanghai')
    current_hour = datetime.datetime.now(tz).hour
    if(current_hour==7):
        return True
    else:
        return False
class index:
    def GET(self):
        return 'index'
    def POST(self):
        # current_data=web.data()
        # if(current_data==b'kindle4rss'):
        #     kindle4rss_deliver()
        # else:
        #     print("error")
        return 'index'
if __name__ == "__main__":
    port = os.environ.get("PORT", "5000")
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', int(port)))
    app.run()
