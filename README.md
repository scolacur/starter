Instructions
----

Hi there, and thanks for applying to join the core FLE dev team!
To give you a chance to demonstrate how you approach a problem,
using a variety of technologies and a healthy dose of creative
freedom, we've put together this short practice project. To make
it a bit faster for you to get started, we put together this
skeleton repository that you can use as a starting point.

Within this repository's `starter/data/` folder is a `movies.json`
file, which is a snapshot of the Rotten Tomatoes API. Your task is to
display all the movies (e.g. in a list), and allow the user to view details
of a movie once it's clicked. You can use whatever technologies and
methods you'd like to accomplish this task; the only requirement is to
use Django as the backend web framework. You can also add other features
such as search or filtering, make it a single-page JS app, or focus on
making it pretty, etc.

So to get things started, do the following:

1. Clone this repo into your local machine (DO NOT FORK!)
2. Create a new repository in your github account
3. Change your local repository's origin remote to point to your new remote Github repository
4. Once you're satisfied with your code, push your local repository into the remote Github repository
5. Send us the link to your Github repo!

That's it! We'll review your code soon and get back to you once we're done!

#notes

I tried to do several things, all rather imperfectly, just as an MVP sort of thing. Here are a few things I did:

Updated the project to the newest version of Django

Added ‘movies’ as its own app, to make the application more modular. In general, I tried to keep the code as modular and reusable as possible.

JSON Parsing
The json is parsed and movie objects are added to the DB immediately after the models are created, so that it happens only once, rather than whenever a view is loaded. If I were hitting the actual API, I might want to update the DB more frequently, and maybe implement caching.

YouTube Search API
I connected the YouTube search API to get the trailers for each movie. You can see youtube.py for details. I gitignored the API key.

The site is pretty responsive as I took advantage of bootstrap's grid system.


Things I would do with more time
-Use SCSS instead of pure CSS
-Integrate build automation for faster iteration
-Hook up to the actual rotten tomatoes API to get up to date information on app load
-Add a link to torrent the movie xD
-Searching, filtering, favorites, etc..


This was my first experience with both Python and Django, and I learned this mostly by reading the Django documentation and following their tutorials, so please forgive any faux pas / bad practice :)

I actually had a lot of fun with this, so thanks for the opportunity to learn something new!
