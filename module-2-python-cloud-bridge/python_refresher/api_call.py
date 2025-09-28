# 🌐 API Invocation with Requests

import requests

response = requests.get("https://api.github.com")
print("GitHub API status code:", response.status_code)