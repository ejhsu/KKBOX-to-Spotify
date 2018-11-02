from lxml import etree
from utils import cleanText

class KBLParser(object):
  def parse(self, source='./kkbox.kbl'):
    tree = etree.parse(source, parser=etree.HTMLParser(encoding='utf-8'))
    root = tree.getroot()

    playlists = []

    for playlist in root.findall('.//playlist'):
      playlist_name = playlist.find('playlist_name').text

      song_datas = playlist.find('playlist_data').findall('.//song_data')
      songs = []

      for song in song_datas:
        name = cleanText(song.find('song_name').text)
        artist = cleanText(song.find('song_artist').text)
        album = cleanText(song.find('song_album').text)
        songs.append({'name': name, 'artist': artist, 'album': album})

      playlists.append({'name': playlist_name, 'songs': songs})


    return playlists

if __name__ == '__main__':
  parser = KBLParser()
  parser.parse()
