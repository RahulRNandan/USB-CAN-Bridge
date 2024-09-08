import threading
import queue
import time

usb_data_queue = queue.Queue()
can_data_queue = queue.Queue()

def usb_to_can_bridge():
    while True:
        if not usb_data_queue.empty():
            data = usb_data_queue.get()
            print(f"Forwarding data to CAN: {data}")
            can_data_queue.put(data)
        time.sleep(0.1)

def can_to_usb_bridge():
    while True:
        if not can_data_queue.empty():
            data = can_data_queue.get()
            print(f"Forwarding data to USB: {data}")
            usb_data_queue.put(data)
        time.sleep(0.1)

if __name__ == "__main__":
    threading.Thread(target=usb_to_can_bridge, daemon=True).start()
    threading.Thread(target=can_to_usb_bridge, daemon=True).start()

    # Simulate incoming USB data
    while True:
        data = [1, 2, 3]
        usb_data_queue.put(data)
        time.sleep(1)
