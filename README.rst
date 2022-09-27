This is a django app that wraps `MapServer`_

It makes it possible to use MapServer through django.

.. _mapserver: http://mapserver.org

Installation
============

0. Create a virtualenv to hold the installation (This step is
   optional, but highly reccommended).

   .. code:: bash

      virtualenv venv
      source venv/bin/activate

#. Install mapserver along with the following system-wide dependencies:

   .. code:: bash

      sudo apt-get install cgi-mapserver python-mapscript

#. Install this repository using pip

   .. code:: bash

      pip3 install git+https://github.com/kssalanio/django-mapserver.git#egg=django-mapserver
