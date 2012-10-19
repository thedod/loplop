# Based on the SConscript of oplop's SL4A implementation
# https://code.google.com/p/oplop/source/browse/SL4A/SConscript
from __future__ import with_statement

import urllib
import urllib2


def qr_code(target, source):
    """Generate the QR code for the SL4A script using the Google Chart API.

    The docs on the chart API can be found at
    http://code.google.com/apis/chart/docs/gallery/qr_codes.html

    The zxing project's online QR code generator is at
    http://zxing.appspot.com/generator/

    """
    google_charts_api = 'http://chart.apis.google.com/chart'
    args = {'cht': 'qr', 'chs': '391x391'}
    with open(str(source), 'rb') as file:
        args['chl'] = 'loplop.py\n' + file.read()
    query = urllib.urlencode(args)
    url = urllib2.urlopen('?'.join([google_charts_api, query]))
    with open(str(target), 'wb') as file:
        file.write(url.read())


if __name__=='__main__':
    qr_code('qr_code_loplop_sl4a.png', 'loplop.sl4a.py')
