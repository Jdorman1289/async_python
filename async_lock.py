import asyncio

# this could be a parquet file, a database, etc.
shared_data = 0

# this is the lock that will be used to synchronize access to the shared data
lock = asyncio.Lock()


async def add_to_shared_data():
    global shared_data
    # telling it to use the lock
    async with lock:
        print("adding to shared data")
        shared_data += 1
        await asyncio.sleep(1)
        print(f"new shared data state: {shared_data}")


async def main():
    # multiple calls to the shared data
    await asyncio.gather(
        add_to_shared_data(), add_to_shared_data(), add_to_shared_data()
    )


asyncio.run(main())
