from sys import stdout as ss
import locale
import lxml.etree

def print_r(s):
    ss.write("%s \r" % (" " * 50))
    ss.write("%s \r" % s)
    ss.flush()

def truncate(s):
    return s[:50]

def format_number(n):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format("%d", n, 1)

def get_xml(s):
    return lxml.etree.fromstring(s)

