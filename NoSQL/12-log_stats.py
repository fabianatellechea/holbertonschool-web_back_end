#!/usr/bin/env python3
"""Python script that provides some stats
about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    mclient = MongoClient("mongodb://127.0.0.1:27017")
    nlogs = mclient.logs.nginx

    print(f"{nlogs.count_documents({})} logs")
    print("Methods:")
    get = nlogs.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get}")
    post = nlogs.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post}")
    put = nlogs.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put}")
    patch = nlogs.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch}")
    delete = nlogs.count_documents({"method": "DELETE"})
    print(f"\tmethod DELETE: {delete}")
    status = nlogs.count_documents({"path": "/status"})
    print(f"{status} status check")
