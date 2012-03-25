from django.test import TestCase
from django.conf import settings
from os import path
import urllib2, urllib

class CloudoooTestCase(TestCase):

  def test_post_simple_usage(self):
    file = open(path.join(settings.TEST_DATA_DIR, "test.odt"))
    response = self.client.post("/", {"name": "test.odt", 'attachment': file})
    self.assertEquals(200, response.status_code)
