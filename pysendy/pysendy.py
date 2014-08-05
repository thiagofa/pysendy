# -*- coding: utf-8 -*-
from .exceptions import *
import requests

class Sendy(object):

    def __init__(self, base_url, api_key=''):
        self.api_key = api_key
        self.base_url = base_url

    def subscribe(self, name='', email='', list_id='', **fields):
        params = {'name': name, 'email': email, 'list': list_id}
        for key, val in fields.items():
            params.update({key:val})
        self._post('/subscribe', params, SUBSCRIPTION_ERRORS)

    def unsubscribe(self, email='', list_id=''):
        params = {'email': email, 'list': list_id}
        self._post('/unsubscribe', params, UNSUBSCRIPTION_ERRORS)

    def _post(self, path, params, errors):
        url = self.base_url + path
        _params = {'boolean': 'true'}
        _params.update(params)

        try:
            response = requests.post(url, data=_params)
            success = response.text == '1'
        
            if not success:
                try:
                    err = errors[response.text](response.text)
                except KeyError:
                    err = UserException('Failed [' + path + ']: ' + response.text)

                raise err

        except requests.exceptions.RequestException as e:
            raise HttpRequestException(e.message)

        if response.status_code != 200:
            raise HttpRequestException(response.status_code)
