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

    def __init__(self):
        return

    def info(self):
        return  {self.base_url, self.username, self.password}


    def fetchIssues(self):

        issues = []
        r = self.repo
        issues = r.get_issues()
        return issues



    def fetchLabels(self):
       repo = self.repo
       labels = repo.get_labels()
        for label in labels:



    def tallyIssueCommentsByUser(self, issue_number):

        #fetch comments for issue
        url = self.base_url + '/' + str(issue_number) + '/comments'
        response = requests.get(url, auth=(self.username, self.password))
        if (response.status_code != 200):
             print("Error fetching issue! Error code: " + str(response.status_code))
             return False
        rjson = response.json()
        user_answers = {}

        for comment in rjson:
              answerer = comment['user']['login']
              answer_count = 0
              if answerer in user_answers:
                      answer_count = user_answers[answerer]
              answer_count = answer_count + 1
              user_answers[answerer] = answer_count

        return user_answers
