import sys, getopt, math, re, json
from pprint import pprint
import requests


def main(argv):
    usage = 'get_issue_comments.py -i <input file>'
    input_file = None
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.error:
        print usage
        sys.exit(2)

    for opt, arg, in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg


    # open file
    if input_file is None:
        print "No input file supplied."
        print usage
        sys.exit()

    #we'll store who is asking questions, and who is answering questions.
    user_questions = {}
    user_answers = {}

    with open(input_file) as f:
        data = json.load(f)

    ## This isnt necessary if we only query question issues
    # for i in data:
    #     store = False
    #     for label in i['labels']:
    #         if label['name'] == 'question':
    #             store = True
    #     if store:
    #         pprint(i)
    for i in data:
         asker = i['user']['login']
         count = 0
         if asker in user_questions:
             count = user_questions[asker]

         count = count + 1
         user_questions[asker]= count

         issue_number = i['number']

         #now lookup who answered this issue
         url = 'https://api.github.com/repos/tripal/tripal/issues/' + str(issue_number) + '/comments'
         response = requests.get(url)
         rjson = response.json()

         for comment in rjson:
             answerer = comment['user']['login']
             if answerer != asker:
                 answer_count = 0
                 if answerer in user_answers:
                     answer_count = user_answers[answerer]
                 answer_count = answer_count + 1
                 user_answers[answerer] = answer_count

    pprint(user_answers)




if __name__ == "__main__":
    main(sys.argv[1:])

    """"

    """
