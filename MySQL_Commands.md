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

For outputing the query results into a file

```
select * from aka_name INTO OUTFILE '/home/saish/Documents/DataMining/Project/aka_name.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
```

```
select name,count(id) from name group by name having count(id)>1;
```
Example of joining mulitiple tables together with similar IDs:
```
SELECT distinct n.gender, n.name, r.role from name n INNER JOIN cast_info c ON n.id = c.person_id INNER JOIN role_type r ON r.id = c.role_id where n.gender is not null; 
```
