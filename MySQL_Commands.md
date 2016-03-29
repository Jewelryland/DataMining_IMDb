##Some common commands to navigate through the MySQL database:

```
sudo mysql -u root -p
```
```
mysql>use imdb;
```
```
mysql> show tables;
```

```
mysql> desc table_name;
```

For getting a formatted output-

```
mysql> Select * from table_name \G
```

For outputing the query results intoa file

```
select * from aka_name INTO OUTFILE '/home/saish/Documents/DataMining/Project/aka_name.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
```

