#!/usr/bin/python
import SimpleHTTPServer
import SocketServer

PORT = 8888

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "<title>Jupyter Notebook</title>jupyter serving at port", PORT
httpd.serve_forever()
