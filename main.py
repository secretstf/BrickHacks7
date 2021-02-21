import os
import requests # gives access to websites

# Set or replace these values
# I think you have to upload it to the repo, so you can upload the file to the repo.
# Its on the left I believe
file_path = os.environ["TestSong.mp3"]
api_key = os.environ["bboZsjxKSeuRPApxB6svab4GUdQGzLq2"]

# Declare your dlb:// location

url = "https://api.dolby.com/media/input"
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json",
}

body = {
    "url": "dlb://in/example.mp4",
}

response = requests.post(url, json=body, headers=headers)
response.raise_for_status()
data = response.json()
presigned_url = data["url"]

# Upload your media to the pre-signed url response

print("Uploading {0} to {1}".format(file_path, presigned_url))
with open(file_path, "rb") as input_file:
  requests.put(presigned_url, data=input_file)