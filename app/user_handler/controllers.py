from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app.user_handler.models import User
from app.user_handler.forms import AddUserForm, DeleteUserForm, ChooseActionForm
from app import db

user_handler = Blueprint('user_handler', __name__, url_prefix='/')

@user_handler.route('/', methods=['GET', 'POST'])
def choose_action():
    form = ChooseActionForm(request.form)
    if 'options' in request.form:
        action = request.form['options']
        if action == 'Delete User':
            return redirect('/delete_user/')
        if action == 'Add User':
            return redirect('/add_user/')
    return render_template("user_handler/choose_action.html", form=form)

@user_handler.route('/add_user/', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm(request.form)
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        new_user = User(email=email, name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')

    return render_template("user_handler/add_user.html", form=form)


@user_handler.route('/delete_user/', methods=['GET', 'POST'])
def delete_user():
    form = DeleteUserForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        User.query.filter_by(email=email).delete()
        db.session.commit()
        return redirect('/')
    return render_template("user_handler/delete_user.html", form=form)
