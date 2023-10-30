posts = []
post_id_counter = 1

def create_post(username, caption):
    global post_id_counter  
    post = {"id": post_id_counter, "username": username, "caption": caption}
    posts.append(post)
    post_id_counter += 1  

def view_posts():
    return posts

def delete_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            deleted_post = post
            posts.remove(post)
            return deleted_post
    return None


create_post("User1", "My first post!")
create_post("User2", "Hello, world!")
create_post("User1", "Another post by User1")

all_posts = view_posts()
for post in all_posts:
    print(f"Post {post['id']}: {post['username']} - {post['caption']}")

post_id_to_delete = 1  
deleted_post = delete_post(post_id_to_delete)
if deleted_post:
    print(f"Deleted Post {deleted_post['id']}: {deleted_post['username']} - {deleted_post['caption']}")
else:
    print("Post not found or cannot be deleted.")