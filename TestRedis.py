import redis


class TestRedis:

    def __init__(self):
        self.my_redis = redis.Redis(host="localhost", port="6379")

    def connect_to_redis(self, host, port):
        try:
            self.my_redis = redis.Redis(host=host, port=port)
        except redis.connection.ConnectionError:
            print("Wrong Host IP or Port entered")
            raise

    def list_all_keys(self):
        keys = self.my_redis.keys()
        for i in range(0, len(keys)):
            keys[i] = keys[i].decode('utf-8')
        return keys

    def get_keys(self, pattern):
        keys = self.my_redis.keys(pattern)
        for i in range(0, len(keys)):
            keys[i] = keys[i].decode('utf-8')
        return keys

    def delete_key(self, key):
        self.my_redis.delete(key)

    def clean_database(self):
        self.my_redis.flushdb()

    def add_key(self, key, value):
        self.my_redis.set(key, value)
