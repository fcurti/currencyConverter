.. image:: https://raw.githubusercontent.com/fcurti/currencyconverter/master/logo/logo.png

This is a pythonic currency converter API using cherryPy, just for fun.

Currency data sources
---------------------

The exchange rate source in use is the `European Central Bank <https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml>`_.


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

.. code-block:: bash
 
The convert currency AP entry point
 
http://localhost:8080/convert
 
HTTP Parameters

amount :: the amount to be converted (mandatory)

src_currency :: the amount's currency (default EUR)

dest_currency :: the currency to convert the amount (default USD)

reference_date :: the reference date for the currency exchange rate in YYYY-MM-DD format
