# -*- coding: utf-8 -*-

from .context import helpers

import os
import unittest


class TestHelpers(unittest.TestCase):
    """Basic test cases for helpers usage."""

    def test_get_token_missing(self):
        """Exit when the IONCHANNEL_SECRET_KEY is not set."""
        token = os.environ.get('IONCHANNEL_SECRET_KEY')
        token = '' if token is None else token
        try:
            del os.environ['IONCHANNEL_SECRET_KEY']
        except KeyError:
            # The variable may already be unset. If so, ignore the exception.
            pass

        with self.assertRaises(SystemExit):
            helpers.get_token()

        # Restore the secret key for other tests.
        os.environ['IONCHANNEL_SECRET_KEY'] = token

    def test_get_api_endpoint(self):
        os.environ['IONCHANNEL_ENDPOINT_URL'] = 'https://api.ionchannel.io'
        helpers.get_api_endpoint()
        assert(helpers.get_api_endpoint() == 'https://api.ionchannel.io')


if __name__ == '__main__':
    unittest.main()
