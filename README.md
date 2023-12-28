# BSY-bonus

1. Your task is to write the bot code and the controller code. The bot will be the infected computer, and the controller is what you use to control the bots.

2. Both parts should use www.dropbox.com to communicate. You can register a free account and create a new application that uses the Python SDK (dropbox library) to upload and download files, etc.

3. The goal is to run some of your bots as 'infected' computers in the dropbox channel, and you also connect to this channel with your controller to control them.

4. The communication between the bots and the controller should not be easily detected as 'bots' in the channel, therefore all communication should look like normal English markdown or text (text, images and emojis are accepted). You should use some steganography technique to hide your messages as English.

5. The controller should check if the bots are alive periodically.

6. The controller should give orders to the bot and the bot should answer the output of the orders
The minimum orders are the following commands:
	- w (list of users currently logged in)
	- ls <PATH> (list content of specified directory)
	- id (if of current user)
	- Copy a file from the bot to the controller. The file name is specified
	- Execute a binary inside the bot given the name of the binary. Example: ‘/usr/bin/ps’

7. Publish the whole code in github and put the link as a flag for this stage. Make sure you do not publish your API keys!!!

8. Provide sufficient documentation on how to setup and use the client and the server so that we can test it.
