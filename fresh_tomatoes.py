''' This module merges several HTML files to create a dynamic webpage. '''

import webbrowser
import os
import re


def parse_html(html):
    """ returns html string from `HTML/_<template>.html` """
    return ''.join([row for row in open('HTML/_{}.html'.format(html),
                                        'r').readlines()])

# load the styles and scripting for the page
MAIN_PAGE_HEAD = parse_html('head')

# Load the main page layout and title bar
MAIN_PAGE_CONTENT = parse_html('main')

# load a single movie entry html template
MOVIE_TILE_CONTENT = parse_html('tile')

# load a single modal movie entry html template
INFO_MODAL_CONTENT = parse_html('infoModal')


def create_movie_tiles_content(movies):
    '''Creates a tile to be displayed for each movie on the webpage.'''
    # The HTML content for this section of the page
    merged_tile_content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        merged_tile_content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
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
            movie_awards=movie.awards,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return merged_tile_content


def open_movies_page(movies):
    '''Function that creates a movies file and appends rendered HTML to it.'''
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles and movie modals placeholders generated content
    rendered_content = MAIN_PAGE_HEAD + MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies))

    # clean up html where it is inserting non breaking space
    rendered_content = unicode(rendered_content, "UTF-8")
    rendered_content = rendered_content.replace(u"\u00A0", " ")

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
