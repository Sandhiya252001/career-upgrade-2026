import time
import requests
url="https://google.com"
start_time=time.time()
response= requests.get(url)
end_time=time.time()
Response_time=(end_time-start_time)*1000
print(f"Status: UP",
f"\nResponse Time:{Response_time}"
)
    