#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

from Connection import Connection
import sys


def main():
    # get args
    argc = len(sys.argv)
    argv = sys.argv

    # check number of arguments
    if argc != 3:
        exit("python3 controller.py <API KEY> <INTERVAL>")

    # programmer friendly naming
    api_key = argv[1]
    interval = int(argv[2])
    shopping_list = "/shopping_list.txt"

    # create connection
    conn = Connection(api_key)

    # check connection
    if not conn.is_connected():
        exit("Could not to connect to Dropbox!")

    # counters
    last_minus_counter = 0
    last_positive_counter = 0

    while True:

        if not conn.exist_file(shopping_list):
            conn.



if __name__ == "__main__":
    main()