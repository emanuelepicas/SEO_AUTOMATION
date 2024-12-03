import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv("code/.env")

# Function to upload video to Facebook
def upload_to_facebook(video_path, caption):
    access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
    url = f"https://graph-video.facebook.com/v12.0/me/videos"
    with open(video_path, 'rb') as video_file:
        response = requests.post(
            url,
            params={"access_token": access_token},
            files={"source": video_file},
            data={"description": caption}
        )
    if response.status_code == 200:
        print("Video uploaded to Facebook successfully!")
    else:
        print(f"Facebook upload failed: {response.json()}")

# Function to upload video to Instagram
def upload_to_instagram(video_path, caption):
    access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
    url = f"https://graph.facebook.com/v12.0/{os.getenv('INSTAGRAM_USER_ID')}/media"
    with open(video_path, 'rb') as video_file:
        response = requests.post(
            url,
            params={"access_token": access_token},
            files={"video": video_file},
            data={"caption": caption}
        )
    if response.status_code == 200:
        print("Video uploaded to Instagram successfully!")
    else:
        print(f"Instagram upload failed: {response.json()}")

# Function to upload video to Twitter
def upload_to_twitter(video_path, caption):
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET")
    url = "https://upload.twitter.com/1.1/media/upload.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    with open(video_path, 'rb') as video_file:
        response = requests.post(
            url,
            headers=headers,
            files={"media": video_file}
        )
    if response.status_code == 200:
        print("Video uploaded to Twitter successfully!")
    else:
        print(f"Twitter upload failed: {response.json()}")

# Function to upload video to YouTube
def upload_to_youtube(video_path, title, description):
    api_key = os.getenv("YOUTUBE_API_KEY")
    url = "https://www.googleapis.com/upload/youtube/v3/videos"
    headers = {"Authorization": f"Bearer {api_key}"}
    metadata = {
        "snippet": {
            "title": title,
            "description": description
        },
        "status": {
            "privacyStatus": "public"
        }
    }
    files = {
        "media": open(video_path, 'rb'),
        "snippet": (None, metadata)
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        print("Video uploaded to YouTube successfully!")
    else:
        print(f"YouTube upload failed: {response.json()}")

# Main execution
if __name__ == "__main__":
    video_file = "videos/sample_video.mp4"
    caption = "Check out my latest video on AI and cybersecurity!"
    title = "AI and Cybersecurity"
    description = "An in-depth look at how AI is revolutionizing cybersecurity."

    upload_to_facebook(video_file, caption)
    upload_to_instagram(video_file, caption)
    upload_to_twitter(video_file, caption)
    upload_to_youtube(video_file, title, description)
