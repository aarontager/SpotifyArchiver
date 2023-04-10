from constants import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID, DISCOVER_PLAYLIST_ID, DISCOVER_ARCHIVE_PLAYLIST_ID, RELEASE_PLAYLIST_ID, RELEASE_ARCHIVE_PLAYLIST_ID

import spotipy
import spotipy.oauth2 as oauth

auth_manager = oauth.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                  client_secret=SPOTIFY_CLIENT_SECRET,
                                  redirect_uri="http://localhost:8080/callback",
                                  scope="playlist-modify-public, playlist-modify-private, user-library-read")
spotify = spotipy.Spotify(auth_manager=auth_manager)
me = spotify.me()


def get_song_list_from_spotify(playlist_uri):
    tracks = spotify.playlist_tracks(playlist_uri)["items"]
    songs = []

    for track in tracks:
        track = track["track"]
        songs.append(track["uri"])
    return songs


if __name__ == "__main__":
    song_list = get_song_list_from_spotify(playlist_uri=DISCOVER_PLAYLIST_ID)
    spotify.playlist_add_items(DISCOVER_ARCHIVE_PLAYLIST_ID, song_list)
    
    song_list_release = get_song_list_from_spotify(playlist_uri=RELEASE_PLAYLIST_ID)
    spotify.playlist_add_items(RELEASE_ARCHIVE_PLAYLIST_ID, song_list_release)
