# Python Workshop
## Overview
* Development Environment
* Web technologies (HTTP, HTML, JSON)
* Python 001
* Scraper example
* REST API example

## Web Technologies
* HTTP
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

* Python
  * Explain importing
