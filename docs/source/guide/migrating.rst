Migrating to 1.0
================

Before starting an upgrade, make a backup of your code.

1. Replace `main.py` with the most updated one. Some boilerplate functions
   such as `make_wsgi_app()` were removed and the app is now instantiated
   directly.

2. Some import statements are no longer valid, but there're equivalents for
   all previous functions.

   from tipfy import get_config
   from tipfy import import_string

3. Middleware defined in handlers must be instances. Before::

       class BaseHandler(RequestHandler):
           middleware = [sessions.SessionMiddleware]

   After::

       class BaseHandler(RequestHandler):
           middleware = [sessions.SessionMiddleware()]


Common exceptions
-----------------
**Problem**::

    AttributeError: 'module' object has no attribute 'make_wsgi_app'

**Solution**: Replace `main.py` with the most updated one.

----

**Problem**::

    ImportError: cannot import name get_config

**Solution**: Remove the `from tipfy import get_config` import, and call
get_config from the handler or app instance.

----

**Problem**::

    ImportError: cannot import name import_string

**Solution**: Remove the `from tipfy import import_string` import, and
import it from werkzeug.

----

**Problem**::

    ImportError: cannot import name escape

**Solution**: Remove the `from tipfy import escape` import, and
import it from werkzeug.


----

**Problem**::

    ImportError: cannot import name cached_property

**Solution**: Remove the `from tipfy import cached_property` import, and
import it from werkzeug.

----

**Problem**::

    ImportError: cannot import name redirect

**Solution**: Remove the `from tipfy import redirect` import, and use
`self.redirect` inside a handler.

----

**Problem**::

    ImportError: cannot import name redirect_to

**Solution**: Remove the `from tipfy import redirect_to` import, and use
`self.redirect_to` inside a handler.

----

**Problem**::

    ImportError: cannot import name url_for

**Solution**: Remove the `from tipfy import url_for` import, and use
`self.url_for` inside a handler.

----

**Problem**::

    ImportError: cannot import name cached_property

**Solution**: Remove the `from tipfy import cached_property` import, and
import it from werkzeug.

----

**Problem**::

    ImportError: cannot import name NotFound

**Solution**: use `self.abort(404)` inside handlers.

----

**Problem**::

    ImportError: cannot import name rules

**Solution**: The new `main.py` import the rules list from `urls.py` directly.
If you have a `get_rules()` function in `urls.py`, you can still use it.
Just make the appropriate changes in `main.py`:

**main.py**

.. code-block:: python

   from urls import get_rules

   # ...

   app = Tipfy(config=config, debug=debug)
   app.router.add(get_rules(app))

Alternatively, you can change `urls.py` and replacing the `get_rules()`
function by a simple `rules` list.

----

**Problem**::

    ImportError: cannot import name _slugify

**Solution**: Import it from tipfy.utils.

----

**Problem**::

    ImportError: No module named tipfy.ext.i18n

**Solution**: Replace `from tipfy.ext import i18n` by `from tipfy import i18n`.
The i18n module is now part of tipfy core.

----

**Problem**::

    ImportError: No module named tipfy.ext.auth

**Solution**: Replace `from tipfy.ext import auth` by `from tipfy import auth`.
The auth module is now part of tipfy core.

----

**Problem**::

    ImportError: No module named tipfy.ext.wtforms

**Solution**: Replace `from tipfy.ext import wtforms` by
`from tipfyext import wtforms`. The wtforms module is now part of tipfy core.

----

**Problem**::

    ImportError: No module named tipfy.ext.session

**Solution**: Replace `from tipfy.ext import session` by
`from tipfy import sessions`. The sessions module is now part of tipfy core.

----

**Problem**::

    AttributeError: 'module' object has no attribute 'AllSessionMixins'

**Solution**: Remove `AllSessionMixins` from your code. The sessions module
is now part of tipfy core and available in the `RequestHandler` by default.

----

**Problem**::

    AttributeError: 'module' object has no attribute 'AppEngineAuthMixin'

**Solution**: Remove `AppEngineAuthMixin` from your code. The auth module
is now part of tipfy core and available in the `RequestHandler` by default.

----

**Problem**:: `User` model can't be imported.

**Solution**: Use `from tipfy.appengine.auth.model import User`.

----

**Problem**::

    AttributeError: 'SomeHandlerName' object has no attribute 'auth_current_user'

**Solution**: auth is now an attribute of `RequestHandler`. Inside a handler,
use `self.auth.user` instead.

----

**Problem**::

    AttributeError: 'SomeHandlerName' object has no attribute 'auth_create_user'

**Solution**: auth is now an attribute of `RequestHandler`. Inside a handler,
use `self.auth.create_user` instead.

----

**Problem**::

    AttributeError: 'SomeHandlerName' object has no attribute 'auth_session'

**Solution**: auth is now an attribute of `RequestHandler`. Inside a handler,
use `self.auth.session` instead.

----

**Problem**::

    AttributeError: 'SomeHandlerName' object has no attribute 'auth_login_url'

**Solution**: auth is now an attribute of `RequestHandler`. Inside a handler,
use `self.auth.login_url` instead.

----

**Problem**::

    AttributeError: 'SomeHandlerName' object has no attribute 'auth_logout_url'

**Solution**: auth is now an attribute of `RequestHandler`. Inside a handler,
use `self.auth.logout_url` instead.

----

**Problem**::

    TypeError: logout_url() takes exactly 1 argument (2 given)

**Solution**: pass the redirect argument as keyword: `redirect=some_url`.

----

**Problem**::

    KeyError: "Module 'tipfy' requires the config key 'dev' to be set."

**Solution**: 'dev' is no longer a valid config key, so if you try to use
it this exception will be raised. Use `self.app.debug` inside a handler, or
to check if the dev server is in use import `DEV_APPSERVER` from tipfy.

----

**Problem**::

    KeyError: "Module 'tipfy.sessions' requires the config key 'secret_key' to be set."

**Solution**: set a 'secret_key' in `config.py`:

.. code-block:: python

   config['tipfy.sessions'] = {
       'secret_key': 'important: change this to something very secret!',
   }


AttributeError: 'WikiViewHandler' object has no attribute 'messages'
