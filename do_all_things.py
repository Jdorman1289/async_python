import asyncio


# define the pretend internet co-routine (this is acting like a network call)
async def get_data(delay):
    print("digging up data...")
    # simulate a delay
    await asyncio.sleep(delay)

    print("done!")

    return {"data": "dug up data"}


# define the main co-routine
async def main():
    print("Start of co-routine")

    # asyncio.create_task is used to run the co-routine in parallel
    task1_data = asyncio.create_task(get_data(2))
    task2_data = asyncio.create_task(get_data(2))

    # wait for the co-routine to finish pausing the main thread
    result1 = await task1_data
    result2 = await task2_data

    # this is to show that it won't work in parallel until task is created
    task3_data = asyncio.create_task(get_data(2))
    result3 = await task3_data

    print(f"finished first call to co-routine with result: {result1}")
    print(f"finished second call to co-routine with result: {result2}")
    print(f"finished third call to co-routine with result: {result3}")

    # asyncio.gather is used to run mulitple co-routines in parallel without
    # having to create_task and await each one individually
    all_next_results_list = await asyncio.gather(get_data(2), get_data(2), get_data(2))

    print(f"all next results list: {all_next_results_list}")

    print("End of main co-routine")


# start the co-routine
asyncio.run(main())
