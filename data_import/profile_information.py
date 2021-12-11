from dataclasses import dataclass
import json


@dataclass
class ProfileInfo:
    """contains all relevant information to get access to the strava api"""
    client_id: str
    client_secret: str
    refresh_token: str

    @classmethod
    def from_json(cls, path: str) -> 'ProfileInfo':
        with open(path) as f:
            data = json.load(f)

        return cls(**data)
