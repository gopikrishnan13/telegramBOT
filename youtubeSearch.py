YoutubeAPIKEY = 'AIzaSyD8U_ZxCerZ4ELN95srCzu0hcd12p0ivWw' #youtube api key keep private

import json
from googleapiclient.discovery import build #google api cline module
youtube = build('youtube', 'v3', developerKey=YoutubeAPIKEY) #create object 

#search youtube video send request
request = youtube.search().list(
    part='snippet',
    q='Class 3 - Project Management, Version Control, Maintainance'
)
response = request.execute() #send request to youtube
#print(json.dumps(response, indent=2))
#create youtube link
Videolink = 'https://www.youtube.com/watch?v={}'.format(response['items'][0]['id']['videoId']) 
print (json.dumps(response, indent=2))
