import time
import random

def simulate_can_data():
    while True:
        data = [random.randint(0, 255) for _ in range(3)]
        print(f"CAN Data: {data}")
        time.sleep(1)  # Simulate data sending every second

if __name__ == "__main__":
    simulate_can_data()
