import json

from data_importer.profile_information import ProfileInfo
from data_importer.api import WebImporter


if __name__ == '__main__':

    with open('./my_token.json') as f:
        token = json.load(f)

    profile = ProfileInfo(**token)

    importer = WebImporter(profile)
    athlete = importer.get_athlete()

    activities = importer.get_activities()

    for activity in activities:
        print(activity)
    print(athlete)