import redis

host = 'localhost'
port = 6379
db = 2

redis_client = redis.Redis(host=host, port=port, db=db)

ttl_seconds = 3600

cursor = '0'
while cursor != 0:
    cursor, keys = redis_client.scan(cursor=cursor, match='*')
    for key in keys:
        redis_client.expire(key, ttl_seconds)
        print(f"TTL: '{key.decode()}'")
