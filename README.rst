.. image:: https://raw.githubusercontent.com/fcurti/currencyconverter/master/logo/logo.png

This is a pythonic currency converter API

Currency data sources
---------------------

The default source is the `European Central Bank <http://www.ecb.int/>`_. This is the ECB historical rates for 42 currencies against the Euro since 1999.
It can be downloaded here: `eurofxref-hist.zip <http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip>`_.
The converter can use different sources as long as the format is the same.


Installation
------------

You can install directly after cloning:

.. code-block:: bash

  $ python setup.py install --user
 
 
Run WebServer
------------
 
.. code-block:: bash
 
  $ currencyConverter > ./log/currencyConverter.log 2>&1 &
  
  
API reference
------------

.. code-block:: bash
 
The convert currency AP entry point
 
http://localhost:8080/convert
 
HTTP Parameters

amount :: the amount to be converted

src_currency :: the amount's currency

dest_currency :: the currency to convert the amount

reference_date :: the reference date for the currency exchange rate
