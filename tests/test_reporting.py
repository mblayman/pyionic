# -*- coding: utf-8 -*-

from .context import reporting
from .context import core

import unittest
from pprint import pprint


class TestReporting(unittest.TestCase):
    """Basic test cases for reporting usage."""

    def test_get_projects_from_team(self):
        user = core.Users()
        team_id = list(user.get_self()['data']['teams'].keys())[0]
        report_projects = reporting.Projects()
        data_list = report_projects.get_projects_ids_from_team(team_id)
        assert isinstance(data_list, list)

    def test_get_projects_ids_and_names_from_team(self):
        user = core.Users()
        team_id = list(user.get_self()['data']['teams'].keys())[0]
        report_projects = reporting.Projects()
        data_list = report_projects.get_projects_ids_and_names_from_team(team_id)
        assert isinstance(data_list, list)
        for data in data_list:
            assert isinstance(data, tuple)

    def test_get_highest_cve_for_product_version(self):
        vulnerability = reporting.Vulnerability()
        assert isinstance(vulnerability.get_highest_cve_for_product_version('python', '2.7'), str)

    def test_get_sorted_list_cves_for_project_version(self):
        vulnerability = reporting.Vulnerability()
        test_data = vulnerability.get_sorted_list_cves_for_project_version('python', '2.7')
        assert isinstance(test_data, list)
        for data in test_data:
            assert isinstance(data, tuple)

if __name__ == '__main__':
    unittest.main()
