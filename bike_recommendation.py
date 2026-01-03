from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select database
db = client["bike_recommender"]

# Select collection
bikes_collection = db["bikes"]


bikes = [
    {"id": 1, "name": "Yamaha MT-15", "genres": ["Naked", "Street"]},
    {"id": 2, "name": "KTM Duke 200", "genres": ["Naked", "Street"]},
    {"id": 3, "name": "KTM Duke 390", "genres": ["Naked", "Performance"]},
    {"id": 4, "name": "Bajaj Pulsar NS200", "genres": ["Naked", "Street"]},
    {"id": 5, "name": "TVS Apache RTR 200", "genres": ["Naked", "Performance"]},

    {"id": 6, "name": "Yamaha R15", "genres": ["Sport", "Racing"]},
    {"id": 7, "name": "KTM RC 200", "genres": ["Sport", "Racing"]},
    {"id": 8, "name": "KTM RC 390", "genres": ["Sport", "Racing"]},
    {"id": 9, "name": "Kawasaki Ninja 300", "genres": ["Sport", "Racing"]},
    {"id": 10, "name": "Kawasaki Ninja 400", "genres": ["Sport", "Racing"]},

    {"id": 11, "name": "Royal Enfield Classic 350", "genres": ["Cruiser", "Touring"]},
    {"id": 12, "name": "Royal Enfield Bullet 350", "genres": ["Cruiser"]},
    {"id": 13, "name": "Royal Enfield Meteor 350", "genres": ["Cruiser", "Touring"]},
    {"id": 14, "name": "Bajaj Avenger 220", "genres": ["Cruiser"]},
    {"id": 15, "name": "Harley Davidson Street 750", "genres": ["Cruiser"]},

    {"id": 16, "name": "Royal Enfield Himalayan", "genres": ["Adventure", "Touring"]},
    {"id": 17, "name": "KTM Adventure 250", "genres": ["Adventure", "Off-road"]},
    {"id": 18, "name": "KTM Adventure 390", "genres": ["Adventure", "Off-road"]},
    {"id": 19, "name": "BMW G 310 GS", "genres": ["Adventure", "Touring"]},
    {"id": 20, "name": "Suzuki V-Strom 250", "genres": ["Adventure", "Touring"]},

    {"id": 21, "name": "Hero Splendor Plus", "genres": ["Commuter", "Mileage"]},
    {"id": 22, "name": "Honda Shine", "genres": ["Commuter", "Mileage"]},
    {"id": 23, "name": "Bajaj Platina", "genres": ["Commuter", "Mileage"]},
    {"id": 24, "name": "TVS Raider", "genres": ["Commuter", "Street"]},
    {"id": 25, "name": "Hero Glamour", "genres": ["Commuter"]},

    {"id": 26, "name": "Honda Activa", "genres": ["Scooter", "Automatic"]},
    {"id": 27, "name": "TVS Jupiter", "genres": ["Scooter", "Automatic"]},
    {"id": 28, "name": "Suzuki Access 125", "genres": ["Scooter", "Automatic"]},
    {"id": 29, "name": "TVS Ntorq", "genres": ["Scooter", "Performance"]},
    {"id": 30, "name": "Yamaha Ray ZR", "genres": ["Scooter", "Street"]},

    {"id": 31, "name": "BMW S 1000 RR", "genres": ["Sport", "Superbike"]},
    {"id": 32, "name": "Ducati Panigale V2", "genres": ["Sport", "Superbike"]},
    {"id": 33, "name": "Kawasaki Ninja ZX-10R", "genres": ["Sport", "Superbike"]},
    {"id": 34, "name": "Honda CBR 650R", "genres": ["Sport", "Performance"]},
    {"id": 35, "name": "Suzuki Hayabusa", "genres": ["Sport", "Touring"]},

    {"id": 36, "name": "Jawa 42", "genres": ["Cruiser", "Retro"]},
    {"id": 37, "name": "Jawa Perak", "genres": ["Cruiser", "Bobber"]},
    {"id": 38, "name": "Benelli Imperiale 400", "genres": ["Cruiser", "Retro"]},
    {"id": 39, "name": "Honda CB 350", "genres": ["Cruiser", "Touring"]},
    {"id": 40, "name": "Yezdi Roadster", "genres": ["Cruiser"]},

    {"id": 41, "name": "Hero Xpulse 200", "genres": ["Adventure", "Off-road"]},
    {"id": 42, "name": "Suzuki Gixxer SF", "genres": ["Sport", "Street"]},
    {"id": 43, "name": "Yamaha FZ-S", "genres": ["Naked", "Street"]},
    {"id": 44, "name": "TVS Apache RR 310", "genres": ["Sport", "Racing"]},
    {"id": 45, "name": "BMW G 310 R", "genres": ["Naked", "Performance"]},

    {"id": 46, "name": "Triumph Street Triple", "genres": ["Naked", "Performance"]},
    {"id": 47, "name": "Triumph Bonneville", "genres": ["Cruiser", "Retro"]},
    {"id": 48, "name": "Kawasaki Z900", "genres": ["Naked", "Superbike"]},
    {"id": 49, "name": "Honda Rebel 500", "genres": ["Cruiser"]},
    {"id": 50, "name": "CFMoto 300NK", "genres": ["Naked", "Street"]}
]


if bikes_collection.count_documents({}) == 0:
    bikes_collection.insert_many(bikes)


user_input = input("Enter the bike type you like (comma separated): ")

# convert user input to lowercase
user_genres = [genre.strip().lower() for genre in user_input.split(",")]


recommend = []

for bike in bikes_collection.find():
    match_count = 0

    # convert bike genres to lowercase
    bike_genres = [g.lower() for g in bike["genres"]]

    for genre in user_genres:
        if genre in bike_genres:
            match_count += 1

    if match_count > 0:
        recommend.append({
            "name": bike["name"],
            "score": match_count
        })


recommend.sort(key=lambda x: x["score"], reverse=True)


print("\nRecommended Bikes (Ranked):")
for bike in recommend:
    print(f"- {bike['name']} (Match Score: {bike['score']})")