#/!usr/bin/env python
import sys
import pyquery

if __name__ == '__main__':
  url = sys.argv[1]
  empty = pyquery.PyQuery(Url=url)('a[href=""]')
  if empty:
    print '%s empty links' % len(empty)
  else:
    print 'all good'
