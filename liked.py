import json
import requests
from secrets import spotify_user_id

class CreatePlaylists:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    #Log into youtube
    def get_youtube_client(self):
        pass
        pass
        pass

    #Grab the liked videos
    def get_liked_videos(self):
        pass

    # Create a new playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            header={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist_id
        return response_json["id"]

    # Search for the song
    def get_spotify_uri(self, song_name, artist):
                """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]

        return uri

    # Add this song into the new spotify playlist
    def add_song_to_playlist(self):
        pass
