import asyncio
from allora_chain_data import (
    get_latest_inference_block,
    calculate_blocks_from_timeframe,
    collect_inference_data
)


async def get_user_input():
    while True:
        try:
            topic_id = int(input("Enter the topic ID (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the topic ID.")

    print("\nSelect a timeframe:")
    print("1. 1 Hour")
    print("2. 1 Day")
    print("3. 1 Week")
    print("4. 1 Month")

    timeframe_options = {
        "1": "1Hour",
        "2": "1Day",
        "3": "1Week",
        "4": "1Month"
    }

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in timeframe_options:
            timeframe = timeframe_options[choice]
            break
        print("Invalid choice. Please enter a number between 1 and 4.")

    return topic_id, timeframe


async def main():
    print("Allora Network Inference Data Collector\n")

    try:
        topic_id, timeframe = await get_user_input()

        current_block = await get_latest_inference_block(topic_id)
        print(f"\nCurrent block height: {current_block}")

        blocks_to_go_back = calculate_blocks_from_timeframe(timeframe)
        target_block = max(1, current_block - blocks_to_go_back)  # Ensure block doesn't go below 1

        print(f"Calculated block height for {timeframe} ago: {target_block}")

        result = await collect_inference_data(topic_id, target_block)
        print("\nOperation completed successfully!")
        print(result)
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())

