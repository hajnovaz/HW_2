import csv
import json


movies = []

with open('netflix_titles.tsv', mode='r', encoding='utf-8') as input_file:
    reader=csv.DictReader(input_file, delimiter='\t')

    for line in reader:
        title = line.get('PRIMARYTITLE')
        directors_input = line.get('DIRECTOR')
        cast_input = line.get('CAST')
        genres_input = line.get('GENRES')
        startyear_input = line.get('STARTYEAR')

        directors = []
        if directors_input:
            parts_d = directors_input.split(',')
            for director in parts_d:
                directors.append(director.strip())

        cast = []
        if cast_input:
            parts_c = cast_input.split(',')
            for actor in parts_c:
                cast.append(actor.strip())

        genres = []
        if genres_input:
            genres = genres_input.split(',')
           

        
        if startyear_input:
            year = int(startyear_input)
            decade = (year // 10) * 10
        else:
            decade = None
        
        record={
            'title': title,
            'directors': directors,
            'cast': cast,
            'genres': genres,
            'decade': decade
        }

        movies.append(record)

with open('hw02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(movies, output_file, ensure_ascii= False, indent=4)

