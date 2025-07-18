from dataclasses import dataclass

@dataclass
class User:
    id: str
    username: str
    name: str
    created_at: str = None
    description: str = None
    location: str = None
    url: str = None
    verified: bool = None
    profile_image_url: str = None