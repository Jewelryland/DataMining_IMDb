#This contains the code used for fetching data via IMDbPy and IMDb-pie module

For installing IMDBPy
```pip install imdbpy```


For installing ImdbPie

```pip install imdbpie```


For fetching the top 250 movie data

```
from from imdbpie import Imdb

imdb = Imdb()

imdb = Imdb(cache=True)

imdb.top_250() 
```

