import queue
import time
import random

request_queue = queue.Queue()


def generate_request():
    request_id = random.randint(1, 100)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")


def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"\nЗаявка {request_id} обробляється.")
        time.sleep(1)
        print(f"Заявка {request_id} виконана.\n")
    else:
        print("Черга порожня. Заявок для обробки немає.\n")


while True:
    for _ in range(random.randint(0, 3)):
        generate_request()
    time.sleep(1)
    process_request()
    time.sleep(1)
