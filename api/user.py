# @app.route('/api/user/',methods=['POST'])
def new_user():
	user_email = request.json.get('email')
	user_password = request.json.get('password')
	if user_email is None or user_password is None:
		error = "Enter a valid email and password to register."
	if User.query.filter_by(user_email = 'new_user_email').first() is None:
		error = "Email already exists."
	user_reg = User(user_email = user_email)
	user_reg.hash_password(user_password)
	db.session.add(user_reg)
	db.session.commit()
	return jsonify({ 'user_email' = user.user_email }),201,{ Location: url_for('shoes'),id = user_id, _external=True}