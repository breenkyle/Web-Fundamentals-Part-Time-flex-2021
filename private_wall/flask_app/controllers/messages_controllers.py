from flask import render_template, redirect, session, flash, request
import re
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.message_model import Message
# from flask_bcrypt import Bcrypt


@app.route('/post_message', methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content']
    }
    Message.save(data)
    return redirect('/user_wall')


@app.route('//destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/user_wall')


