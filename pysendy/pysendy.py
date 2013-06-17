# -*- coding: utf-8 -*-
from .exceptions import *
import requests

class Sendy(object):

    def __init__(self, base_url, api_key=''):
        self.api_key = api_key
        self.base_url = base_url

    def subscribe(self, name='', email='', list_id=''):
        url = self.base_url + '/subscribe'
        params = {'name': name, 'email': email, 'list': list_id, 'boolean': 'true'}

        try:
            response = requests.post(url, data=params)
            subscribed = response.text == '1'
        
            if not subscribed:
                try:
                    err = SUBSCRIPTION_ERRORS[response.text](response.text)
                except KeyError:
                    err = UserException('Not subscribed: ' + response.text)

                raise err

        except requests.exceptions.RequestException as e:
            raise HttpRequestException(e.message)

        if response.status_code != 200:
            raise HttpRequestException(response.status_code)
