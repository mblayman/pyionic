# -*- coding: utf-8 -*-

from .context import pyionic

import unittest
from pprint import pprint


class TestCore(unittest.TestCase):
    """Basic test cases for core usage."""

    def test_get_self(self):
        test = pyionic.core.Users()
        data = test.get_self()['data']
        assert isinstance(data, dict)
        assert data['id']
        assert data['teams']

    def test_get_team(self):
        users = pyionic.core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[4]
        teams = pyionic.core.Teams()
        data = teams.get_team(team_id)['data']
        assert isinstance(data, dict)
        assert data['id']

    def test_get_projects(self):
        users = pyionic.core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[4]
        projects = pyionic.core.Projects()
        data = projects.get_projects(team_id)
        assert isinstance(data, dict)
        assert data['data']

    def test_get_project(self):
        users = pyionic.core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[4]
        projects = pyionic.core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        data = projects.get_project(team_id, project_id)
        assert isinstance(data, dict)
        assert data['data']

    def test_get_analysis_summery(self):
        users = pyionic.core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[4]
        projects = pyionic.core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        analysis = pyionic.core.Analysis()
        data = analysis.get_analysis_summery(team_id, project_id)
        assert isinstance(data, dict)
        assert data['data']

    def test_get_analysis(self):
        users = pyionic.core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[4]
        projects = pyionic.core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        analysis = pyionic.core.Analysis()
        analysis_id = analysis.get_analysis_summery(team_id, project_id)['data']['id']
        data = analysis.get_analysis(team_id, project_id, analysis_id)
        assert isinstance(data, dict)
        assert data['data']

    def test_analyze_project(self):
        users = pyionic.core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[4]
        projects = pyionic.core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        scanner = pyionic.core.Scanner()
        scan = scanner.analyze_project(team_id, project_id)
        assert isinstance(scan, dict)
        assert scan['data']['status'] == 'accepted'

    def test_get_vulnerabilities(self):
        vulnerability = pyionic.core.Vulnerability()
        vulnerabilities = vulnerability.get_vulnerabilities('python', '3.4')
        assert isinstance(vulnerabilities, dict)
        assert vulnerabilities['data']

    def test_get_vulnerability(self):
        vulnerability = pyionic.core.Vulnerability()
        vulnerability_data = vulnerability.get_vulnerability('CVE-2017-5753')
        assert isinstance(vulnerability_data, dict)
        assert vulnerability_data['data']

if __name__ == '__main__':
    unittest.main()
