import urllib
import urllib2
import optparse

host = 'http://api2.yp.com/listings/v1/listingmap'
key = '3dd19ebb13e05d4ce6fdbf98414dbaea'

# Search options

parser = optparse.OptionParser()
parser.add_option('-l', '--listingid', dest='listingid', help='YP Listing ID. This value is required.')
parser.add_option('-w', '--pixel_width', dest='pixel_width', help='Integer representing pixel width of the map. Defaults to 400')
parser.add_option('-u', '--pixel_height', dest='pixel_height', help='Integer representing pixel height of the map. Defaults to 400')
parser.add_option('-i', '--image_format', dest='image_format', help='String representing mime-type map. Defaults to GIF')
parser.add_option('-z', '--zoom', dest='zoom', help='Fraction from .1 to 1 for zoom factor of the map. Defaults to 1')
parser.add_option('-v', '--pan_vertical', dest='pan_vertical', help='Positive or negative number reflecting the percentage of the map to pan south (negative) or north (positive). Defaults to 0')
parser.add_option('-p', '--pan_horizontal', dest='pan_horizontal', help='Positive or negative number reflecting the percentage of the map to pan west (negative) or east (positive). Defaults to None')

options, args = parser.parse_args()

# Required options

if not options.listingid:
    parser.error('You need a listing to make a map of!')

# URL params

url_params = {}
if options.listingid:
    url_params['listingid'] = options.listingid
if options.pixel_width:
    url_params['pixel_width'] = options.pixel_width
if options.pixel_height:
    url_params['pixel_height'] = options.pixel_height
if options.image_format:
    url_params['image_format'] = options.image_format
if options.zoom:
    url_params['zoom'] = options.zoom
if options.pan_vertical:
    url_params['pan_vertical'] = options.pan_vertical
if options.pan_horizontal:
    url_params['pan_horizontal'] = options.pan_horizontal

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
