#!/usr/bin/env python3

"""Logger."""

from pymongo import MongoClient


def main() -> None:
    """This is the main method."""
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client: MongoClient = MongoClient(host="localhost", port=27017)
    nginx_collection = client.logs.nginx
    total_count: int = nginx_collection.estimated_document_count()
    s_check: int = nginx_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{total_count} logs")
    print("Methods:")
    for i in method:
        method_count: int = nginx_collection.count_documents({"method": i})
        print(f"\tmethod {i}: {method_count}")
    print(f"{s_check} status check")


if __name__ == '__main__':
    main()
