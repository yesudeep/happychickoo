#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 happychickoo.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import configuration

import logging
import utils
import tornado.web
import tornado.wsgi

from google.appengine.api import memcache
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from utils import BaseRequestHandler

logging.basicConfig(level=logging.DEBUG)

class IndexHandler(BaseRequestHandler):
    def get(self):
        self.render('index.html')

class ShowcaseHandler(BaseRequestHandler):
    def get(self):
        self.render('showcase.html')

class AboutHandler(BaseRequestHandler):
    def get(self):
        self.render('about.html')

class ContactHandler(BaseRequestHandler):
    def get(self):
        self.render('contact.html')

settings = {
    "debug": configuration.DEBUG,
    #"xsrf_cookies": True,
    "template_path": configuration.TEMPLATE_PATH,
}
urls = (
    (r'/', IndexHandler),
    (r'/about/', AboutHandler),
    (r'/contact/', ContactHandler),
    (r'/showcase/', ShowcaseHandler),
)
application = tornado.wsgi.WSGIApplication(urls, **settings)

def main():
    from gaefy.db.datastore_cache import DatastoreCachingShim
    DatastoreCachingShim.Install()
    run_wsgi_app(application)
    DatastoreCachingShim.Uninstall()

if __name__ == '__main__':
    main()
