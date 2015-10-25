import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

import django
from django.test.utils import get_runner
from django.conf import settings

django.setup()

TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests(['geelweb.django.newsletters'])
sys.exit(bool(failures))
