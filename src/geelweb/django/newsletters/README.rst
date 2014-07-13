==================
django-newsletters
==================

A django app to manage subscription and unsubscription to newsletter.

Install
=======

From PyPi::

    pip install django-newsletters

From Source::

    python setup.py install

Configuring
===========

Add ``geelweb.django.newsletters`` to ``INSTALLED_APPS`` in your settings.

Create the db with ``python manage.py syncdb`` or ``python manage.py migrate newsletters`` if you are using `south <http://south.aeracode.org/>`_

Template tags
=============

Load template tags with ``{% load newsletters_tags %}``

newsletter_form
---------------

Display a form to subscribe to the newsletter.

::
    {% newsletter_form %}

The url where redirect after the email was registered can be sets using the
first parameter::

    {% newsletter_form '/thank-you' %}
