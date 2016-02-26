#Notes

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
