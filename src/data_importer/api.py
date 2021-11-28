import json
from typing import List
from stravalib.client import Client
from stravalib.model import Activity, Athlete

from data_importer.profile_information import ProfileInfo
from data_importer.base import Importer


class WebImporter(Importer):
  """imports data from web (strava api)"""
  def __init__(self, profile_info: ProfileInfo) -> None:
      self._profile = profile_info

      self._client = Client()
      self._refresh_access_token()

  def _refresh_access_token(self):
    """get access token to use the api, see https://github.com/hozn/stravalib"""
    self._client.refresh_access_token(**self._profile.dict())

  def get_activities(self) -> List[Activity]:
    activities = self._client.get_activities()
    return list(activities)

  def get_athlete(self) -> Athlete:
      return self._client.get_athlete()

