#Reddit offline mirror

import simplejson as json
import urllib2
import urlparse

def info(privurl):
    queries = urlparse.urlparse(privurl).query
    return [quries['user'], queries['feed']]


def consturls(secret, user):
    #http://www.reddit.com/.json?feed=secret&user=user
    #http://www.reddit.com/user/%s/liked.json?feed=seret&user=%s etc.
    urls = {}
    
    for name, url in urls:
        jsonsaver(name, url)

def jsonsaver(name, url):
    response = urllib2.urlopen(i)
    
    json = response.read()
    
    f = open("%s.json", "w") % name
    f.write(json)
    f.close()

if __name__ == "__main__":
    import sys
    privurl = sys.argv[1]
    queries = urlparse.urlparse(privurl).query
    print urlparse.parse_qs(queries)['feed']