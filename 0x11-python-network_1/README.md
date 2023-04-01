# Python Network :page_with_curl: 0x11-python-network_1

## About this project :black_nib:

In this project I learnt and practiced about:

* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` #requestsiswaysimplerthanurllib
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service
* How to interact with an API using `requests` package

## Task files description :card_index:

* [0-hbtn_status.py](./0-hbtn_status.py): Python script that fetches
  `https://alx-intranet.hbtn.io/status`.
  * Uses `urllib`.

* [1-hbtn_header.py](./1-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./1-hbtn_header.py <URL>`
	* Uses `urllib`.

* [2-post_email.py](./2-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./2-post_email.py <URL> <email>`.
	* Uses `urllib`.

* [3-error_code.py](./3-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `urllib`.

* [4-hbtn_status.py](./4-hbtn_status.py): Python script that fetches
  `https://alx-intranet.hbtn.io/status`.
  * Uses `requests`.


* [5-hbtn_header.py](./5-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./5-hbtn_header.py <URL>`
	* Uses `requests`.

* [6-post_email.py](./6-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./6-post_email.py <URL> <email>`.
	* Uses `requests`.


* [7-error_code.py](./7-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `requests`.


* [8-json_api.py](./8-json_api.py): Python script that sends a `POST` request
  to `http://0.0.0.0:5000/search_user` with a letter passed as parameter.
  * Usage: `./8-json_api.py <letter>`
	* The letter is sent as the value of the variable `q`.
	* If no letter is given, sets `q=""`.
	* If the response body is properly formatted and non-empty, displays it as
  `[<id>] <name>`.
  * Uses `requests`.

* [10-my_github.py](./10-my_github.py): Python script that takes GitHub
  credentials (username and password) and uses the Github API to display the
  corresponding ID.
  * Usage: `./10-my_github.py <username> <password>`
	* Uses `requests`.

* [100-github_commits.py](./100-github_commits.py): Python script that lists
  the 10 most recent comments of a given GitHub repository using the GitHub API.
  * Usage: `./100-github_commits.py <repository name> <owner name>`
	* Uses `requests`.
