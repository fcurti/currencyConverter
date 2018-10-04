.. image:: https://raw.githubusercontent.com/fcurti/currencyconverter/master/logo/logo.png

This is a pythonic currency converter REST API using cherryPy, just for fun.

The REST API could be containerized using the provided Dockerfile or using docker-compose.

Automated test is powered by python unittest suite.

The CurrencyConverter class is inspired to another git project with some customization in order to digest an exchange rate source in XML format. The time to market has been improved in this way.

WebApp and unitTest are Python 3.6 certified.

Currency data sources
---------------------

The exchange rate source in use is the `European Central Bank <https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml>`_.

It contains the last 90s days exchange rate.

The webapp dynamically retrieve the latest xml file at project startup time and reload the exchange rate resource each day automatically during the 1st daily user GET.


Installation
------------

You can install directly after cloning typing git clone https://github.com/fcurti/currencyConverter on your fileSystem :

.. code-block:: bash

  $ python setup.py install --user
 
 
Run WebServer
------------

The python setup.py install the currencyConverter script in your home.

To be sure it runs please add $HOME/.local/bin on your PATH env.

.. code-block:: bash

  $ export PATH=${PATH}:$HOME/.local/bin

.. code-block:: bash
 
  $ currencyConverter

  with log redirection
  $ mkdir log && currencyConverter > ./log/currencyConverter.log 2>&1 &
  
  
API reference
------------
 
The convert currency entry point

http://localhost:8080/convert

HTTP Parameters

* amount :: the amount to be converted (mandatory)
* src_currency :: the amount's currency (default EUR)
* dest_currency :: the currency to convert the amount (default USD)
* reference_date :: the reference date for the currency exchange rate in YYYY-MM-DD format ( default is yesterday )

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

Using docker-compose as follow

.. code-block:: bash

  $ docker-compose up --build

Or 

build the Docker image using the following command

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
  
  or using docker-compose
  
  $ docker-compose logs
  
UNIT TEST
---------

Unit test are implemented in unitTest.py.

Assertion:

webServerRunning
  check if webServer is up & running
  
amountConverted
  check if the amount has been converted

badCurrency
  check if the provided src_currency is supported
  
Run unit test typing the following, using python version 3.6

.. code-block:: bash
 
  $ python unitTest.py
  
