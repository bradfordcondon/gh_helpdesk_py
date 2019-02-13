import configparser
import sys,os, getopt, math, re, json
from pprint import pprint
import requests

class GitHub:


    config = configparser.ConfigParser()
    config.read('config.env')

    base_url = "https://api.github.com/repos/tripal/tripal/issues/"
    username = config.get('GITHUB', 'USERNAME')
    password = config.get('GITHUB', 'PASSWORD')

    def __init__(self):
        return

    def info(self):
        return  {self.base_url, self.username, self.password}


    def fetchIssues():

        url = self.base_url
        response = requests.get(url, auth=(self.username, self.password))
        rjson = response.json()

        return rjson



    defl fetchLabels():
       url = self.base_url + 'labels'
       response = requests.get(url, auth=(self.username, self.password))
       rjson = response.json()

       #import return keys are id: and name:
       #see: https://developer.github.com/v3/issues/labels/#list-all-labels-for-this-repository
       return rjson


    def tallyIssueCommentsByUser(self, issue_number):

        #fetch comments for issue
        url = self.base_url + str(issue_number) + '/comments'
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
