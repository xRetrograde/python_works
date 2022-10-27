import flask
import flask_sqlalchemy

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.id
    
    
@app.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return flask.render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post_detail(id):
    post = Post.query.get(id)
    return flask.render_template('post_detail.html', post=post)

@app.route('/post/create', methods=['GET', 'POST'])
def post_create():
    if flask.request.method == 'POST':
        title = flask.request.form['title']
        content = flask.request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return flask.redirect('/')
    return flask.render_template('post_create.html')

@app.route('/post/<int:id>/delete', methods=['POST'])
def post_delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return flask.redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run()