import os
from urllib.parse import urlparse
import requests
# Import API class from pexels_api package
from pexels_api import API
from requests.structures import CaseInsensitiveDict
# Type your Pexels API
PEXELS_API_KEY = '563492ad6f9170000100000128f0f5bd9d114207967cd6461c6e6f14'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('pets', page=10, results_per_page=100)
# Get photo entries
photos = api.get_entries()
headers = CaseInsensitiveDict()
headers["Authorization"] = "xxx"
# Loop the five photos
for photo in photos:
  # Print photographer
  print('Photographer: ', photo.photographer)
  # Print url
  print('Photo url: ', photo.url)
  # Print original size url
  print('Photo original size: ', photo.large)
  a = urlparse(photo.large)
  filename = os.path.basename(a.path)
  r = requests.get(photo.large, headers=headers)
  open('pets/'+filename, 'wb').write(r.content)