import sys, getopt, math, re, json
from pprint import pprint

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

    with open(input_file) as f:
        data = json.load(f)

    pprint(data)


if __name__ == "__main__":
    main(sys.argv[1:])

    """"

    """
