import web

urls = (
    '/', 'home' # goes to the homepage class
)

app = web.application(urls, globals()) # start app

# Classes/Routes

class home:
    def GET(self):
        return "home"
    
if __name__ == "__main__": # ensures the code only runs when executed directly and not when imported as a module
    app.run()