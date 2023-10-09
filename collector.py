import requests

class Collector:
    def __init__(self, api_url, api_token=None):
        self.api_url = api_url
        self.api_token = api_token

    def get_data(self, params=None):
        headers = {"Content-Type": "application/json",
                 "Accept": "application/json",}
        if self.api_token:
            headers["Authorization"] = f"Bearer {self.api_token}"
        try:
            response = requests.get(self.api_url, headers=headers, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()  
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


