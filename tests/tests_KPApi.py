# -*- coding: UTF-8 -*-
__author__ = 'bespontoff'

import os
import unittest

from main import KPApi


class TestKPApi(unittest.TestCase):
    def setUp(self) -> None:
        self.api = KPApi(token=os.environ.get('X_API_KEY'))

    def test_api_films_return_valid_data(self):
        response = self.api.films('301')
        self.assertIn('data', response)
        self.assertEqual(response['data']['filmId'], 301)

    def test_api_films_with_append_to_response_return_valid_data(self):
        response = self.api.films('301', append_to_response='BUDGET, EXTERNAL_ID, RATING, REVIEW, POSTERS')
        self.assertIn('data', response)
        self.assertIn('rating', response)
        self.assertIn('budget', response)
        self.assertIn('review', response)
        self.assertIn('externalId', response)
        self.assertIn('images', response)

    def test_api_films_return_401_with_wrong_token(self):
        api = KPApi('wrong token')
        response = api.films('301')
        self.assertEqual(response['status'], 401)

    def test_api_frames_return_valid_data(self):
        response = self.api.frames('301')
        self.assertIn('frames', response)

    def test_api_frames_return_401_with_wrong_token(self):
        api = KPApi('wrong token')
        response = api.frames('301')
        self.assertEqual(response['status'], 401)

    def test_api_videos_return_valid_data(self):
        response = self.api.videos('301')
        self.assertIn('trailers', response)
        self.assertIn('teasers', response)

    def test_api_videos_return_401_with_wrong_token(self):
        api = KPApi('wrong token')
        response = api.videos('301')
        self.assertEqual(response['status'], 401)

    def test_api_studios_return_valid_data(self):
        response = self.api.studios('301')
        self.assertIn('production', response)
        self.assertIn('filming', response)
        self.assertIn('imageFormat', response)
        self.assertIn('camera', response)
        self.assertIn('copyFormat', response)
        self.assertIn('filmingFormat', response)
        self.assertIn('image', response)
        self.assertIn('language', response)
        self.assertIn('productionStudios', response)
        self.assertIn('specialEffectsStudios', response)
        self.assertIn('dubbingStudios', response)
        self.assertIn('rentStudios', response)

    def test_api_studios_return_401_with_wrong_token(self):
        api = KPApi('wrong token')
        response = api.studios('301')
        self.assertEqual(response['status'], 401)

