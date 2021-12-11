from data_import.profile_information import ProfileInfo
from data_import.data_download import download_activities_from_api


if __name__ == '__main__':
    from datetime import datetime

    profile_info = ProfileInfo.from_json(path='./my_token.json')

    filename = 'activities_' + datetime.today().strftime("%Y-%m-%d")
    
    download_activities_from_api(profile_info, './data', filename)