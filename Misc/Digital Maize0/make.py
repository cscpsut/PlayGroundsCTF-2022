import os
import uuid
import random

flag_position = random.randint(0, 100 * 10)

if flag_position < (1000) // 2:
    flag_position = flag_position + (1000) // 2

flag = ("CSCCTF{" + str(uuid.uuid4()) + "}").encode()
counter = 0
os.mkdir("dCORN")


for b in range(0, 100):
    b_directory = str(uuid.uuid4())
    b_parent_dir = "./dCORN/" + "/"
    path = os.path.join(b_parent_dir, b_directory)
    os.mkdir(path)

    for c in range(0, 10):
        c_directory = str(uuid.uuid4())
        c_parent_dir = "./dCORN/" + b_directory + "/"
        path = os.path.join(c_parent_dir, c_directory)
        os.mkdir(path)
        for d in range(0, 1):
            counter = counter + 1
            if counter == flag_position:
                f = open(
                    path + "/" + str(uuid.uuid4()) + ".txt",
                    "wb",
                ).write(flag)
                print(f"flag inserted in {c_parent_dir}/{str(uuid.uuid4())}.txt")

print(counter)
