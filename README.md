# W4Bot
A Discord bot, written in Python, build and used by the W4 CTF team.

## Commands

| Command         | Describtion                    | Example                             |
|-----------------|--------------------------------|-------------------------------------|
| !ping           | Gives a pong response          | !ping                               |
| !showhelp       | Shows the commands available   | !showhelp                           |
| !info @[user]   | Shows information about a user | !info @Silverbaq                    |
| !b64encode text | Base64 encodes a string        | !b64encode this is a string         |
| !b64decode text | Base64 decodes a string        | !b64decode dGhpcyBpcyBhIHN0cmluZw== |
| !chat text      | Chat with the bot              | !chat Hello, how are you?           |


## Setup
Make an .env file in the root directory. It should contain the following:

* TOKEN = The discord bot api token (as a string)
* TWITCH_CLIENT_ID = The twitch client id (As a string)
* CHANNEL_ID = The discord channel id, where streams going online should be promoted (as an int)