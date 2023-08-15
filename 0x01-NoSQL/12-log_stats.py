#!/usr/bin/env python3

"""
Logger.
"""

from pymongo import MongoClient


method = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def main():
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    nginx_collection = db.nginx
    print(f"{nginx_collection.estimated_document_count()} logs")
    print("Methods")
    for i in method:
        print(
            f'\tmethod {i}: {nginx_collection.count_documents({"method":i})}'
        )
    print("{} status check"
          .format(nginx_collection.count_documents(
              {"method": "GET", "path": "/status"})))


if __name__ == '__main__':
    main()
