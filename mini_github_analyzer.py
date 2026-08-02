import requests

base_url = "https://api.github.com/users/"

def client_data():
    name = input("Enter a username: ").strip()
    url = f"{base_url}{name}"
    try:
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(url)
        print(f"status code = {response.status_code}")
        return response
    except requests.exceptions.ConnectionError:
        print("Network error: Please check your internet connection or DNS.")
        return None
    except requests.exceptions.Timeout:
        print("Timeout error: GitHub took too long to respond.")
        return None

def user_data(user_response):
    if user_response is None:
        return None
    elif user_response.status_code == 200:
        return user_response.json()
    elif user_response.status_code == 403:
        print(" you have exceeded the limit rate, try again after sometimes :)")
    elif user_response.status_code == 404:
        print("github user not found")
    elif user_response.status_code == 500:
        print("(Internal Server Error): Something broke in GitHub's code")
    elif user_response.status_code == 502:
        print("(Bad Gateway): The server you reached tried to talk to another GitHub server, and failed.")
    elif user_response.status_code == 503:
        print("(Service Unavailable): GitHub is intentionally down for maintenance or completely overloaded.")
    


r = client_data()
data = user_data(r)

try:
    print(f"name: {data['name']}")
    print(f"followers: {data['followers']}")
    print(f"following: {data['following']}")
    print(f"public respostories: {data['public_repos']}")
    print(f"account created date: {data['created_at']}")
    print(f"profile url: {data['html_url']}")

except TypeError:
    pass


