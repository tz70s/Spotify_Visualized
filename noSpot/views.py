from django.shortcuts import render
from django.http import HttpResponse
from spot import spot

# Create your views here.

# from django.http import HttpResponse
"""
def hello_world(request):
	return render(request,
		'hello_world.html',
		{'current_time': datetime.now()})
"""


def index(request):
	return render(request,'index.html',
		{'profile_pic':spot.get_pics_url(),
		 'genre_list':spot.get_genres(),
		 'followers':spot.get_followers(),
		 'artist_name':spot.get_artist_name(),
		 'top_tracks':spot.get_top_tracks(),
		 'related_artists':spot.get_related_artists(),
		 'embed_source':spot.get_embed_song(),
		})

def search(request):
	search_name = request.GET['search_name']
	spot.get_name(search_name)
	return render(request,'index.html',
		{'profile_pic':spot.get_pics_url(spot.get_name(search_name)),
		 'genre_list':spot.get_genres(spot.get_name(search_name)),
		 'followers':spot.get_followers(spot.get_name(search_name)),
		 'artist_name':spot.get_artist_name(
	spot.get_name(search_name)),
		 'top_tracks':spot.get_top_tracks(spot.get_name(search_name)),
		 'related_artists':spot.get_related_artists(spot.get_name(search_name)),
		 'embed_source':spot.get_embed_song(spot.get_name(search_name)),
		})