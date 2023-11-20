def recommend(mem, books):
    ans = []
    for m in mem:
        pref_genre = m["preferred_genre"]
        rec_book = None

        for b in books:
            if b["genre"] == pref_genre:
                rec_book = b["title"] 
                break

        ans.append({"member": m["name"], "book": rec_book})

        return ans
    

members = [
    {"name": "Alice", "preferred_genre": "Mystery"},
    {"name": "Bob", "preferred_genre": "Science Fiction"},
    {"name": "Charlie", "preferred_genre": "Fantasy"},
]

books = [
    {"title": "The Secret Code", "genre": "Mystery"},
    {"title": "Galactic Odyssey", "genre": "Science Fiction"},
    {"title": "Realm of Magic", "genre": "Fantasy"},
    {"title": "Tech Thriller", "genre": "Science Fiction"},
]

recommendations = recommend(members, books)
print(recommendations)