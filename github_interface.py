import configparser
import sys,os, getopt, math, re, json
from pprint import pprint
import requests

from github import Github



class IssueFetcher:


    config = configparser.ConfigParser()
    config.read('config.env')
    username = config.get('GITHUB', 'USERNAME')
    password = config.get('GITHUB', 'PASSWORD')
    g = Github(username, password)
    repo = g.get_repo("tripal/tripal")
    total_user_count = {}

    def __init__(self):
        return

    def info(self):
        return  {self.base_url, self.username, self.password}


    def fetchIssues(self):
        r = self.repo
        issues_total = {}
        for issue in r.get_issues(state='all'):
            user_count = {}
            for comment in issue.get_comments():
                user = comment.user.login
                self.addTally(self.total_user_count, user)
                self.addTally(user_count, user)
            issues_total[issue.id] = user_count
        return issues_total


    def addTally(self, dict, key):
        if key in dict:
             dict[key] += 1
        else:
             dict[key] = 1
        return dict




        return issues
