from flask import Flask, render_template

app = Flask(__name__)

profile = {
    'name': '깽깽이풀',
    'title': '초보개발자',
    'bio': '안녕하세요, 파이썬을 공부중입니다',
    'email': 'ratna7@naver.com',
}

posts = [
    {
        'id': 1,
        'title': '첫 번째 블로그 포스트',
        'date': '2026-05-11',
        'category': '일상',
        'summary': 'Flask로 개인 블로그를 만들었습니다. 신기합니다.',
        'content': 'Flask로 개인 블로그를 만들었습니다. 흥미롭습니다.',
    },
    
]

@app.route('/')
def index():
    return render_template('index.html', profile=profile, posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    p = next((p for p in posts if p['id'] == post_id), None)
    if p is None:
        return '포스트를 찾을 수 없습니다.', 404
    return render_template('post.html', profile=profile, post=p)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
