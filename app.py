import os
import sys
from flask import (
	Flask,
	jsonify,
	abort,
	redirect,
	url_for,
	render_template)
from flask import request
import json
from flask_cors import CORS
from database.models import setup_db, Actors, Movies
from auth.auth import AuthError, requires_auth
from helpers import insert_data

# from authlib.integrations.flask_client import OAuth


def create_app(test_config=None):

	app = Flask(__name__)
	setup_db(app)
	CORS(app)

	@app.after_request
	def after_request(response):

		response.headers.add('Access-Conrool-Allow-Headers', 'Content-Type, Authorization, true')
		response.headers.add('Access-Conrool-Allow-Methods', 'GET, POST, PUT, PATCH, OPTION')

		return response

	# database data filter helper

	def actor_helper():
		actors = Actors.query.all()
		all_actors = [actor.format() for actor in actors]
		return all_actors

	def movie_helper():
		movies = Movies.query.all()
		all_movies = [movie.format() for movie in movies]
		return all_movies

	"""Endpoints"""

	@app.route('/')
	def index():
		return jsonify({ 
			"message":"Ok page is working!",
			})

	"""
	It is not a part of API i maded it to make testing easier
	Actully i faced some problems with drop_all() and 
	create_all() commands when i use them in app.py as a
	auto reset database, i tried so many times , i deployed
	this app for heoku for 41 times lol and its becouse of
	this commands, if you have any answer pls reply me
	my email: asqaraliyev01@gmail.com 
	"""
	@app.route('/reset_database', methods=['GET'])
	def reset_database():
		insert_data()
		return redirect(url_for('index'))
	"""---------------------------------------"""
	""" GET endpoint for actors """
	@app.route('/actors', methods = ['GET'])
	def actors():
		try:
			actors = actor_helper()

		except Exception:
			print(sys.exc_info())
			abort(404)
			
		finally:
			return jsonify({
				'success': True,
				'actors': actors,
				})

	""" GET endpoint for movies """
	@app.route('/movies', methods = ['GET'])
	def movies():

		try:
			movies = movie_helper()

		except Exception:
			print(sys.exc_info())
			abort(404)
			
		finally:
			return jsonify({
				'success': True,
				'movies': movies
				})

	""" POST endpoint for actors """
	@app.route('/actors', methods = ['POST'])
	@requires_auth('post:actors')
	def post_actors(jwt):

		body = request.get_json()
		name = body.get('name')
		age = body.get('age')
		gender =  body.get('gender')


		if (name is None) or (age is None) or (gender is None):
			abort(400)

		try:
			new_actor = Actors(
			name = name,
			age = age,
			gender = gender)

			new_actor.insert()
			actor = [new_actor.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'actor': actor
				})

		except Exception:
			print(sys.exc_info())
			abort(422)
			
	""" POST endpoint for movies """
	@app.route('/movies', methods = ['POST'])
	@requires_auth('post:movies')
	def post_movies(jwt):

		body = request.get_json()
		title = body.get('title')
		release_data = body.get('release_data')

		if (title is None) or (release_data is None):
			abort(400)

		try:
			new_movie = Movies(
			title = title,
			release_data = release_data)

			new_movie.insert()
			movie = [new_movie.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'movie': movie
				})

		except Exception:
			print(sys.exc_info())
			abort(422)
			
	""" PATCH endpoint for actors """
	@app.route('/actors/<int:actor_id>', methods = ['PATCH'])
	@requires_auth('patch:actors')
	def patch_actors(jwt, actor_id):

		if not actor_id: 
			abort(404)

		body = request.get_json()
		name = body.get('name')
		age = body.get('age')
		gender = body.get('gender')

		if (name is None) and (age is None) and (gender is None):
			abort(400)

		actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
			
		if actor is None:
			abort(404) 

		try:
			if name:
				actor.name = name
			if age:
				actor.age = age
			if gender:
				actor.gender = gender

			actor.update()
			actor = [actor.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'actor': actor
				})

		except Exception:
			print(sys.exc_info())
			abort(422)
			

	""" PATCH endpoint for movies """
	@app.route('/movies/<int:movie_id>', methods = ['PATCH'])
	@requires_auth('patch:movies')
	def patch_movies(jwt, movie_id):

		if not movie_id: 
			abort(404)

		body = request.get_json()
		title = body.get('title', None)
		release_data = body.get('release_data', None)

		if (title is None) and (release_data is None):
			abort(400)

		movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
		if movie is None:
			abort(404)

		try:
			movie.title = title
			movie.release_data = release_data

			movie.update()
			movie = [movie.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'movie': movie
				})
		except Exception:
			print(sys.exc_info())
			abort(422)

	""" DELETE endpoint for actors """
	@app.route('/actors/<int:actor_id>', methods = ['DELETE'])
	@requires_auth('delete:actors')
	def delte_actors(jwt, actor_id):

		if not actor_id:
			abort(404)

		actor = Actors.query.filter(Actors.id==actor_id).one_or_none()

		if actor is None:
			abort(404)

		try:
			actor = Actors.query.filter(Actors.id==actor_id).one_or_none()

			if actor is None:
				abort(404)

			actor.delete()

			return jsonify({
				'success': True,
				'status_code': 200,
				'deleted': actor_id,
				'message':'deleted successfully'
				})
		except:
			abort(422)

	""" DELETE endpoint for movies """
	@app.route('/movies/<int:movie_id>', methods = ['DELETE'])
	@requires_auth('delete:movies')
	def delte_movies(jwt, movie_id):

		if not movie_id:
			abort(404)

		movie = Movies.query.filter(Movies.id==movie_id).one_or_none()

		if movie is None:
			abort(404)

		try:
			movie.delete()

			return jsonify({
				'success': True,
				'status_code': 200,
				'deleted': movie_id,
				'message':'deleted successfully'
				})
		except:
			abort(422)

	""" ERROR handlers """
	@app.errorhandler(422)
	def unprocessable(error):
	    return jsonify({
	        "success": False,
	        "error": 422,
	        "message": "unprocessable"
	    }), 422

	@app.errorhandler(400)
	def bad_request(error):
	    return jsonify({
	        "success": False,
	        "error": 400,
	        "message": "bad request"
	    }), 400

	@app.errorhandler(404)
	def not_found(error):
	    return jsonify({
	        "success": False,
	        "error": 404,
	        "message": "not found"
	    }), 404

	# auth errorhandlers
	@app.errorhandler(AuthError)
	def auth_error_handler(AuthError):
		return jsonify({
	        		"error": AuthError.status_code,
	        		"message": AuthError.error["description"],
	        		"success": False,
	    			}), AuthError.status_code




	return app