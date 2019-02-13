# import the Flask class from the flask module
from flask import Flask, render_template

from github_interface import GitHub

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('home.html')  # render a template

@app.route('/summary')
def summary(data=None):
    #provides a summary of repo activity

    data = get_issue_comments.get_issue_information(100)
    #run the get issue script

    return render_template('summary.html', data=data)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
