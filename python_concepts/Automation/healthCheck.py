import requests
import time

url = "https://google.com"

try:
    start_time = time.time()

    response = requests.get(url)

    end_time = time.time()

    response_time = (end_time - start_time) * 1000

    print("Website:", url)

    if response.status_code == 200:
        print("Status: OK")
    else:
        print("Status: FAILED")

    print("HTTP Status Code:", response.status_code)
    print(f"Response Time: {response_time:.2f} ms")

except requests.exceptions.RequestException as e:
    print("Website Down!")
    print("Error:", e)