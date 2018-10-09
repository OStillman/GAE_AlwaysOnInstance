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

def counter_loop():
    global GLOBAL_COUNTER
    try:
        while GLOBAL_COUNTER < 600:
            GLOBAL_COUNTER += 1
            time.sleep(1)
        logging.info("Shutting down after 600 cycles")
    except:
        logging.info("Counter loop saw shutdown")

