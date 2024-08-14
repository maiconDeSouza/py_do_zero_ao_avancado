import pprint
films_dict = {
    "Top Gun": {
        "year_lauch": 2023,
        "review": 9.7,
        "genre": ["Sci-fi", "Action", "Thriller"],
        "plan_included": True
    },
    "interstellar": {
        "year_lauch": 2014,
        "review": 8.6,
        "genre": ["Sci-fi", "Drama"],
        "plan_included": True
    }

}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(films_dict)
print(films_dict["Top Gun"]["genre"])

films_dict["Top Gun"]["director"] = "Fulano"
del films_dict["interstellar"]
pp = pprint.PrettyPrinter(depth=4)
