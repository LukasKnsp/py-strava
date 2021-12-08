from stravalib.model import Activity, Athlete
from typing import List, Dict
import json

from data_importer.base import Importer


class ImporterJSON(Importer):
    def __init__(self, json: List[Dict]) -> None:
        self.activities = list()
        self._json = json

    def get_activities(self) -> List[Activity]:
        return [Activity(**activity) for activity in self._json]

    def get_athlete() -> Athlete:
        pass
    