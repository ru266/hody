import requests
import os
from .exceptions import InvalidCredentials, UserNotFound, RateLimitExceeded
from .user import User

class TwitterFetcher:
    BASE_URL = "https://api.twitter.com/2"
    
    def __init__(self, bearer_token=None):
        self.bearer_token = bearer_token or os.getenv('TWITTER_BEARER_TOKEN')
        if not self.bearer_token:
            raise InvalidCredentials("Twitter Bearer Token not provided. Set TWITTER_BEARER_TOKEN environment variable.")

    def _make_request(self, endpoint, params=None):
        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise InvalidCredentials("Invalid Twitter API credentials")
        elif response.status_code == 404:
            raise UserNotFound("Twitter user not found")
        elif response.status_code == 429:
            raise RateLimitExceeded("Twitter API rate limit exceeded")
        else:
            response.raise_for_status()

    def fetch_by_username(self, username):
        endpoint = "/users/by"
        params = {
            "usernames": username,
            "user.fields": "id,name,username,created_at,description,location,url,verified,profile_image_url"
        }
        data = self._make_request(endpoint, params)
        return User(**data['data'][0])

    def fetch_by_email(self, email):
        # Requires Academic Research access
        endpoint = "/users/by"
        params = {
            "user.fields": "id,name,username,created_at,description,location,url,verified,profile_image_url",
            "query": email
        }
        data = self._make_request(endpoint, params)
        return User(**data['data'][0])