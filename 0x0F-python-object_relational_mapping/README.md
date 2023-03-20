# Python :page_with_curl: 0x0F-python-object_relational_mapping

## About this project:
In this project I learnt and practiced:
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to `SELECT` rows in a MySQL table from a Python script
How to `INSERT` rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table

## Task files description;
* [0-select_states.py](./0-select_states.py): Python script that uses MySQLdb
  to list all states in the database `hbtn_0e_0_usa`.
  * Usage: `./0-select_states.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `states.id`.

* [1-filter_states.py](./1-filter_states.py): Python script that uses MySQLdb
  to list all states with names starting with `N` in the database `hbtn_0e_0_usa`.
  * Usage: `./1-filter_states.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `states.id`.


* [2-my_filter_states.py](./2-my_filter_states.py): Python script that uses
  MySQLdb to display all values matching a given name in the `states` table of
  the database `hbtn_0e_0_usa`.
  * Usage: `./2-my_filter_states.py <mysql username> <mysql password>
  <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.
  * Uses string formatting to construct the SQL query.

* [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): Python script
  that uses MySQLdb to display all values matching a given name in the `states`
  table of the database `hbtn_0e_0_usa`.
  * Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password>
  <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.
  * Safe from SQL injections.

* [4-cities_by_state.py](./4-cities_by_state.py): Python script that uses
  MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
  * Usage: `./4-cities_by_state.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `cities.id`.


* [5-filter_cities.py](./5-filter_cities.py): Python script that uses MySQLdb
  to list all cities of a given state in the database `hbtn_0e_4_usa`.
  * Usage: `./5-filter_cities.py <mysql username> <mysql password>
  <database name>`.
  * Results are sorted by ascending `cities.id`.

* [model_state.py](./model_state.py): Python module defining a class `State`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.

* [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): Python script
  that uses SQLAlchemy to list all `State` objects from the database
  `hbtn_0e_6_usa`.
  * Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password>
  <database name>`.
  * Results are sorted by ascending `states.id`.

* [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): Python script
  that uses SQLAlchemy to print the first `State` object from the database
  `hbtn_0e_6_usa`, ordered by `states.id`.
  * Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password>
  <database name>`.
  * If the `states` table is empty, prints `Nothing`.


* [9-model_state_filter_a.py](./9-model_state_filter_a.py): Python script
  that uses SQLAlchemy to list all `State` objects that contain the letter `a`
  in the database `hbtn_0e_6_usa`.
  * Usage: `./9-model_state_filter_a.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `states.id`.

* [10-model_state_my_get.py](./10-model_state_my_get.py): Python script that
  uses SQLAlchemy to print the `id` of the `State` object with name matching that
  passed as argument in the database `hbtn_0e_6_usa`.
  * Usage: `./10-model_state_my_get.py <mysql username> <mysql password>
  <database name> <state searched name>`.
  * Displays the `id` of the matched `State`.
  * If no match is found, prints `Not found`.

