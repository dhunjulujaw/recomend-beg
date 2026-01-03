movies = [
    {"id": 1, "title": "Avengers", "genres": ["Action", "Sci-Fi"]},
    {"id": 2, "title": "Iron Man", "genres": ["Action", "Sci-Fi"]},
    {"id": 3, "title": "Batman", "genres": ["Action", "Crime"]},
    {"id": 4, "title": "Titanic", "genres": ["Romance", "Drama"]},
    {"id": 5, "title": "Notebook", "genres": ["Romance", "Drama"]},
    {"id": 6, "title": "Interstellar", "genres": ["Sci-Fi", "Drama"]}
]

watched_movie=["Avengers","Batman"] 

user_genre=input("Enter the genre you like : ")

recommend=[]

for movie in movies:
    if user_genre in movie["genres"] and movie['title'] not in watched_movie:
        recommend.append(movie["title"])
        
print("\nRecommendation Movies:")
for movie in recommend:
    print("-",movie)
else:
    print("\nSorry, no movies found for this genre.")