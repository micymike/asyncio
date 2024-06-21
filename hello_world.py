from asyncflows import AsyncFlows
import asyncio

async def main():
    try:
        # Load the flow from the file
        flow = AsyncFlows.from_file("hello_world.yaml")
        # Run the flow
        result = await flow.set_vars(name="Michael Moses").run()
        # Print the result
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
asyncio.run(main())
