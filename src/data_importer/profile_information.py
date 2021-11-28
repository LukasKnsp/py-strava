from pydantic import BaseModel


class ProfileInfo(BaseModel):
    """contains all relevant information to get access to the strava api"""
    client_id: str
    client_secret: str
    refresh_token: str