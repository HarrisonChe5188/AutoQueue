# AutoQueue
# AutoQueue

AutoQueue is a Python script that automatically populates a Spotify playlist with tracks detected from a YouTube page. It scrapes the video titles and artists from the page source, searches for matching songs on Spotify, and queues them into a selected or newly created playlist.

## Features

* 🔍 Scrapes video titles and artists from YouTube URLs
* 🎵 Searches for tracks on Spotify using Spotipy
* 🏆 Adds found tracks to an existing or new playlist
* 🔐 Uses Spotify OAuth for secure access

## Requirements

* Python 3.6+
* Spotify Developer credentials (Client ID and Client Secret)
* A valid Spotify account

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AutoQueue.git
cd AutoQueue
```

2. Install the required dependencies:

```bash
pip install spotipy
```

3. Set up your Spotify Developer credentials:

Go to [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) and create an app. Replace the `client_id`, `client_secret`, and `redirect_uri` in the script with your app's credentials.

## Usage

Run the script with:

```bash
python autoqueue.py
```

Follow the on-screen prompts:

1. Choose to create a new playlist or use an existing one
2. Paste a YouTube playlist or video link
3. The script will scrape the titles and add matched songs to your playlist

## Example

```text
Do you want to create a new playlist or use an existing one?
Type 'new' for new playlist or 'existing' for existing: new
Enter new playlist name: YouTube Finds
Enter playlist description (optional): Songs from a cool YouTube playlist
Paste Youtube link below
https://www.youtube.com/playlist?list=PLabc123...
Searching for: Song Title Artist Name
Found: Song Title by Artist Name
...
10 tracks added to playlist!
```

## Notes

* This script relies on YouTube's current page structure; if YouTube changes its HTML format, the scraping regex may break.
* Ensure the YouTube page is publicly accessible and contains a list of music videos.

## License

This project is for educational and personal use only. It is not affiliated with or endorsed by YouTube or Spotify.



