import redis


cache = redis.StrictRedis()

print(cache.ping())
cache.lpush("test_queue", 1)
cache.lpush("test_queue", 2)
cache.lpush("test_queue", 3)

print(cache.blpop("test_queue", timeout=1)[-1])
print(cache.blpop("test_queue", timeout=1)[-1])
