#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cherrypy
import random
import string
import json
from datetime import datetime
from platform import python_version
from currencyConverter.currency_converter import CurrencyConverter
from currencyConverter.currency_converter import RateNotFoundError

class currencyConverterServer(object):
	
	def __init__(self,c):
		self.converter=c

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
		status='good'
		message='converted'
		amountConverted=0

		try:
			if not amount.strip():
				raise ValueError('amount parameter cannot be empty')
			
			amountConverted=self.converter.convert(amount, src_currency, dest_currency, datetime.strptime(reference_date, '%Y-%m-%d').date())
			#cherrypy.response.headers['Content-Type'] = 'application/json'	
			#return json.dumps(ret).encode('utf8')
		except (RateNotFoundError,ValueError) as e:
			amountConverted=''
			status='error'
			message=str(e)
		finally:
			ret={
				"amount": amountConverted,
				"currency": dest_currency,
				"status": status,
				'message': message
			}
			cherrypy.response.headers['Content-Type'] = 'application/json'			
			return json.dumps(ret).encode('utf8')

def main():
	c = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip')
	#cConverter = CurrencyConverter('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml')	
	cherrypy.quickstart(currencyConverterServer(c))


if __name__ == '__main__':
    main()
