import cherrypy
import random
import string

class Test1(object):
	@cherrypy.expose
	def index(self):
		return "Hello test1"

	@cherrypy.expose
	def gen(self, length=8):
		return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
	cherrypy.quickstart(Test1())

