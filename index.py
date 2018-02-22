import web
import os, sys
urls = (
    '/', 'index'
)
class index:
    def GET(self):
        print("A visit encounter\n")
        return 'index '

if __name__ == "__main__":
    port = os.environ.get("PORT", "5000")
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', int(port)))
    app.run()
