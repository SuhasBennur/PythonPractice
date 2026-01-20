import requests
import asyncio
import http.client
import urllib.request

url1 = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url1)

if response.status_code == 200:
    data1 = response.json()  # Automatically parse JSON
    print(data1)



url2 = "https://jsonplaceholder.typicode.com/posts/1"
response = urllib.request.urlopen(url2)
data2 = response.read().decode("utf-8")

print(data2)



conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1")
response = conn.getresponse()

print(response.status, response.reason)
print(response.read().decode())



async def fetch():
    url3 = "https://jsonplaceholder.typicode.com/posts/1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url3) as response:
            data3 = await response.json()
            print(data3)

asyncio.run(fetch())


