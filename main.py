#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime
import random





template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

def loto(maxstevilo,kolikokroglic):
    rezultati = []
    izrebanih = 0
    while izrebanih < kolikokroglic:
        #print i
        #print kolikokroglic
        #print maxstevilo
        cifra = random.randrange(1,maxstevilo)
        #print cifra
        if cifra not in rezultati:
            rezultati.append(cifra)
            izrebanih +=1
    rezultati.sort()
    return rezultati



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

class homeHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Homepage"}

        self.render_template("home.html", params=params)

class mojiprojHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Homepage"}

        self.render_template("moji.html", params=params)

class blogHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Homepage"}

        self.render_template("blog.html", params=params)

class kontaktHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Homepage"}

        self.render_template("kontakt.html", params=params)

class druzinaHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Homepage"}

        self.render_template("druzina.html", params=params)

class omeniHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "O meni"}

        self.render_template("omeni.html", params=params)


class lotoHandler(BaseHandler):
    def get(self):
        cifre = loto(39,7)
        params = {"stevilke":cifre }
        return self.render_template("loto.html", params=params)

class timeHandler(BaseHandler):
    def get(self):

        cas = datetime.datetime.now()
        params = {"sporocilo": "Glavna stran, izberite cas ali loto:","time" : cas}

        return self.render_template("time.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', lotoHandler),
    webapp2.Route('/time', timeHandler),
    webapp2.Route('/home', homeHandler),
    webapp2.Route('/home/omeni', omeniHandler),
    webapp2.Route('/home/moji', mojiprojHandler),
    webapp2.Route('/home/blog', blogHandler),
    webapp2.Route('/home/kontakt', kontaktHandler),
    webapp2.Route('/home/druzina', druzinaHandler),
], debug=True)
