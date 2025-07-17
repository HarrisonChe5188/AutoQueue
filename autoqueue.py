import urllib.request
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client(scope):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='0025a479eee74d20aabee4cfc4b1f1a2',
        client_secret='5b00f8c9de3249cc8de82336624c8de4',
        redirect_uri='http://127.0.0.1:8888/callback',
        scope=scope
    ))


def choose_playlist(sp):
    user_id = sp.me()['id']
    playlists = sp.current_user_playlists()['items']
    print("Do you want to create a new playlist or use an existing one?")
    choice = input("Type 'new' for new playlist or 'existing' for existing: ").strip().lower()
    if choice == 'new':
        name = input("Enter new playlist name: ")
        desc = input("Enter playlist description (optional): ")
        playlist = sp.user_playlist_create(user_id, name, description=desc)
        return playlist['id']
    else:
        print("Your playlists:")
        for idx, pl in enumerate(playlists):
            print(f"{idx+1}: {pl['name']}")
        sel = int(input("Select playlist number: ")) - 1
        return playlists[sel]['id']


def main():
    scope = "playlist-modify-public"
    sp = get_spotify_client(scope)
    playlist_id = choose_playlist(sp)

    website = input('Paste Youtube link below\n')
    print('\n')
    fp = urllib.request.urlopen(website)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()

    pattern = r'"VIDEO_ATTRIBUTE_IMAGE_STYLE_SQUARE","title":"(.*?)","subtitle":"(.*?)"'
    matches = re.finditer(pattern, mystr)

    track_uris = []
    for m in matches:
        title = m.group(1)
        artist = m.group(2)
        query = f"{title} {artist}"
        print(f"Searching for: {query}")
        results = sp.search(query, limit=1, type='track')
        tracks = results['tracks']['items']
        if tracks:
            track_uri = tracks[0]['uri']
            print(f"Found: {tracks[0]['name']} by {tracks[0]['artists'][0]['name']}")
            track_uris.append(track_uri)
        else:
            print("No track found for:", query)

    if track_uris:
        sp.playlist_add_items(playlist_id, track_uris)
        print(f"{len(track_uris)} tracks added to playlist!")
    else:
        print("No tracks to add.")


if __name__ == '__main__':
    main()








