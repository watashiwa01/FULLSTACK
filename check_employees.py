import urllib.request
import sys

try:
    r = urllib.request.urlopen('http://127.0.0.1:5000/employees', timeout=5)
    html = r.read().decode('utf-8')
    print('LENGTH', len(html))
    print('CONTAINS_TABLE', '<table' in html)
    print('\nSNIPPET:\n', '\n'.join(html.split('\n')[:20]))
except Exception as e:
    print('ERROR:', e)
    sys.exit(1)