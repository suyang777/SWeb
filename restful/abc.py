# -*- coding:utf-8 -*-
"""
    index action demo
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async


@url(r"/")
class OKHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        #self.write('Hello world suyang!')
        self.render('index.html',name='comger',data={'na':'abccc','nb':'asdfas'})

    def post(self):
    	self.write('ok1')

@url(r"/post")
class PostHandler(ContextHandler,tornado.web.RequestHandler):
    def post(self):
    	uname = self.get_argument('username')
    	pwd = self.get_argument('password')
    	chk = self.get_argument('check')
    	self.write(dict(uname=uname,pwd=pwd,check=chk))

@url(r"/pro")
class Test(ContextHandler,tornado.web.RequestHandler):
	"""docstring for test"""
	def post(self):
		self.render('index.html',name='8888',data={'a':'1','b':'2'})
