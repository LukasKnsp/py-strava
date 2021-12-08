import json
from datetime import datetime
import os

from data_importer.profile_information import ProfileInfo
from data_importer.api import WebImporter


if __name__ == '__main__':

    TOKEN_PATH = r'/Users/lukas/coding/py-strava/my_token.json'
    SAVE_PATH = r'/Users/lukas/coding/py-strava/data'

    # load token
    with open(TOKEN_PATH) as f:
        data = json.load(f)

    profile_info = ProfileInfo(**data)

    # download activities
    importer = WebImporter(profile_info)
    activities = importer.get_activities()
    serialized_activities = [activity.to_dict() for activity in activities]

    # save to json
    today = datetime.today().strftime('%Y-%m-%d')
    filename = 'my_full_strava_data_' + today + '.json'

    os.makedirs(SAVE_PATH, exist_ok=True)
    with open(os.path.join(SAVE_PATH, filename), 'w') as fout:
        json.dump(serialized_activities, fout, ensure_ascii=False, indent=4)