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

```
select name,count(id) from name group by name having count(id)>1;
```
Example of joining mulitiple tables together with similar IDs:
SELECT Products.Title, Product_Lines.pl_Title, Manufacturers.man_Title
 FROM Products INNER JOIN Product_Lines ON Products.pl_ID = Product_Lines.pl_ID INNER JOIN Manufacturers ON Product_Lines.man_ID = Manufacturers.man_ID

```
