# -*- coding: utf-8 -*-

from .context import core

import unittest
from pprint import pprint


class TestCore(unittest.TestCase):
    """Basic test cases for core usage."""

    def test_get_self(self):
        test = core.Users()
        data = test.get_self()['data']
        assert isinstance(data, dict)
        assert data['id']
        assert data['teams']

    def test_get_team(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        teams = core.Teams()
        data = teams.get_team(team_id)['data']
        assert isinstance(data, dict)
        assert data['id']

    def test_get_projects(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        projects = core.Projects()
        data = projects.get_projects(team_id)
        assert isinstance(data, dict)
        assert data['data']

    def test_get_project(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        projects = core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        data = projects.get_project(team_id, project_id)
        assert isinstance(data, dict)
        assert data['data']

    # Fails until delivery is setup for pyionic team
    # def test_get_analysis_summery(self):
    #     users = pyionic.core.Users()
    #     team_id = list(users.get_self()['data']['teams'].keys())[0]
    #     print(team_id)
    #     projects = pyionic.core.Projects()
    #     project_id = projects.get_projects(team_id)['data'][0]['id']
    #     print(project_id)
    #     analysis = pyionic.core.Analysis()
    #     data = analysis.get_analysis_summery(team_id, project_id)
    #     print(data)
    #     assert isinstance(data, dict)
    #     assert data['data']

    def test_get_analysis(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        projects = core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        analysis = core.Analysis()
        analysis_id = analysis.get_analysis_summery(team_id, project_id)['data']['id']
        data = analysis.get_analysis(team_id, project_id, analysis_id)
        assert isinstance(data, dict)
        assert data['data']

    def test_analyze_project(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        projects = core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        scanner = core.Scanner()
        scan = scanner.analyze_project(team_id, project_id)
        assert isinstance(scan, dict)
        assert scan['data']['status'] == 'accepted'

    def test_get_analysis_status(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        projects = core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        analysis = core.Analysis()
        analysis_id = analysis.get_analysis_summery(team_id, project_id)['data']['id']
        scanner = core.Scanner()
        data = scanner.get_analysis_status(team_id, project_id, analysis_id)
        assert isinstance(data, dict)
        assert data

    def test_get_vulnerabilities(self):
        vulnerability = core.Vulnerability()
        vulnerabilities = vulnerability.get_vulnerabilities('python', '3.4')
        assert isinstance(vulnerabilities, dict)
        assert vulnerabilities['data']

    def test_get_vulnerability(self):
        vulnerability = core.Vulnerability()
        vulnerability_data = vulnerability.get_vulnerability('CVE-2017-5753')
        assert isinstance(vulnerability_data, dict)
        assert vulnerability_data['data']

    def test_get_products(self):
        vulnerability = core.Vulnerability()
        vulnerability_data = vulnerability.get_products('cpe:/a:ruby-lang:ruby:1.8.7')
        assert isinstance(vulnerability_data, dict)
        assert vulnerability_data['data']

    def test_get_rulesets(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        rulesets = core.Rulesets()
        rulesets_data = rulesets.get_rulesets(team_id)
        assert isinstance(rulesets_data, dict)
        assert rulesets_data['data']

    def test_get_ruleset(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        rulesets = core.Rulesets()
        ruleset_id = rulesets.get_rulesets(team_id)['data'][0]['id']
        ruleset_data = rulesets.get_ruleset(team_id, ruleset_id)
        assert isinstance(ruleset_data, dict)
        assert ruleset_data['data']

    def test_get_applied_ruleset_for_project(self):
        users = core.Users()
        team_id = list(users.get_self()['data']['teams'].keys())[0]
        projects = core.Projects()
        project_id = projects.get_projects(team_id)['data'][0]['id']
        ruleset = core.Rulesets()
        data = ruleset.get_applied_ruleset_for_project(team_id, project_id)
        assert isinstance(data, dict)
        assert data


if __name__ == '__main__':
    unittest.main()
