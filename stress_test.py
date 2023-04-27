import requests
import time

start_time = time.time()

for i in range(20000):
    response = requests.get('http://localhost:38525/users')
    print(i)
    #if response.status_code != 200:
        #print(f'Request {i} failed with status code {response.status_code}')

elapsed_time = time.time() - start_time
print(f'Finished making {i+1} requests in {elapsed_time} seconds')
