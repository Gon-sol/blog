
from flask import render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user

from forms import PostForm, RegisterForm, LoginForm
from models import Post, User
from ext import app, db


@app.route("/")
def main():
    posts = Post.query.all()
    user = current_user
    return render_template("main.html", posts = posts, user=user)

@app.route("/main")
def main2():
    posts = Post.query.all()
    user = current_user
    return render_template("main.html", posts = posts, user=user)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    user_already_exists = False
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is None:
            new_user = User(username=form.username.data, password=form.password.data, role=form.role.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        else:
            user_already_exists = True
    else:
        print(form.errors)
    return render_template("register.html", form=form, user_already_exists=user_already_exists)

@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user != None and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    else:
        print(form.errors)
    return render_template("log_in.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/post")
def no_post_selected_page():
    posts = Post.query.all()
    return render_template("main.html", posts = posts)

@app.route("/post/<post_key>")
def posts_page(post_key):
    post = Post.query.get(post_key)
    return render_template("post.html", post = post)

@app.route("/create_post", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, description=form.description.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)
    return render_template("create_post.html", form=form)

@app.route('/delete/<int:item_id>', methods=['POST', 'GET'])
def delete(item_id):
    item_to_delete = Post.query.get(item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect("/")
