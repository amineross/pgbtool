# PostgreSQL Backup Tool

CLI Backup tool for PostgreSQL Databases either to S3 Buckets or Locally.

# Installation

1) Clone the following link :
~~~
$ git clone https://github.com/amineross/pgbtool.git
~~~
2) Run setup.py
~~~
$ python3 setup.py
~~~

# Usage

Example usage of pgbtool: 

1) Using an S3 Bucket :
~~~
$ pgbtool posgstres://name@example.com:5432/db_name --driver s3 bucket_name
~~~
1) Using a local path :
~~~
$ pgbtool posgstres://name@example.com:5432/db_name --driver local path/to/file
~~~
## Contribute to the project
1) Ensure **pip** and **pipenv** are installed.
2) Clone the repository.
3) **cd** into the repository
4) Run **pipenv shell**
5) Install dependencies with **pipenv install**
