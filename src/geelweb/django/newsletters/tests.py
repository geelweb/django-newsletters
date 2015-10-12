from django.db import IntegrityError
from django.template import Template, Context
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


class TemplateTagTest(TestCase):
    TEMPLATE = Template("{% load newsletters_tags %}{% newsletter_form %}")
    TEMPLATE_WITH_ARGS = Template("""{% load newsletters_tags %}{% newsletter_form label="Give us your email" placeholder="Email" on_success="do_something();"%}""")

    def test_form(self):
        label = """<label for="id_email">%(label)s *</label>"""
        html = """<input
            class="form-control"
            id="newsletter_email"
            maxlength="254"
            name="email"
            placeholder="%(placeholder)s"
            required="required"
            type="text" />"""
        html_success = """<input type="hidden" name="on_success" value="%(on_success)s" >"""

        content = self.TEMPLATE.render(Context({}))
        self.assertInHTML(label % {'label': 'Subscribe to our newsletter'}, content)
        self.assertInHTML(html % {'placeholder': 'Enter your email address'}, content)

        content = self.TEMPLATE_WITH_ARGS.render(Context({}))
        self.assertInHTML(label % {'label': 'Give us your email'}, content)
        self.assertInHTML(html % {'placeholder': 'Email'}, content)
        self.assertInHTML(html_success % {'on_success': 'do_something();'}, content)
