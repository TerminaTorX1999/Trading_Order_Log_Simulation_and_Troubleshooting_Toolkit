import random
import datetime

STATUSES = ["NEW", "ACK", "FILL", "CANCEL"]

def random_time(base):
    return base + datetime.timedelta(seconds=random.randint(1, 300))


def generate_logs(n=1000):
    base_time = datetime.datetime(2026, 3, 25, 10, 0, 0)

    with open("logs.txt", "w") as f:
        for i in range(1, n + 1):
            order_id = i
            t = base_time

            # NEW
            t = random_time(t)
            f.write(f"ORDER_ID={order_id} STATUS=NEW TIME={t}\n")

            # ACK
            t = random_time(t)
            f.write(f"ORDER_ID={order_id} STATUS=ACK TIME={t}\n")

            # Randomly decide fill or cancel
            if random.random() > 0.2:
                t = random_time(t)
                f.write(f"ORDER_ID={order_id} STATUS=FILL TIME={t}\n")
            else:
                t = random_time(t)
                f.write(f"ORDER_ID={order_id} STATUS=CANCEL TIME={t}\n")


if __name__ == "__main__":
    generate_logs(1000)
