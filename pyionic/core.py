# -*- coding: utf-8 -*-
from . import helpers
import requests


class Teams:
    def __init__(self):
        self.token = helpers.get_envvars()
        self.endpoint = helpers.get_api_endpoint()

    def get_team(self, team_id):
        """Gets a teams info"""
        url = self.endpoint + '/v1/teams/getTeam?someid=%s' % team_id
        res = requests.get(url, headers={"authorization": self.token})
        return res.json()


class Users:
    def __init__(self):
        self.token = helpers.get_envvars()
        self.endpoint = helpers.get_api_endpoint()

    def get_self(self):
        url = self.endpoint + '/v1/users/getSelf'
        res = requests.get(url, headers={"authorization": self.token})
        return res.json()


class Projects:
    def __init__(self):
        self.token = helpers.get_envvars()
        self.endpoint = helpers.get_api_endpoint()

    def get_projects(self, team_id):
        url = self.endpoint + '/v1/project/getProjects?team_id=%s' % team_id
        res = requests.get(url, headers={"authorization": self.token})
        return res.json()

    def get_project(self, team_id, project_id):
        url = self.endpoint + '/v1/project/getProject?team_id=%s&id=%s' % (team_id, project_id)
        res = requests.get(url, headers={"authorization": self.token})
        return res.json()


class Analysis:
    def __init__(self):
        self.token = helpers.get_envvars()
        self.endpoint = helpers.get_api_endpoint()

    def get_analysis_summery(self, team_id, project_id):
        url = self.endpoint + '/v1/animal/getLatestAnalysisSummary?team_id=%s&project_id=%s' % (team_id, project_id)
        res = requests.get(url, headers={"authorization": self.token})
        return res.json()

    def get_analysis(self, team_id, project_id, analysis_id):
        url = self.endpoint + '/v1/animal/getAnalysis?team_id=%s&project_id=%s&id=%s' % (team_id, project_id, analysis_id)
        res = requests.get(url, headers={"authorization": self.token})
        return res.json()


class Scanner:
    def __init__(self):
        self.token = helpers.get_envvars()
        self.endpoint = helpers.get_api_endpoint()

    def analyze_project(self, team_id, project_id):
        url = self.endpoint + '/v1/scanner/analyzeProject?team_id=%s&project_id=%s' % (team_id, project_id)
        res = requests.post(url, headers={"authorization": self.token})
        return res.json()

class Vulnerability:
    def __init__(self):
        self.token = helpers.get_envvars()
        self.endpoint = helpers.get_api_endpoint()

    def get_vulnerabilities(self, product, version):
        url = self.endpoint + '/v1/vulnerability/getVulnerabilities?product=%s&version=%s' % (product, version)
        res = requests.get(url)
        return res.json()
