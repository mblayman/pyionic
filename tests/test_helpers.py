# -*- coding: utf-8 -*-

from .context import helpers

import os
import unittest
from pprint import pprint


class TestHelpers(unittest.TestCase):
    """Basic test cases for helpers usage."""

    def test_get_envvars(self):
        with self.assertRaises(SystemExit) as cm:
            del os.environ['IONCHANNEL_SECRET_KEY']
            helpers.get_envvars()
            self.assertEqual(cm.exception.code, 1)

    def test_get_api_endpoint(self):
        os.environ['IONCHANNEL_ENDPOINT'] = 'https://api.ionchannel.io'
        
if __name__ == '__main__':
    unittest.main()
