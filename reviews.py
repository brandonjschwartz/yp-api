import urllib
import urllib2
import optparse

host = 'http://api2.yp.com/listings/v1/reviews'
key = 'xxxxx'
# Get your API key at http://developer.yp.com/

# Search options

parser = optparse.OptionParser()
parser.add_option('-l', '--listingid', dest='listingid', help='YP Listing ID. This value is required.')

options, args = parser.parse_args()

# Required options

if not options.listingid:
    parser.error('You need a listing to see any reviews!')

# URL params

url_params = {}
if options.listingid:
    url_params['listingid'] = options.listingid

def request(host, url_params, key):
    # Returns API response
    # Pull API URL
    encoded_params = ''
    if url_params:
        encoded_params = urllib.urlencode(url_params)
    url = '%s?%s&key=%s' % (host, encoded_params, key)
    print 'URL: %s' % (url,)

    # Connect to the API

    try:
        url2 = urllib2.Request(url, headers={'User-Agent': 'Python-API'})
        conn = urllib2.urlopen(url2, None)
        try:
            response = conn.read()
        finally:
            conn.close()
    except urllib2.HTTPError, error:
        response = 'You have a problem'
    return response

response = request(host, url_params, key)
print response
