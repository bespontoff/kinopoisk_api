# -*- coding: UTF-8 -*-
__author__ = 'bespontoff'

import requests

BASE_URL = 'https://kinopoiskapiunofficial.tech/api/'
V1 = 'v1/'
V2 = 'v2.1/'


class KPApi:
    def __init__(self, token):
        self._token = token
        self._headers = {'X-API-KEY': self._token}

    def films(self, id, append_to_response=''):
        response = requests.get(BASE_URL + V2 + f'films/{id}',
                                params={'append_to_response': append_to_response},
                                headers=self._headers)
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def frames(self, id):
        response = requests.get(BASE_URL + V2 + f'films/{id}/frames',
                                headers=self._headers)
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def videos(self, id):
        response = requests.get(BASE_URL + V2 + f'films/{id}/videos',
                                headers=self._headers)
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def studios(self, id):
        response = requests.get(BASE_URL + V2 + f'films/{id}/studios',
                                headers=self._headers)
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def search_by_keyword(self, keyword, page=1):
        response = requests.get(BASE_URL + V2 + f'films/search-by-keyword',
                                headers=self._headers,
                                params={'keyword': keyword, 'page': page})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def filters(self):
        response = requests.get(BASE_URL + V2 + f'films/filters',
                                headers=self._headers)
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def search_by_filters(self,
                          country='',
                          genre='',
                          order='RATING',
                          rating_from=0,
                          rating_to=10,
                          year_from=1988,
                          year_to=2020,
                          page=1):
        response = requests.get(BASE_URL + V2 + f'films/search-by-filters',
                                headers=self._headers,
                                params={'country': country,
                                        'genre': genre,
                                        'order': order,
                                        'ratingFrom': rating_from,
                                        'ratingTo': rating_to,
                                        'yearFrom': year_from,
                                        'yearTo': year_to,
                                        'page': page})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def top(self, type_='BEST_FILMS_LIST', page=1, list_id=1):
        response = requests.get(BASE_URL + V2 + f'films/top',
                                headers=self._headers,
                                params={'type': type_, 'page': page, 'listId': list_id})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def releases(self, year, month, page=1):
        response = requests.get(BASE_URL + V2 + f'films/releases',
                                headers=self._headers,
                                params={'year': year, 'month': month, 'page': page})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def reviews(self, id, page=1):
        response = requests.get(BASE_URL + V1 + f'reviews',
                                headers=self._headers,
                                params={'filmId': id, 'page': page})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def review_details(self, id):
        response = requests.get(BASE_URL + V1 + f'reviews/details',
                                headers=self._headers,
                                params={'reviewId': id})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def staff(self, id):
        response = requests.get(BASE_URL + V1 + f'staff',
                                headers=self._headers,
                                params={'filmId': id})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}

    def collections(self, list_type='BEST_FILMS_LIST', list_id=0):
        response = requests.get(BASE_URL + V1 + f'collections/films',
                                headers=self._headers,
                                params={'listType': list_type, 'listId': list_id})
        if response.status_code in [200, 401, 429]:
            return response.json()
        return {'code': response.status_code, 'error': 'External api error'}
