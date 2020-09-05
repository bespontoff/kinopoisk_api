# -*- coding: UTF-8 -*-
__author__ = 'bespontoff'

import os

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


