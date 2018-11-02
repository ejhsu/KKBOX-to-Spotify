# Transfer playlist from KKBOX to Spotify

# Steps

1. export playlist from kkbox as a .kbl file
2. create Spotify app at [Spotify App Dashboard](https://developer.spotify.com/dashboard/applications)
3. find your client id and secret
4. export the following variables:
```sh
export SPOTIPY_CLIENT_ID=${YOUR_CLIENT_ID}
export SPOTIPY_CLIENT_SECRET=${YOUR_CLIENT_SECRET}
export SPOTIPY_REDIRECT_URI=http://localhost
```

5. set `http://localhost` to *Redirect URIs* in your app

6. run `python3 run.py ${YOUR_USER_ID}`
