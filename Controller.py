import web

urls = (
    '/', 'home' # goes to the homepage class
)

app = web.application(urls, globals()) # start app