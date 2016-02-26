from django.shortcuts import render, HttpResponseRedirect

def landing_page(request):

	#I didn't want to put the movies view on the main landing page,
	# since in a larger app we might want to reserve the home page for
	# something else. So right now I'll just redirect to /movies.

	return HttpResponseRedirect('/movies')
