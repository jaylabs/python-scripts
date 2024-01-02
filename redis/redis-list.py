import redis

r = redis.Redis(host='localhost', port=6379, db=0)

keys = r.keys('*')

for key in keys:
    ttl = r.ttl(key)
    memUsage = r.memory_usage(key)
    print(f"Key: {key}, TTL: {ttl} seconds, Memory Usage: {memUsage} bytes")
    
