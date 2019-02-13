import configparser

class GitHub:


    config = configparser.ConfigParser()
    config.read('config.env')

    base_url = "https://api.github.com/repos/tripal/tripal/issues/"
    username = config.get('GITHUB', 'USERNAME')
    password = config.get('GITHUB', 'PASSWORD')

    def f(self):
        return 'hello world'



    def tallyIssueCommentsByUser(issue_number):

        #fetch comments for issue
        url = base_url + str(issue_number) + '/comments'
        response = requests.get(url, auth=(username, password))
        if (response.status_code != 200):
             print("Error fetching issue! Error code: " + str(response.status_code))
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
