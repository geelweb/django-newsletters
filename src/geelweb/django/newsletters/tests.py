from django.db import IntegrityError
from django.test import TestCase

from geelweb.django.newsletters.models import Newsletter

class NewsletterTest(TestCase):
    def test_uniqueness(self):
        item = Newsletter.objects.create(email="john@example.com")
        with self.assertRaises(IntegrityError):
            item = Newsletter.objects.create(email="john@example.com")

    def test_defaults(self):
        item = Newsletter.objects.create(email="john@example.com")
        self.assertTrue(item.optin)

    def test_unicode(self):
        item = Newsletter.objects.create(email="john@example.com")
        self.assertEqual(str(item), "john@example.com")

