#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """ function"""
    return mongo_collection.find()
