import os
import pymongo

def get_database(settings):
    """Return Mongo database based on the given settings, also pulling the
    mongo host, port and database form the environment variables if they're not
    defined in the settings.
    """

    uri = settings['HTTPCACHE_MONGODB_URI']
    db = settings['HTTPCACHE_MONGODB_DATABASE']

    return pymongo.MongoClient(uri)[db]

