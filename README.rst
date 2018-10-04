.. image:: https://raw.githubusercontent.com/fcurti/currencyconverter/master/logo/logo.png

This is a pythonic currency converter REST API using cherryPy, just for fun.

Python 3.6 certified.

Currency data sources
---------------------

The exchange rate source in use is the `European Central Bank <https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml>`_.

It contains the last 90s days exchange rate, refreshed each day.


Installation
------------

You can install directly after cloning:

.. code-block:: bash

  $ python setup.py install --user
 
 
Run WebServer
------------

The python setup.py install the currencyConverter script in your home.
To be sure it runs please add ~.local/bin to the PATH

.. code-block:: bash

  $ export PATH=${PATH}:~.local/bin

.. code-block:: bash
 
  $ currencyConverter

  with log redirection
  $ currencyConverter > ./log/currencyConverter.log 2>&1 &
  
  
API reference
------------
 
The convert currency entry point

http://localhost:8080/convert

HTTP Parameters

* amount :: the amount to be converted (mandatory)
* src_currency :: the amount's currency (default EUR)
* dest_currency :: the currency to convert the amount (default USD)
* reference_date :: the reference date for the currency exchange rate in YYYY-MM-DD format ( default is today)

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


DOCKER
------

You may also run the currencyConverter API using docker.

Build the Docker image using the following command

.. code-block:: bash
 
  $ docker build -t fcurti/currencyconverter .
	
Run container

.. code-block:: bash
 
  $ docker run -tid -p 8080:8080 --name="currency_converter" fcurti/currencyconverter
  
Open browser @ this url

http://localhost:8080/convert?amount=1

Logs

.. code-block:: bash

  $ docker logs currency_converter
  
