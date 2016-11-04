# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'ds161295.mlab.com'
MONGO_PORT = 61295

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = 'apitestuser'
MONGO_PASSWORD = ''

MONGO_DBNAME = 'users'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


user_schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 40,
        'required': True,
    },
    'middlename': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'email': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'unique': True,
        'required': True
    },
    'password': {
        # store in plaintext for now. yeah I know
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'long': {'type': 'float'},
            'lat': {'type': 'float'}
        },
    },
    'born': {
        'type': 'datetime',
    },
    'listings': {
        #_id of listings
        'type': 'list',
        'items': {
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 100,
            },
            'description': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 1000,
            },
            'location': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 100,
            },
        },
    }
}

user = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'user',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'email'
    },
    
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    
    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
    
    'schema': user_schema
}

DOMAIN = {'users': user}
