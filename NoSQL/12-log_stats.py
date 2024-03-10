#!/usr/bin/env python3
"""Python script that provides some stats
about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    mclient = MongoClient("mongodb://127.0.0.1:27017")
    collection = mclient.logs.nginx

nlogs = collection.count_documents({})
print(f"{nlogs} logs")
print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for m in methods:
    method = collection.count_documents({"method": m})
    print(f"\tmethod {m}: {method}")
status = collection.count_documents(
    {"method": "GET", "path": "/status"})
print(f"{status} status check")
