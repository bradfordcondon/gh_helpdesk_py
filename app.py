# import the Flask class from the flask module
from flask import Flask, render_template

import pprint, json

from github_interface import IssueFetcher

# create the application object
app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=4)
gh = IssueFetcher()
issues = gh.fetchIssues()


@app.route('/')
def home():
    total_issues = len(issues)
    return render_template('home.html', total = total_issues)

@app.route('/debug')
def debug():

    return "yay"


@app.route('/labels/<label>')
def summarize_label(label):
    #fetch issues
    return

@app.route('/summary')
def summary(data=None):
    #provides a summary of repo activity

    data = get_issue_comments.get_issue_information(100)
    #run the get issue script

    return render_template('summary.html', data=data)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
