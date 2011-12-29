__author__ = 'yuan'

import urllib
import urllib2
import cookielib

url = "http://passport.csdn.net/account/login"
#url = "http://www.baidu.com"
class Csdn:
    cookie_file = "./cookie.txt"
    def __init__(self, user, passwd):
        self.username = user
        self.passwd = passwd
    def login(self):
        ckjar = cookielib.MozillaCookieJar(Csdn.cookie_file)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1')
        res = opener.open(req)
        html = res.read()
        res.close()

        print html
        ckjar.save(filename=self.cookie_file, ignore_discard=False, ignore_expires=False)

        req = urllib2.Request("http://counter.csdn.net/pv.aspx?id=20")
        req.add_header('Referer', url)
        res = opener.open(req)
        print res.read();
        res.close()
        ckjar.save(filename=self.cookie_file, ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    csdn = Csdn('hotforever', 'baidu_c0m')
    csdn.login()

