import os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = 'C:/Users/d3nw3/PycharmProjects/book_exercise'
port = 80

os.chdir(webdir)
svraddr = ("", port)
svrobj = HTTPServer(svraddr, CGIHTTPRequestHandler)

svrobj.serve_forever()
