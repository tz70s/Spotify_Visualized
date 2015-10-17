import spotipy

default_name = "fad"
name = "arctic"

spot = spotipy.Spotify()

res = spot.search(q='artist:' + name, type='artist')
if res['artists']['items'] == []:
	res = spot.search(q='artist:' + default_name, type='artist')
temp_uri = ""

def get_uri():
	if res['artists']['items'] != []:
		return res['artists']['items'][0]['uri']

def get_pics_url():
	if res['artists']['items'] != []:
		return res['artists']['items'][0]['images'][0]['url']
def get_genres():
	if res['artists']['items'] != []:
		if res['artists']['items'][0]['genres'] != []:
			return res['artists']['items'][0]['genres']
		else:
			return ["No Genres Display"]

def get_artist_name():
	if res['artists']['items'] != []:
		return res['artists']['items'][0]['name']

def get_followers():
	if res['artists']['items'] != []:
		return "https://embed.spotify.com/follow/1/?uri="+get_uri()+"&size=basic&theme=light"

def get_top_tracks():
	if res['artists']['items'] != []:
		temp_uri = res['artists']['items'][0]['uri']
		resp = spot.artist_top_tracks(temp_uri)
		count = 0
		name_list = []
		for track in resp['tracks']:
			name_list.append(track['name'])
			count+=1
			if count == 5:
				break
		return name_list

def get_embed_song():
	if res['artists']['items'] != []:
		temp_uri = res['artists']['items'][0]['uri']
		resp = spot.artist_top_tracks(temp_uri)
		play_string = "https://embed.spotify.com/?uri=spotify:trackset:"
		for track in resp['tracks']:
			play_string += track['uri'].strip("spotify:track")
			play_string += ","
		return play_string[:-1]

def get_related_artists():
	if res['artists']['items'] != []:
		temp_uri = res['artists']['items'][0]['uri']
		relate_resp = spot.artist_related_artists(temp_uri)
		name_list = []
		for reart in relate_resp['artists']:
			name_list.append(reart['name'])
		return name_list






