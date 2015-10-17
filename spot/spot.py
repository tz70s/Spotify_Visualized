import spotipy

class resObj():
	def __init__(self,res,name):
		this.res = res


default_name = "fad"
name = ""

spot = spotipy.Spotify()

default_res = spot.search(q='artist:' + default_name, type='artist')
if default_res['artists']['items'] == []:
	default_res = spot.search(q='artist:' + default_name, type='artist')

def get_name(search_name):
	name = search_name
	res = spot.search(q='artist:' + name, type='artist')
	if res['artists']['items'] == []:
		res = spot.search(q='artist:' + default_name, type='artist')
	return res

def get_uri(res = default_res):
	if res['artists']['items'] != []:
		return res['artists']['items'][0]['uri']

def get_pics_url(res = default_res):
	if res['artists']['items'] != []:
		return res['artists']['items'][0]['images'][0]['url']
def get_genres(res = default_res):
	if res['artists']['items'] != []:
		if res['artists']['items'][0]['genres'] != []:
			return res['artists']['items'][0]['genres']
		else:
			return ["No Genre Display"]

def get_artist_name(res = default_res):
	if res['artists']['items'] != []:
		return res['artists']['items'][0]['name']

def get_followers(res = default_res):
	if res['artists']['items'] != []:
		return "https://embed.spotify.com/follow/1/?uri="+get_uri()+"&size=basic&theme=light"

def get_top_tracks(res = default_res):
	if res['artists']['items'] != []:
		resp = spot.artist_top_tracks(get_uri(res))
		count = 0
		name_list = []
		for track in resp['tracks']:
			name_list.append(track['name'])
			count+=1
			if count == 5:
				break
		return name_list

def get_embed_song(res = default_res):
	if res['artists']['items'] != []:
		resp = spot.artist_top_tracks(get_uri(res))
		play_string = "https://embed.spotify.com/?uri=spotify:trackset:"
		for track in resp['tracks']:
			play_string += track['uri'].strip("spotify:track")
			play_string += ","
		return play_string[:-1]

def get_related_artists(res = default_res):
	if res['artists']['items'] != []:
		relate_resp = spot.artist_related_artists(get_uri(res))
		name_list = []
		for reart in relate_resp['artists']:
			name_list.append(reart['name'])
		return name_list






