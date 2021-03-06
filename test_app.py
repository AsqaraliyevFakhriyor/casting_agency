import os
from app import create_app
from database.models import setup_db, Movies, Actors
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

""" i imported this function there 
becouse GIT freezed when i 
runned this file when i use it 
from another file """

test_actor = Actors(
    name='Mark',
    age='32',
    gender='male')

test_movie = Movies(
    title='Alone in Mars',
    release_data='14.07.2045')

class CapstoneTest(unittest.TestCase):
    def setUp(self):

        DB_PATH = os.getenv('DATABASE_URL_TEST')
        praducer_token = os.getenv("PRODUCER_TOKEN")
        director_token = os.getenv("DIRECTOR_TOKEN")

        self.app = create_app()
        self.client = self.app.test_client
        self.praducer_token = praducer_token
        self.director_token = director_token
        self.test_actor_data = {"name": "Emerson", "age": 20, "gender":"male"}
        self.test_movie_data = {"title": "Avatar", "release_data":"20.09.2021"}

        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass


    """ TEST for ACTOES endpoints """ 
    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_post_actor(self):
        response = self.client().post('/actors',
            json=self.test_actor_data,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'][0]['name'], 'Emerson')
        self.assertEqual(data['actor'][0]['age'], 20)
        self.assertEqual(data['actor'][0]['gender'], 'male')

    def test_post_actor_400(self):
        response = self.client().post('/actors',
            json={},
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_post_actor_unauthorized_401(self):
        response = self.client().post('/actors',
            json=self.test_actor_data)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header expected')

    def test_patch_actor(self):
        new_actor = {"name": "Lily", "age": 19, "gender": "female"}
        response = self.client().patch('/actors/1',
            json=new_actor,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        data_actor = data['actor'][0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data_actor['name'], 'Lily')
        self.assertEqual(data_actor['age'], 19)
        self.assertEqual(data_actor['gender'], 'female')

    def test_patch_actor_400(self):
        response = self.client().patch('/actors/1',
            json={},
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_patch_actor_unauthorized_401(self):

        new_actor = {"name": "Lily", "age": 19, "gender": "female"}
        response = self.client().patch('/actors/1',json=new_actor)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header expected')

    def test_patch_actor_404(self):
        response = self.client().patch('/actor/1000',
            json=new_actor,
            headers={'Authorization': f'Bearer {self.praducer_token}'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'not found')


    def test_delete_actor(self):
        test_actor.insert()
        response = self.client().delete(f'/actors/{test_actor.id}',
            headers={'Authorization': f'Bearer {self.director_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertEqual(data['deleted'], test_actor.id)

    def test_delete_actor_401(self):
        response = self.client().delete('/actors/3')

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header expected')

    def test_delete_actor_404(self):
        response = self.client().delete('/actors/1000',
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'not found')


    """ TEST for MOVIES endpoints"""
    
    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_post_movie(self):
        response = self.client().post('/movies',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie'][0]['title'], 'Avatar')
        self.assertEqual(data['movie'][0]['release_data'],'20.09.2021')

    def test_post_movie_400(self):
        response = self.client().post('/movies', 
            json={}, 
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    
    def test_post_movie_unauthorized_401(self):
        response = self.client().post('/movies',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.director_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'To complate command permission needed')

    def test_patch_movie(self):
        response = self.client().patch('/movies/1',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        data_movie = data['movie']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data_movie[0]['title'], 'Avatar')
        self.assertEqual(data_movie[0]['release_data'],'20.09.2021')

    def test_patch_movie_400(self):
        response = self.client().patch('/movies/2',
            json={},
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_delete_movie(self):

        test_movie.insert()
        response = self.client().delete(f'/movies/{test_movie.id}',
            headers={'Authorization': f'Bearer {self.praducer_token}'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertEqual(data['deleted'], test_movie.id)

    def test_delete_movie_401(self):

        response = self.client().delete(f'/movies/4',
            headers={'Authorization': f'Bearer {self.director_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'To complate command permission needed')

    def test_delete_movie_404(self):
        response = self.client().delete('/movies/10000',
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

if __name__ == "__main__":
    unittest.main()