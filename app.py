from flask import Flask, jsonify, render_template, request
import spotipy
import os
import pyen

en = pyen.Pyen("BKR5Y3OYAZHK5RWGC")
app = Flask(__name__,static_folder="static")

default_name = "vancouver sleep clinic"
name = ""

spot = spotipy.Spotify()
response = {}

@app.route('/default')
def get_artist_uri():
	response = spot.search(q='artist:' + default_name, type='artist')
	if response['artists']['items'] == []:
		response = spot.search(q='artist:' + default_name, type='artist')
	return jsonify(response)

@app.route('/defsongs')
def deflist():
	res = spot.search(q='artist:' + default_name, type='artist')
	resp = spot.artist_top_tracks(res['artists']['items'][0]['uri'])
	return jsonify(resp)

@app.route('/defrelated')
def defRelate():
	tmpName = default_name
	res = spot.search(q='artist:' + tmpName, type='artist')
	relate_resp = spot.artist_related_artists(res['artists']['items'][0]['uri'])
	return jsonify(relate_resp)

@app.route('/biodef')
def defBio():
	res = spot.search(q='artist:' + default_name, type='artist')
	artist_uri = res['artists']['items'][0]['uri']
	echonest_response = en.get( 'artist/profile', id = artist_uri, bucket = ['biographies'] )
	response = {}
	response['status'] = echonest_response['status']
	response['artist'] = {}
	for bio in echonest_response['artist']['biographies']:
		if ('truncated' not in bio) or bio['truncated'] == False:
			response['artist']['biographies'] = [bio]
			break
	return jsonify(response)

"""
search part
"""

@app.route('/search')
def searcher():
	name = request.args.get('artist')
	response = spot.search(q='artist:' + name, type='artist')
	if response['artists']['items'] == []:
		response = spot.search(q='artist:' + name, type='artist')
	return jsonify(response)

@app.route('/songs')
def playlist():
	tmpName = request.args.get('artist')
	res = spot.search(q='artist:' + tmpName, type='artist')
	resp = spot.artist_top_tracks(res['artists']['items'][0]['uri'])
	return jsonify(resp)

@app.route('/related')
def searchRelate():
	tmpName = request.args.get('artist')
	res = spot.search(q='artist:' + tmpName, type='artist')
	relate_resp = spot.artist_related_artists(res['artists']['items'][0]['uri'])
	return jsonify(relate_resp)

@app.route('/biosearch')
def searchBio():
	tmpName = request.args.get('artist')
	res = spot.search(q='artist:' + tmpName, type='artist')
	artist_uri = res['artists']['items'][0]['uri']

	echonest_response = en.get( 'artist/profile', id = artist_uri, bucket=['biographies'])
	response = {}
	response['status'] = echonest_response['status']
	response['artist'] = {}
	for bio in echonest_response['artist']['biographies']:
		if ('truncated' not in bio) or bio['truncated'] == False:
			response['artist']['biographies'] = [bio]
			break
	return jsonify(response)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)
