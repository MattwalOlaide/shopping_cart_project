from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@app.route('/api/resource')
@auth.login_required
def get_resource():
	return jsonify({'data':'Email: %s verified!' % g.user.user_email})

@auth.verify_password
def verify_password(email,password):
	#token auth
	user = Users.verify_auth_token(user_email_or_token)
	if not user:
		#use email and password
		user = if User.query.filter_by(user_email = 'new_user_email').first()
		if not user or not user.verify_password(password):
			return False
	g.user = user
	return True