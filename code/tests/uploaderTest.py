import os

# Function to generate title and description
def generate_title_and_description(video_path):
    filename = os.path.basename(video_path)
    title = f"Exciting Insights from {filename}"
    description = f"This video explores fascinating topics and provides in-depth knowledge. Watch to learn more about the amazing content from {filename}!"
    return title, description

# Main function for testing
if __name__ == "__main__":
    video_path = "videos/test_video.mp4"  # Change this to your test video
    if os.path.exists(video_path):
        title, description = generate_title_and_description(video_path)
        print("\n--- Generated Title ---")
        print(title)
        print("\n--- Generated Description ---")
        print(description)
    else:
        print("Video file not found! Please check the path.")
