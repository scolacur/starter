from django.shortcuts import render
from .models import Movie
from .models import Movie, CastMember, Character
from django.http import Http404
from embed_video.backends import detect_backend
from .youtube import youtube_search, execute_youtube_search

# Create your views here.
def index(request):


	# print(movie_list)
	context = {
		'movie_list': Movie.objects.order_by('title')
		# 'movie_list': movie_json['movies']
	}
	return render(request, 'movies/index.html', context);


def detail(request, movie_id):
	try:
		movie = Movie.objects.get(pk=movie_id)
	except Movie.DoesNotExist:
		raise Http404('Movie does not exist')

# Make request to YouTube API for trailer
	q = movie.title + ' trailer'
	args = {
		'q': q,
		'max_results': '1',
		'safeSearch': 'moderate'
	}

	link = execute_youtube_search(args)

	if link:
		movie.video = detect_backend(link)
	else:
		movie.video = detect_backend('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

	context = {
		'movie': movie,
		'my_video': movie.video
	}

	return render(request, 'movies/detail.html', context);
