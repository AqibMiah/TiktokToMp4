import os
import yt_dlp


def download_tiktok_video(url, output_path='/Users/aqibmiah/Desktop/Tiktoks/'):
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Options for yt-dlp
    ydl_opts = {
        'format': 'best',  # Choose the best quality available
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Save as video title
        'noplaylist': True,  # Download only a single video
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video

        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    tiktok_url = input("Please enter the TikTok video URL: ")

    # Save the video to the specified path
    download_tiktok_video(tiktok_url, output_path='/Users/aqibmiah/Desktop/Tiktoks/')
