#!/usr/bin/env python3
"""
filter by topics.
"""


def schools_by_topic(mongo_collection, topic):
    """
    filter the function by topic.
    """
    return mongo_collection.find({"topics": {"$in": topic}})
