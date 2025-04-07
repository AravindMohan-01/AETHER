from pymongo import MongoClient
import ast
import os
import copy

class Database_update:
    def __init__(self):
        # Mongo DB connection
        mongo_host = 'localhost'
        mongo_port = 27017
        maxSevSelDelay = 1

        if 'MONGO_PORT_27017_TCP_ADDR' in os.environ:
            mongo_host = os.environ['MONGO_PORT_27017_TCP_ADDR']

        if 'MONGO_PORT_27017_TCP_PORT' in os.environ:
            mongo_port = int(os.environ['MONGO_PORT_27017_TCP_PORT'])

        self.client = MongoClient(mongo_host, mongo_port, serverSelectionTimeoutMS=maxSevSelDelay)
        self.db = self.client.apiscan

    def fetch_records(self):
        records = self.db.vulnerabilities.find({})
        if records:
            for data in records:
                data.pop('_id')
                print(data)

    def insert_record(self, data):
        try:
            self.db.vulnerabilities.insert_one(data)
        except Exception as e:
            raise e

    def update_record(self, find, update):
        try:
            self.db.vulnerabilities.update_one(find, update)
        except Exception as e:
            raise e

    def update_scan_record(self, find, update):
        try:
            self.db.scanids.update_one(find, update, upsert=True)
        except Exception as e:
            raise e

    def get_latest_scan_by_url(self, url):
        """
        Fetch any existing scan record for the given URL from the scanids collection.
        """
        try:
            return self.db.scanids.find_one({"url": url})
        except Exception as e:
            print(f"Error while fetching previous scan for URL {url}: {e}")
            return None

    def clone_scan_result(self, old_scanid, new_scanid, url):
        try:
        # Clone scan metadata
            data = self.db.scanids.find_one({"scanid": old_scanid})
            if data:
                data.pop('_id', None)
                data['scanid'] = new_scanid
                data['url'] = url
                if 'total_scan' not in data:
                    data['total_scan'] = 10 
                self.db.scanids.insert_one(data)
                print(f"[i] Reused scan metadata from {old_scanid} to {new_scanid}")

        # ✅ Clone vulnerabilities for this scan
            vulnerabilities = self.db.vulnerabilities.find({"scanid": old_scanid})
            for vuln in vulnerabilities:
                vuln.pop('_id', None)
                vuln['scanid'] = new_scanid
                self.db.vulnerabilities.insert_one(vuln)

            print(f"[i] Cloned vulnerability results from {old_scanid} to {new_scanid}")

        except Exception as e:
            print(f"Error while cloning scan result: {e}")

