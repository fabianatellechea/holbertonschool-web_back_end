#!/usr/bin/env python3
"""Python function that inserts a new document
in a collection based on kwargs """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function """
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
