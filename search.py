import urllib
import urllib2
import optparse

host = 'http://api2.yp.com/listings/v1/search'
key = 'xxxxx'
# Get your API key at http://developer.yp.com/

# Search options

parser = optparse.OptionParser()
parser.add_option('-t', '--term', dest='term', help='Search term')
parser.add_option('-g', '--searchloc', dest='searchloc', help='Location, either city, state, zip code, street, neighborhood, or point of interest')
parser.add_option('-p', '--phonesearch', dest='phonesearch', help='Search by phone number formatted as 10 digit integer')
parser.add_option('-l', '--listingcount', dest='listingcount', help='Total number of listings to return')
parser.add_option('-u', '--shorturl', dest='shorturl', help='Set to true for short URL format. Typically for SMS apps')
parser.add_option('-f', '--format', dest='format', help='Either XML or JSON, YP defaults to XML but this API defaults to JSON')
parser.add_option('-n', '--pagenum', dest='pagenum', help='The page index of the block of results to return, defaults to 1')
parser.add_option('-s', '--sort', dest='sort', help='Select sort criteria for organic results, either distance or alphabetically')
parser.add_option('-r', '--radius', dest='radius', help='Max radius in miles for organic results')

options, args = parser.parse_args()

# Required options

if not options.term and not options.searchloc and not options.phonesearch and not options.listingcount and not options.radius:
    parser.error('You need at least ONE option')

# URL params

url_params = {}
if options.term:
    url_params['term'] = options.term
if options.searchloc:
    url_params['searchloc'] = options.searchloc
if options.phonesearch:
    url_params['phonesearch'] = options.phonesearch
if options.listingcount:
    url_params['listingcount'] = options.listingcount
if options.shorturl:
    url_params['shorturl'] = options.shorturl
if options.format:
    url_params['format'] = options.format
if options.pagenum:
    url_params['pagenum'] = options.pagenum
if options.sort:
    url_params['sort'] = options.sort
if options.radius:
    url_params['radius'] = options.radius

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
