#!/usr/bin/env python3
"""
function to add item to collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert doc to school.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
