#!/usr/bin/env python3
""" function that returns the list
of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """function"""
    school_topic = []
    query = mongo_collection.find({"topics": topic})
    for school in query:
        school_topic.append(school)
    return school_topic
