import webbrowser

class Movie():

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17", "NR"]

    def __init__(self, movie_title, movie_year, movie_rating, movie_released, movie_runtime, movie_genre, movie_director, movie_writer, movie_actors, movie_plot, movie_language, movie_country, movie_awards, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.rating = movie_rating
        self.released = movie_released
        self.duration = movie_runtime
        self.genre = movie_genre
        self.director = movie_director
        self.writer = movie_writer
        self.actors = movie_actors
        self.plot = movie_plot
        self.language = movie_language
        self.country = movie_country
        self.awards = movie_awards
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
