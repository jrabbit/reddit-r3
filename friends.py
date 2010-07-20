#Jrabbit (c) 2010 GPL v3 or later.
from BeautifulSoup import BeautifulSoup
import re
import urllib2
import urllib

def grab(user, passwd):
    o = urllib2.build_opener( urllib2.HTTPCookieProcessor() )
    urllib2.install_opener( o )
    values = {'user' : user, 'passwd' : passwd}
    url = 'http://www.reddit.com/post/login'
    data = urllib.urlencode(values)
    o.open(url, data)
    f = o.open('http://www.reddit.com/prefs/friends/')
    the_page = f.read()
    f.close()
    return the_page

def friends(user, passwd):
    html = grab(user, passwd)
    soup = BeautifulSoup(html)
    links = soup.findAll('a', href=re.compile('^http://www.reddit.com/user/.*'))
    #the first one is always yourself
    friends = []
    for link in links:
        friends.append(str(BeautifulSoup(str(link)).a.contents))
    return friends


if __name__ == "__main__":
    import sys
    user = sys.argv[1]
    passwd = sys.argv[2]
    print friends(user, paswd)

