# Python Workshop
## Overview
* Development Environment
* Web technologies (HTTP, HTML, JSON)
* Python 001
* Scraper example
* REST API example

## Setting up your development Environment
### Python and Pip
1. Install python on [windows](https://www.youtube.com/watch?v=S8oYT5am8j4) or [mac](https://www.youtube.com/watch?v=8BiYGIDCvvA%3Cbr%3E%3Cbr%3EPlease)
2. After the video, verify which versions you have with:
    * `python --version`
    * `python2 --version`
    * `python3 --version`  
If that did not work on windows [you might need to add python to your Path](https://geek-university.com/python/add-python-to-the-windows-path/)
3. Confirm that pip came with it, which it should have. Try each of these 3 commands to see which version(s) you have
  * `pip --version`
  * `pip2 --version`
  * `pip3 --version`  
If you have none of them, follow the directions: https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py


(Alternative method would be with homebrew but I'll leave that for those who want to figure it out)
### Text Editor
I recommend a lightweight editor like Atom or SublimeText. I hear good things about VSCode but am not sure if it requires configuration or not. I will be using Atom.
* Atom - https://atom.io/
* SublimeText - https://www.sublimetext.com/3
* VS Code - https://code.visualstudio.com/Download

### Git
Typing `git --version` in a mac terminal should prompt you to download. If not or if on windows, then go to https://git-scm.com/download/

After it is installed, if you open up a terminal window on mac and type `git clone https://github.com/jasonek/csun_workshop.git` then you will download this repository.

For windows you probably have to use Git Bash to do the same. Git Bash should come with the Windows installer.
Or for either you could click the green "Clone or Download" button.

### Install some Python packages
This will save time on Saturday
`pip3 install beautifulsoup4 twilio pytz virtualenv`

## Web Technologies
* HTTP
  * [Go here for a great introduction. Do not worry about memorizing details but instead let the information help you to build a mental model of how it works](https://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)
  * Protocol (agreed-upon way of sending messages back and forth)
  * Traditional "world wide web" internet, but not the only protocol used over the internet to communicate
  * Web server is a machine that lives at a certain IP address/domain and responds to requests. To convey to the requester whether the server was successful or not, it will also send back an HTTP status code. 200 means good. You've probably seen 404 Not Found and 500 internal server error in a web browser
  * Lets get a sense of what HTTP message look like by sending some manual ones.
      * `curl -v -XGET 'https://pip.pypa.io/en/stable/'`
  * In the headers you can see the status code. There is other metadata about the server and stuff used by the browser, such as for caching
* HTML
  * From DOCTYPE and below you can see HTML
  * its pretty human readable, but everything is surrounded by the <> brackets
  * but this blob of data is exactly what web browsers receive, because its what web servers send, so they have no choice.
  * go to the same web page in a browser, right-click and inspect.

### Python 001
[Python slides](https://docs.google.com/presentation/d/1xzHzm9oo64qkIwwFD6gRfDR6gRwqOnEAdBdZemFaU_E/edit#slide=id.p1)

### Scraper
[Coding Walk-through](https://docs.google.com/presentation/d/1iSBYnLn_N1LbVIA_bwzgxYNtbXIvbuTd2kAovmg4hGM/edit#slide=id.p)

### REST API Example
[REST API](https://docs.google.com/presentation/d/1JJW-ZUsmIVMtsZUBdeUlsVgBjG3J6F1SmQ95fnelzv4/edit#slide=id.g547b16ffbb_0_57)
