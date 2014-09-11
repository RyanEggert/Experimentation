import cgi
from google.appengine.api import users
import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><textarea name="content" rows="3" cols="80"></textarea></div>
      <div><input type="number" name="Quantity" min="1" max = "6"></input></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        numWrite = numbermanipulation(self.request.get('Quantity'))
        self.response.write('\n')
        self.response.write(numWrite) 
        self.response.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)


def numbermanipulation(numIn):
  numOut = int(numIn) * 30
  return numOut


def main():
    app.run()