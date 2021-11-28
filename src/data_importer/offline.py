from stravalib.model import Activity
from typing import List, Dict
import json


class ImporterJSON:
    def __init__(self, json: List[Dict]) -> None:
        self.activities = list()
        self._json = json

    def convert(self):
        activities = [Activity(**activity) for activity in self._json]

        return activities


if __name__ == '__main__':

    with open('/Users/lukas/coding/py-strava/my_full_strava_data.json') as f:
        data = json.load(f)

    importer = ImporterJSON(data)
    activities = importer.convert()

    for activity in activities:
        print(activity)
    