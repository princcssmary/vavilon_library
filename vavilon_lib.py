import random
import text_for_lib
import os

path_to_papka = "C:\\Users\\Admin\\Desktop\\проги для проги\\доп задания"

for dir_name in range(10):
    path = os.path.join(path_to_papka, str(dir_name))
    os.mkdir(path)
    for filename in range(10):
        filepath = os.path.join(path, str(filename) + ".txt")
        with open(filepath, "w+") as f:
            a = text_for_lib.generate_text(random.randint(1,7))
            f.write(a)

