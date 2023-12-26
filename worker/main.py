from src.redis.config import Redis
import asyncio

async def main():
    redis = Redis()
    redis = await redis.create_conection()
    print(redis)
    await redis.set('key', 'value')

if __name__ == '__main__':
    asyncio.run(main())