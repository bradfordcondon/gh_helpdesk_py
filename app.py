# import the Flask class from the flask module
from flask import Flask, render_template

import pprint

from github_interface import GitHub

# create the application object
app = Flask(__name__)

gh = GitHub()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/debug')
def debug():

    str = pprint.pformat(gh.tallyIssueCommentsByUser(100))
    return (str)


@app.route('/labels/<label>')
def summarize_label(label):
    # get info for this label


@app.route('/summary')
def summary(data=None):
    #provides a summary of repo activity

    data = get_issue_comments.get_issue_information(100)
    #run the get issue script

    return render_template('summary.html', data=data)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
