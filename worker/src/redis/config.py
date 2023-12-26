import os
from dotenv import load_dotenv
import aioredis

load_dotenv()

class Redis():

    def __init__(self):
        """Initialize connection"""
        self.REDIS_URL = os.getenv('REDIS_URL')
        self.REDIS_USER = os.getenv('REDIS_USER')
        self.REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
        self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"
    
    async def create_conection(self):
        self.connection = aioredis.from_url(self.connection_url, db=0)

        return self.connection