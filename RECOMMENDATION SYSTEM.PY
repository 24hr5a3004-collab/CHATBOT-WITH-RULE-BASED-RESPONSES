
movies = {
    "Action": ["Avengers", "Batman", "John Wick"],
    "Comedy": ["Mr Bean", "The Mask", "Friends"],
    "Horror": ["Conjuring", "Annabelle", "Nun"]
}

print("Movie Categories:")
print("1. Action")
print("2. Comedy")
print("3. Horror")

choice = input("Enter category: ")

if choice == "Action":
    print("Recommended Movies:")
    for movie in movies["Action"]:
        print(movie)

elif choice == "Comedy":
    print("Recommended Movies:")
    for movie in movies["Comedy"]:
        print(movie)

elif choice == "Horror":
    print("Recommended Movies:")
    for movie in movies["Horror"]:
        print(movie)

else:
    print("Category not found")