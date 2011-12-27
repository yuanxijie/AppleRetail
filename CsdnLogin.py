__author__ = 'yuan'

import urllib
import urllib2
import cookielib

url = "http://passport.csdn.net/account/login"

class Csdn:
    cookie_file = "./cookie.txt"
    def __init__(self, user, passwd):
        self.username = user
        self.passwd = passwd
    def __login(self):
        ckjar = cookielib.MozillaCookieJar(Csdn.cookie_file)
        ckproc = urllib2.HTTPCookieProcessor(ckjar)
        opener = urllib2.build_opener(ckproc)


