#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cherrypy
import random
import string
from datetime import datetime
from platform import python_version
from currencyConverter.currency_converter import CurrencyConverter

class currencyConverterServer(object):
	
	def __init__(self,converter):
		self.converter=converter

	@cherrypy.expose
	def index(self):
		out= """<html>
          <head></head>
          <body>
			PYVERSION: %s
            <form method="get" action="convert">
              <input type="text" value="8" name="amount" />
              <button type="submit">CONVERT EUR IN USD</button>
            </form>
          </body>
        </html>"""
		return out %(python_version())
		
	@cherrypy.expose
	def convert(self, amount=0, src_currency="EUR", dest_currency="USD", reference_date=datetime.now().strftime("%y-%m-%d")):
		out = """<html>
					<body>						
						amount: %s<br />
						src_currency: %s<br />
						dest_currency: %s<br />
						in date: %s
						is: %s
					</body>
					</html>"""
							
		return out %(amount, src_currency, dest_currency, reference_date, self.converter.convert(amount, src_currency, dest_currency, reference_date))

def main():
	cConverter = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip')		
	cherrypy.quickstart(currencyConverterServer(cConverter))


if __name__ == '__main__':
    main()
