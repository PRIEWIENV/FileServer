#!/usr/bin/env python
#! coding: utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import logging
import tornado.options
class MyFile(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/avtest/(.*)", MyFile, {"path":"/home/FileServer/malware"})
        ]

        settings = dict(
            debug = True,
        )
        tornado.web.Application.__init__(self , handlers , **settings)

if __name__ == "__main__":
    tornado.options.define("port", default=80, type=int)
    tornado.options.parse_command_line()
    logging.info("Server Now Start Up")
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()
