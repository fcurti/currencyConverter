.. image:: https://raw.githubusercontent.com/fcurti/currencyconverter/master/logo/logo.png

This is a pythonic currency converter REST API using cherryPy, just for fun.

Currency data sources
---------------------

The exchange rate source in use is the `European Central Bank <https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml>`_.

It contains the last 90s days exchange rate.


Installation
------------

You can install directly after cloning:

.. code-block:: bash

  $ python setup.py install --user
 
 
Run WebServer
------------
 
.. code-block:: bash
 
  $ currencyConverter

  with log redirection
  $ currencyConverter > ./log/currencyConverter.log 2>&1 &
  
  
API reference
------------
 
The convert currency entry point

  http://localhost:8080/convert

HTTP Parameters

.. code-block:: bash

	amount :: the amount to be converted (mandatory)

	src_currency :: the amount's currency (default EUR)

	dest_currency :: the currency to convert the amount (default USD)

	reference_date :: the reference date for the currency exchange rate in YYYY-MM-DD format ( default is today)

Some use cases


Convert 1 EUR in USD with today exchange rate

http://localhost:8080/convert?amount=1

Convert 1 EUR in USD using the exchange rate of 2010-09-28

http://localhost:8080/convert?amount=1&src_currency=EUR&dest_currency=USD&reference_date=2018-09-28

Date bad format

http://localhost:8080/convert?amount=10&src_currency=EUR&dest_currency=USD&reference_date=228

Currency does not exist

http://localhost:8080/convert?amount=10&src_currency=FL&dest_currency=BRR

No exchange rate for the provided date

http://localhost:8080/convert?amount=10&src_currency=EUR&dest_currency=USD&reference_date=2010-09-25



  
