import json
import os

from data_import.profile_information import ProfileInfo
from data_import.api import WebImporter


def download_activities_from_api(
    profile: ProfileInfo, 
    save_path: str, 
    file_name: str = 'activities'
):

    # download activities
    importer = WebImporter(profile.client_id, profile.client_secret, profile.refresh_token)
    activities = importer.get_activities()
    serialized_activities = [activity.to_dict() for activity in activities]

    # save to json
    os.makedirs(save_path, exist_ok=True)
    filename = file_name + '.json'
    
    with open(os.path.join(save_path, filename), 'w') as fout:
        json.dump(serialized_activities, fout, ensure_ascii=False, indent=4)

    