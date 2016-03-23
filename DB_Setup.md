#Importing IMDB dataset into MySQL database

Transferring IMDB dataset plain text files to MySQL server is an essential step before analyzing data mining tasks. 
I went through installing and running MySQL server on my machine. 
I am using OS X 10.11 64bit as the OS platform. 
In order to this long process to run, it requires the memory to have at least 4 GB of free space as a partition.
We will also be using IMDbPy, a python based package. Of course, this library needs us to have Python installed on our machine as well as its development tools along with SQLObject. After installing required software, we will have to download all files from IMDb site: ftp://ftp.fu-berlin.de/pub/misc/movies/database/. 
Then, we can go ahead and create database and begin importing process. 

#steps for database installation:
link - http://imdbpy.sourceforge.net/docs/README.sqldb.txt
Select a mirror of the "The Plain Text Data Files" from
the http://www.imdb.com/interfaces/ page and download
every file in the main directory (beware that the "diffs"
subdirectory contains _a lot_ of files you _don't_ need,
so don't start mirroring everything!).

Starting from release 2.4, you can just download the files you need,
instead of every single file; the files not downloaded will be skipped.
This feature is still quite untested, so please report any bug.

Create a database named "imdb" (or whatever you like),
using the tool provided by your database; as an example, for MySQL
you will use the 'mysqladmin' command:
  # mysqladmin -p create imdb
For PostgreSQL, you have to use the "createdb" command:
  # createdb -W imdb

To create the tables and to populate the database, you must run
the imdbpy2sql.py script:
  # imdbpy2sql.py -d /dir/with/plainTextDataFiles/ -u 'URI'

Where the 'URI' argument is a string representing the connection
to your database, with the schema:
  scheme://[user[:password]@]host[:port]/database[?parameters]

Where 'scheme' is one in "sqlite", "mysql", "postgres", "firebird",
"interbase", "maxdb", "sapdb", "mssql", "sybase", "ibm_db_sa".

Some examples:
    mysql://user:password@host/database
    postgres://user:password@host/database
    mysql://host/database?debug=1
    postgres:///full/path/to/socket/database
    postgres://host:5432/database
    sqlite:///full/path/to/database
    sqlite:/C|/full/path/to/database
    sqlite:/:memory:

For other information you can read the SQLObject/SQLAlchemy documentation.
You can force the use of SQLObject or SQLAlchemy with the '-o' command
line option (i.e.: "-o sqlobject" or "-o sqlalchemy" or a list of comma
separated values to specify an order of preference).



# Steps for installing IMDbPy and SQLObject :
1. Install required packages:
sudo easy_install pip

`sudo python setup.py install`

`sudo easy_install MySQL-python`


2. Download only .gz files from IMDb in the current directory:
`wget -r --accept="*.gz" --no-directories --no-host-directories --level 1 ftp://ftp.fu-berlin.de/pub/misc/movies/database/`

3. Begin the import process: 

`imdbpy2sql.py -d /Users/Bader/Documents/Spring2016/Data-Mining/Project/ -u 'mysql://imdb:imdb@localhost/imdb'`

We are aware that –d is the directory where .gz files are located and –u is the database connection string for the MySQL database. A screenshot of the output is given below:

![Screenshot](Setup.png)
