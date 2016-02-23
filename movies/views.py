from django.shortcuts import render
from .models import Movie
from .models import Movie, CastMember, Character
from django.http import Http404
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
	return render(request, 'movies/detail.html', {'movie': movie});
	# return HttpResponse('Hello, youre at the detail view for movie %s' % movie_id)
