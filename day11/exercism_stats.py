#! python3
#  exercism_stats.py
#  Reads data from exercism.io and prints a table
#  Shows info about number of students, mentors,
#  and number of students per mentor

from bs4 import BeautifulSoup

import requests

# TODO: Print table with pretty format

def printFormattedTable(stats):
	print(stats)

# Read name of all tracks
exercism_main = requests.get('https://exercism.io')
exercism_soup = BeautifulSoup(exercism_main.content, 'html.parser')
track_tags = exercism_soup.findAll('a', {"class": "track"})
trackSet = set([track['href'] for track in track_tags])

stats = []

#TODO: Show progress bar

# Iterate track set and get track info
for id, ref in enumerate(trackSet):
	track_request = requests.get('https://exercism.io' + ref)
	track_soup = BeautifulSoup(track_request.content, 'html.parser')
	overview_section = track_soup.findAll('div', {"class": "overview-section"})
	track_stats = overview_section[0].find_all('h3')
	
	stats.append(
		{
			'mentors': track_stats[0].text.split(' ')[0],
			'students': track_stats[1].text.split(' ')[0],
			'exercises': track_stats[2].text.split(' ')[0],
			'track': ref.split('/')[-1].upper()
		}
	)

printFormattedTable(stats)