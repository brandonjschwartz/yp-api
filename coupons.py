import urllib
import urllib2
import optparse

host = 'http://api2.yp.com/listings/v1/coupons'
key = 'xxxxxxx'
# Get your API key at http://developer.yp.com/

# Search options

parser = optparse.OptionParser()
parser.add_option('-l', '--searchloc', dest='searchloc', help='Location to search - city, state, zip code. This is required')

options, args = parser.parse_args()

# Required options

if not options.listingid:
    parser.error('Where?')

# URL params

url_params = {}
if options.searchloc:
    url_params['searchloc'] = options.searchloc

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
