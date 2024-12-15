import random
import os

with open("thinh.txt", "w", encoding='utf-8') as transcript:
    for i in range(200):
        transcript.write(f"Mã số {random.randrange(1, 200)}, khối lượng {round(random.uniform(50, 100), 1)} \n")
        # transcript.write(f"Mã số {random.randint(1, 200)}")