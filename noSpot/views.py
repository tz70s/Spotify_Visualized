from django.shortcuts import render
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
