#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Glavna stran, izberite cas ali loto:"}

        self.render_template("hello.html", params=params)

class lotoHandler(BaseHandler):
    def get(self):

        return self.render_template("loto.html")

class timeHandler(BaseHandler):
    def get(self):

        cas = datetime.datetime.now()
        params = {"sporocilo": "Glavna stran, izberite cas ali loto:","time" : cas}

        return self.render_template("time.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', lotoHandler),
    webapp2.Route('/time', timeHandler),
], debug=True)
