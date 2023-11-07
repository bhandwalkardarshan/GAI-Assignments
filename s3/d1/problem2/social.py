from flask import Flask, request, jsonify

app = Flask(__name__)
posts = []  

@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.get_json()
    username = data.get('username')
    caption = data.get('caption')

    if not username or not caption:
        return jsonify({'error': 'Username and caption are required'}), 400

    post = {
        'id': len(posts) + 1,
        'username': username,
        'caption': caption,
    }
    posts.append(post)

    return jsonify({'message': 'Post created successfully', 'post': post}), 201

@app.route('/view_posts', methods=['GET'])
def view_posts():
    return jsonify({'posts': posts})

@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404

    posts.remove(post)
    return jsonify({'message': 'Post deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
