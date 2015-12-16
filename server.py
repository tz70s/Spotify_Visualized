from flask import Flask, jsonify, render_template, request
import spotipy

app = Flask(__name__)

default_name = "fad"
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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
