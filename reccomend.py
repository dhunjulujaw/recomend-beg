movies=[
    {"titles":"Avengers","genre":"Action"},
    {"titles":"IronMan","genre":"Action"},
    {"titles":"Batman","genre":"Action"},
    {"titles":"saiyaraa","genre":"Romance"},
    {"titles":"Titanic","genre":"Romance"},
]

user_like="Romance"

recomendation=[]

for movie in movies:
    if movie["genre"]==user_like:
        recomendation.append(movie["titles"])
        
print(recomendation)