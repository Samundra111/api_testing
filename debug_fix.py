import requests

# We use the absolute simplest URL and NO headers
def test_simple_connection():
    url = "https://reqres.in/api/users/2"
    print(f"\nTesting URL: {url}")
    
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Full Response Body: {response.text}")
    
    if response.status_code == 200:
        print("SUCCESS: Your network can reach ReqRes.")
    elif response.status_code == 401:
        print("FAIL: Something in your network/PC is forcing Authentication.")

if __name__ == "__main__":
    test_simple_connection()