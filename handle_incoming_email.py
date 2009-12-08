import logging
import email # pyflakes:ignore
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("From: " + mail_message.sender)
        logging.info("To:" + mail_message.to)
        logging.info("Subject: " + mail_message.subject)
        logging.info("Date: " + mail_message.date)

        (type, payload) = mail_message.bodies(content_type='text/plain').next()
        text = payload.decode()

        logging.info("Text: %s" % text)

application = webapp.WSGIApplication([LogSenderHandler.mapping()], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()


