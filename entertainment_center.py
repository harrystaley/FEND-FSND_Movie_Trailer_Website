import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "1995",
    "G",
    "22 Nov 1995",
    "81 min",
    "Animation, Adventure, Comedy",
    "John Lasseter",
    "John Lasseter (original story by), Pete Docter (original story by), Andrew Stanton (original story by), Joe Ranft (original story by), Joss Whedon (screenplay), Andrew Stanton (screenplay), Joel Cohen (screenplay), Alec Sokolow (screenplay)",
    "Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy"s room.",
    "English",
    "USA",
    "Nominated for 3 Oscars. Another 22 wins & 16 nominations.",
    "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SX300.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

terminator2 = media.Movie(
    "Terminator 2: Judgment Day",
    "1991",
    "R",
    "03 Jul 1991",
    "137 min",
    "Action, Sci-Fi",
    "James Cameron",
    "James Cameron, William Wisher Jr.",
    "Arnold Schwarzenegger, Linda Hamilton, Edward Furlong, Robert Patrick",
    "A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her young son, John Connor, from a more advanced cyborg, made out of liquid metal.",
    "English, Spanish",
    "USA, France",
    "Won 4 Oscars. Another 20 wins & 22 nominations.",
    "http://ia.media-imdb.com/images/M/MV5BMTg5NzUwMDU5NF5BMl5BanBnXkFtZTcwMjk2MDA4Mg@@._V1_SX300.jpg",
    "https://www.youtube.com/watch?v=eajuMYNYtuY")

minions = media.Movie(
    "Minions",
    "2015",
    "PG",
    "10 Jul 2015",
    "91 min",
    "Animation, Comedy, Family",
    "Kyle Balda, Pierre Coffin",
    "Brian Lynch",
    "Sandra Bullock, Jon Hamm, Michael Keaton, Allison Janney",
    "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.",
    "English",
    "USA",
    "N/A",
    "http://ia.media-imdb.com/images/M/MV5BMTg2MTMyMzU0M15BMl5BanBnXkFtZTgwOTU3ODk4NTE@._V1_SX300.jpg",
    "https://www.youtube.com/watch?v=dVDk7PXNXB8"    )

movies = [toy_story, terminator2, minions]
fresh_tomatoes.open_movies_page(movies)
