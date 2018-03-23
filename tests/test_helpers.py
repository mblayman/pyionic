# -*- coding: utf-8 -*-

from .context import helpers

import os
import unittest


class TestHelpers(unittest.TestCase):
    """Basic test cases for helpers usage."""

    # def test_get_envvars(self):
    #     with self.assertRaises(SystemExit) as cm:
    #         envvar_stageing = os.environ['IONCHANNEL_SECRET_KEY']
    #         del os.environ['IONCHANNEL_SECRET_KEY']
    #         helpers.get_envvars()
    #         self.assertEqual(cm.exception.code, 1)

    def test_get_api_endpoint(self):
        os.environ['IONCHANNEL_ENDPOINT_URL'] = 'https://api.ionchannel.io'
        helpers.get_api_endpoint()
        assert(helpers.get_api_endpoint() == 'https://api.ionchannel.io')


if __name__ == '__main__':
    unittest.main()
