from typing import List

from stravalib.client import Client
from stravalib.model import Activity, Athlete


class WebImporter:
  """imports data from web (strava api)"""
  def __init__(self, client_id: str, client_secret: str, refresh_token: str) -> None:

      self._client = Client()
      self._refresh_access_token(client_id, client_secret, refresh_token)

  def _refresh_access_token(self, client_id: str, client_secret: str, refresh_token: str):
    """get access token to use the api, see https://github.com/hozn/stravalib"""
    self._client.refresh_access_token(client_id, client_secret, refresh_token)

  def get_activities(self) -> List[Activity]:
    print('downloading activities from web...')
    activities = self._client.get_activities()
    print('finished')
    return list(activities)

  def get_athlete(self) -> Athlete:
      return self._client.get_athlete()

