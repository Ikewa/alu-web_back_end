#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def main(collection):
    """ Log stats """
    num_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    num_status_check = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{num_logs} logs")
    print("Methods:")
    for method in methods:
        num_method = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {num_method}")
    
    print(f"{num_status_check} status check")

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    logs = db.nginx
    main(logs)
