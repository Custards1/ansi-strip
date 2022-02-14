# ansi-sweep
This project is a microservice intended to strip those pesky ANSI escape sequences generated from various terminals. These escape sequences are sometimes variable in length,content, and are terminal dependent. Many terminal tools, such as 'script', will display content using these codes meant for your terminal alone; This
can be annoying when attempting to use the same output in different envirenments.

# Running
You must have docker to run this project.
In a terminal, open up this repository and type:
```
$ make run
```
# Using
To use the service, simply use the endpoint xterm:
```
POST /xterm:
    Post body:
        {
            kind = 'all'|'color'|'moves'|'basic'
            data = xterm-text
        }
```
As an example; When the server is running try running:
```
$ echo "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m\u001b[1;31mbold red text\u001b[0m"
$ curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"kind":"all","data":"\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m\u001b[1;31mbold red text\u001b[0m"}' \
  http://localhost:8000/xterm
```
# Roadmap
- [x] Strip color sequences from terminal text sequence
- [x] Strip cursor sequences from terminal text sequence
- [x] Strip multibyte sequences from terminal text sequence
- [ ] Strip text mode sequences from terminal text sequence
- [ ] Support for other terminals besides xterm
- [ ] Give the frontpage xterm.js support

# Notes
This project is only intened to strip ansi terminal sequences only!