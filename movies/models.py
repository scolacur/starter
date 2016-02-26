from django.db import models
import json
from django.conf import settings

# Create your models here.

class Movie(models.Model):
	rotten_tomatoes_id = models.DecimalField(max_digits=255, decimal_places=0)
	title = models.CharField(max_length=255)
	year = models.IntegerField()
	mpaa_rating = models.CharField(max_length=255)
	runtime = models.IntegerField()
	theatre_release_date = models.DateField(null=True)
	synopsis = models.TextField(max_length=255, default='N/A')
	#has foreign keys CastMember, Rating
	critics_rating = models.CharField(max_length=255, default='N/A')
	critics_score = models.IntegerField(default='-1')
	# extrathing = models.CharField(max_length=255, default='N/A')
	thumb = models.CharField(max_length=255, default='#')
	poster = models.CharField(max_length=255, default='#')
	audience_score = models.IntegerField(default='-1')

	def __str__(self):
		return self.title

class CastMember(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	cast_member_id = models.IntegerField()
	name = models.CharField(max_length=255)
	#has foreign key Character

class Character(models.Model):
	cast_member = models.ForeignKey(CastMember, on_delete=models.CASCADE)






# Import json
def import_from_json():
	json_data = open(settings.BASE_DIR + '/starter/data/movies.json')
	movie_json = json.load(json_data)

	count = 1

	# Save data from json to DB
	for movie in movie_json['movies']:
		
		newMovie,created = Movie.objects.get_or_create(
			rotten_tomatoes_id	= movie['id'] 						or -1,
			title				= movie['title'] 					or 'N/A',
			year				= movie['year'] 					or -1,
			mpaa_rating			= movie['mpaa_rating'] 				or 'N/A',
			runtime				= movie['runtime'] 					or -1,
			theatre_release_date= movie['release_dates']['theater'] or -1,
			synopsis			= movie['synopsis'] 				or 'N/A',
			thumb				= movie['posters']['profile']		or '#',
			poster				= movie['posters']['original']		or '#'
		)

		try:
			newMovie.critics_rating	= movie['ratings']['critics_rating']
		except KeyError:
			newMovie.critics_rating = 'N/A'

		try:
			newMovie.critics_score	= movie['ratings']['critics_score']
		except KeyError:
			newMovie.critics_score = -1

		try:
			newMovie.audience_score	= movie['ratings']['audience_score']
		except KeyError:
			newMovie.audience_score = -1

		newMovie.save()

		count += 1

import_from_json()
