import web

urls = (
    '/', 'home' # goes to the homepage class
)

app = web.application(urls, globals()) # start app

# Classes/Routes

class home:
    def GET(self):
        return "home"
    
if __name__ == "__main__":
    app.run()