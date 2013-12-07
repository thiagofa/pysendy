Pysendy
=======

Pysendy is a Python wrapper for Sendy's API.
Read the LICENSE file before use it.

Installation
------------
    pip install pysendy

Usage
-----
```python
from pysendy import Sendy
s = Sendy(base_url='http://your_sendy_url')

# subscription (name is optional)
s.subscribe(name='John Doe', email='email@to.subscribe', list_id='the_list_id')

# unsubscription
s.unsubscribe(email='email@to.subscribe', list_id='the_list_id')
```
