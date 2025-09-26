import requests

def greet():
    print("Hello, Legacy Steward!")
    try:
        response = requests.get("https://api.github.com")
        print("GitHub API status:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error reaching GitHub API:", e)

if __name__ == "__main__":
    greet()