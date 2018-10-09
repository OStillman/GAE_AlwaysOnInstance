import logging
import time
import webapp2

from google.appengine.api import runtime
from google.appengine.api import background_thread

GLOBAL_COUNTER = 1

class Shutdown(Exception):
    pass

def shutdown():
    logging.info("Shutdown hook called")
    raise Shutdown