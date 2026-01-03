movies = [
    {"id": 1, "title": "Avengers", "genres": ["Action", "Sci-Fi"]},
    {"id": 2, "title": "Iron Man", "genres": ["Action", "Sci-Fi"]},
    {"id": 3, "title": "Batman", "genres": ["Action", "Crime"]},
    {"id": 4, "title": "Titanic", "genres": ["Romance", "Drama"]},
    {"id": 5, "title": "Notebook", "genres": ["Romance", "Drama"]},
    {"id": 6, "title": "Interstellar", "genres": ["Sci-Fi", "Drama"]}
]

watched_movie=["Avengers","Batman"] 

user_input=input("Enter the genre you like : ")
user_genre=user_input.split(",")
user_genre=[genre.strip() for genre in user_genre]#
"""" “For every genre inside user_genres,
remove spaces using strip(),
and collect the results into a new list.”"""

recommend=[]

for movie in movies:
    match_count=0
    
    for genre in user_genre:
        if genre in movie["genres"]:
            match_count +=1
    
    if match_count>0:
        recommend.append({
            "title":movie["title"],
            "score":match_count
        })
        
#now sorting movies wrt Score
recommend.sort(key=lambda x: x["score"],reverse=True)
"""key → sort using "score"

reverse=True → highest score first"""

print("\nRecommended Movies (Ranked):")
for movie in recommend:
    print(f"- {movie['title']} (Match Score: {movie['score']})")
