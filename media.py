import webbrowser

class Video():
	"""
	This is hte parent class for Movie and Tvshow.
	"""
	def __init__(self, video_title, video_duration):
		self.title = video_title
		self.duration = video_duration
		
class Tvshow(Video):
	"""
	This is a child class of video.
	"""
	
	VALID_RATINGS = ["TV Y", "TV Y7", "TV Y7 FV", "TV G", "TV PG", "TV 14", "TV MA"]
	
	def __init__(self, video_title, video_duration):
		Video.__init__(video_title, video_duration)
		self.arg = arg
		

class Movie(Video):
	""" 
	This is a child class of Video.

	This Class defines the germain informaiton for each movie displayed on my movie website.
	This rating information includes rating, title, story line, the web address for the movie 
	poster and the movie trailer on youtube.

	This also includes a call to the web browser to play the video.
	"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17", "NR"]

	def __init__(self, video_title, video_duration, movie_storyline, poster_image, trailer_youtube):
		Video.__init__(video_title, video_duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)