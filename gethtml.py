import urllib, urllib2, lxml.html, lxml.etree, json

# HTML
def get_html(url):
    return lxml.html.fromstring(urllib2.urlopen(url).read())

def to_string(html):
	return lxml.html.tostring(html, pretty_print=True)

def from_string(s):
	return lxml.html.fromstring(s)

# xml
def get_xml(url):
	return lxml.etree.fromstring(urllib2.urlopen(url).read())

def xml_to_string(xml):
	return lxml.etree.tostring(xml, pretty_print=True)

def xml_from_string(s):
	return lxml.etree.fromstring(xml)

# json
def get_json(url):
    return json.loads(urllib2.urlopen(url).read())
