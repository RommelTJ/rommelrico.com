from django.test import TestCase
from django.core.urlresolvers import reverse

class LaunchPadTests(TestCase):
    def test_launchpad_loaded(self):
        """
        Tests that the page returns ok.
        """
        response = self.client.get(reverse('launchpad:index'))
        self.assertEqual(response.status_code, 200)
