==================
Django newsletters
==================

A basic app to manage newsletter subscriptions.

Install
=======

from source::

    git clone https://github.com/geelweb/django-editos.git
    pip install ./django-editos/

Configuring
===========

Add ``geelweb.django.newsletters`` to ``INSTALLED_APPS``.

Update your db with ``python manage.py syncdb`` or ``python manage.py migrate
newsletters`` if you use `south <http://south.aeracode.org/>`_

Add the app urls to your urls.py::

    url(r'^newsletter/', include('geelweb.django.newsletters.urls'))

Templates tags
==============

newsletter_form
---------------

Render a one field form to add an email to the newsletter.:

    {% load newsletters_tags %}

    {% newsletter_form %}

