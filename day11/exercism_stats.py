#! python3
#  exercism_stats.py
#  Reads data from exercism.io and prints a table
#  Shows info about number of students, mentors,
#  and number of students per mentor

from bs4 import BeautifulSoup

import requests

def printFormattedTable(stats):
	#titles = stats.keys

	for row in stats:
		line = '|'.join(row['track'].ljust(12))
		print(line)

# 1 - Read name of all tracks from:
# https://exercism.io/#explore-languages
exercism_main = requests.get('https://exercism.io')

#if exercism_main.status_code == 200:
#	print('Request completed succesfully')

exercism_soup = BeautifulSoup(exercism_main.content, 'html.parser')

track_tags = exercism_soup.findAll('a', {"class": "track"})

trackSet = set([track['href'] for track in track_tags])

# 2 - Generate object with stats and names (empty)
# First test, retrieve stats for one track

stats = []

# 3 - Read data from track pages (https://exercism.io/tracks/{})
#   - Show completion graph

for id, ref in enumerate(trackSet):
	track_request = requests.get('https://exercism.io' + ref)

	track_soup = BeautifulSoup(track_request.content, 'html.parser')

	overview_section = track_soup.findAll('div', {"class": "overview-section"})

	track_stats = overview_section[0].find_all('h3')

	mentors, students, exercises = track_stats[0].text.split(' ')[0], track_stats[1].text.split(' ')[0], track_stats[2].text.split(' ')[0]

	stats.append(
		{
			'mentors': mentors,
			'students': students,
			'exercises': exercises,
			'track': ref.split('/')[-1].upper()
		}
	)

# 4 - Display table

printFormattedTable(stats)
