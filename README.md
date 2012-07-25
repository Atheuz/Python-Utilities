Python-Utilities
================

General python utilities, higher level abstractions and other things.

gethttp.py
----------
Contains functions for retrieving and handling HTML, XML, JSON from the internet.

###  HTML

#### get_html(url)

	Retrieves an html page via urllib2 and returns as an lxml.html object.
	
#### to_string(html)

	Turns an lxml.html object into a string.
	
#### from_string(s)

	Turns a string into an lxml.html object.

### XML	

#### get_xml(url)
	
	Equivalent of the HTML function, except it's for XML.

#### xml_to_string(xml)

	Equivalent of the HTML function, except it's for XML.

#### xml_from_string(s)

	Equivalent of the HTML function, except it's for XML.
	
### JSON
	
#### get_json(url)

	Retrieves an json page via urllib2 and returns as a dictionary object, processed by the json module.


convenience.py
--------------
Contains output functions.

#### print_r(s)
    
    A print function to be used for return carriage printing, meaning overwritable text.

#### truncate(s)

    A truncation function, basically takes a string and outputs the first 50 letters of it.

#### format_number(n)

    A number formatting function, that takes a number like 1000000 and outputs 1.000.000
