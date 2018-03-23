# URL Query match

The time complexity is O(M*N) for M is the length of key and n is the number of keys.
The search time is O(M) for M is the length of key.
Data structure used is Trie which is a kind of search tree used in this case to store the data of backload_urls and for efficient insert and search operations.

## INPUT

```
python3 url_match.py
backload_urls:http://www.example.com,https://www.hello.com,http://www.siliconvalley.com
No. of queries:3
Query 1 http://www.example.com
Query 2 http://www.pinterest.com
Query 3 http://www.siliconworld.com
FULL URL FOUND
NO URL FOUND
PARTIAL URL FOUND
```

## EXPLANATION

We are creating backload_urls which around million URLs and we have to check whether there is a perfect match or partial match of the urls inputted. This solution helps in providing an optimal solution to the problem.

