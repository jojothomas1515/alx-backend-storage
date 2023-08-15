#!/usr/bin/env python3
"""
update documents.
"""

from pymongo.collection import Collection

def update_topics(mongo_collection: Collection, name, topics):
    """
    update topics
    """
    mongo_collection.update_many({'name':name}, {'$set': {'topics': topics}})
