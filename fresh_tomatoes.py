import webbrowser
import os
import re

def parse_html(html):
    """ returns html string from `HTML/_<template>.html` """
    return ''.join([row for row in open('HTML/_{}.html'.format(html),
                                        'r').readlines()])

# load the styles and scripting for the page
main_page_head = parse_html('head')

# Load the main page layout and title bar
main_page_content = parse_html('main')

# load a single movie entry html template
movie_tile_content = parse_html('tile')

# load a single modal movie entry html template
info_modal_content = parse_html('infoModal')

def create_movie_tiles_content(movies):
    '''Creates a tile to be displayed for each movie on the webpage.'''
    # The HTML content for this section of the page
    tileContent = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        tileContent += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return tileContent

def create_info_modals_content(movies):
    '''Creates a modal for the pertinant movie info for each movie.'''
    # The HTML content for this section of the page
    modalContent = ''
    for movie in movies:
        # Append the modal for the movie with its content filled in
        modalContent += info_modal_content.format(
            movie_year=movie.year,
            movie_rating=movie.rating,
            movie_released=movie.released,
            movie_runtime=movie.duration,
            movie_genre=movie.genre,
            movie_director=movie.director,
            movie_writer=movie.writer,
            movie_actors=movie.actors,
            movie_plot=movie.plot,
            movie_language=movie.language,
            movie_country=movie.country,
            movie_awards=movie.awards
        )
    return modalContent

def open_movies_page(movies):
    '''Function that creates a movies file and appends rendered HTML to it.'''
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Replace the placeholder genrated content
    rendered_content = rendered_content.format(
        movie_modals=create_info_modals_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
