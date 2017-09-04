#!/usr/bin python
# -*- encoding: utf-8 -*-

import os.path

import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web

from tornado.options import define, options

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('managelogin.html')

