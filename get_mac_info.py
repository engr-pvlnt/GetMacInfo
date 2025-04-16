import requests

def lookup_mac_address(mac_address, token):
    url = f"https://api.macvendors.com/v1/lookup/{mac_address}"

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            return data['data']
        elif 'errors' in data:
            return data['errors']
    else:
        return "Not Found"

def main():
    # Get your API in https://macvendors.com/
    token = ""  

    # Get MAC address input from user
    mac_address = input("Enter the MAC address (e.g., FC:FB:FB:01:FA:21): ")
    
    result = lookup_mac_address(mac_address, token)

    print("Result:")
    print(result)

if __name__ == "__main__":
    main()