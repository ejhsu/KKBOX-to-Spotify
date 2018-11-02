import sys

import spotipy
import spotipy.util as util

from utils import urlencode
from kbl_parser import KBLParser

scope = 'playlist-read-private playlist-modify-private'


class Spotify():
  def __init__(self, user, token):
    self.sp = spotipy.Spotify(auth=token)
    self.user = user

  def create_playlist(self, name):
    playlist = self.sp.user_playlist_create(self.user, name, public=False)
    return playlist['id']

  def add_tracks_to_playlist(self, playlist_id, tracks):
    self.sp.user_playlist_add_tracks(self.user, playlist_id, tracks)
    

  def search(self, track, artist='', album='', fallback=True, market=None):
    results = self.sp.search(q='track:{} album:{}'.format(track, ' '.join(album.split(' ')[:3])), limit=1, market=market)
    if results['tracks']['total'] == 0:
      print('could not find {}[{}]'.format(track, album))
      # fallback to search track name only
      results = self.sp.search(
          q='track:{}'.format(track), limit=1)
      
      if results['tracks']['total'] == 0:
        return ''
      else:
        print('but found in fallback mode')
    t = results['tracks']['items'][0]
    track_id = t['id']

    return track_id


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('usage: python3 {} <user_id>'.format(sys.argv[0]))
    exit(1)
  user = sys.argv[1]
  token = util.prompt_for_user_token(user, scope)
  
  sp = Spotify(user, token)
  
  for playlist in KBLParser().parse():
    # create play list
    playlist_name = playlist['name']
    playlist_id = sp.create_playlist(playlist_name)

    tracks = []
    for song in playlist['songs']:
      # search the corresponding song
      song_name = song['name']
      song_artist = song['artist']
      song_album = song['album']
      track_id = sp.search(song_name, album=song_album)

      if track_id == '':
        print('could not find {} by {} in {}'.format(
            song_name, song_artist, playlist_name))
      else:
        tracks.append(track_id)
    sp.add_tracks_to_playlist(playlist_id, tracks)
    input()


