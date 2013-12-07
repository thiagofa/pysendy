# -*- coding: utf-8 -*-
class SendyException(Exception): pass
class UserException(SendyException): pass
class HttpRequestException(SendyException): pass

class InvalidEmailAddressException(UserException): pass
class AlreadySubscribedException(UserException): pass
class SomeFieldsAreMissingException(UserException): pass

class InvalidListIdException(SendyException): pass

SUBSCRIPTION_ERRORS = {
    'Already subscribed.': AlreadySubscribedException,
    'Invalid email address.': InvalidEmailAddressException,
    'Some fields are missing.': SomeFieldsAreMissingException,
    'Invalid list ID.': InvalidListIdException,
}

UNSUBSCRIPTION_ERRORS = {
	'Some fields are missing.': SomeFieldsAreMissingException,
	'Invalid email address.': InvalidListIdException,
}