url1 = "https://www.example.com/page1.html"
url2 = "https://www.example.com/page2.html"
url3 = "https://www.example.com/page3.html"
url4 = "https://www.example.com/page4.html"

MAX_CACHE_SIZE = 2

cache = {}

cache[1] = url1
cache[2] = url2
cache[3] = url3
cache[4] = url4

print(cache)

l = len(cache.items())
while l > 2:
    l = len(cache.items())

print(cache)
