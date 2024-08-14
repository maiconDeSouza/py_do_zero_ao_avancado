films_dict = {
    "name_film": "Top Gun",
    "year_lauch": 2023,
    "review": 9.7,
    "genre": ["Sci-fi", "Action", "Thriller"],
    "plan_included": True
}

print(films_dict)

print(films_dict["name_film"])
print(films_dict.get("name_film"))

print(films_dict.keys())
print(films_dict.values())
print(films_dict.items())

films_dict["director"] = "Dante"

films_dict.update({"preview": 10.00})
print(films_dict)

films_dict.pop("director")
