import time
import requests

services = [
    "https://google.com",
    "https://github.com"
]

for service in services:
    try:
        start_time = time.time()

        response = requests.get(service)

        end_time = time.time()

        response_time = end_time - start_time

        print(f"\nService: {service}")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print("Status: UP")
        else:
            print("Status: DOWN")

        print(f"Response Time: {response_time:.2f} seconds")

    except Exception as e:
        print(f"\nService: {service}")
        print("Status: DOWN")
        print("Error:", e)