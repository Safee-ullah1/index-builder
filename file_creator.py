import requests
import wikipedia
import os
from random import randint


def create_files(count, output):
    for i in range(count):
        title = wikipedia.random(1)
        text = wikipedia.page(title).content
        if not os.path.isdir(output):
            os.mkdir(output)
        with open(os.path.join(output, f"{title}.txt"), "w+", encoding="utf-8") as file:
            file.write(text)