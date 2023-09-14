import requests
import wikipedia
import os
import random


def create_files(count, output):
    for i in range(count):
        title = wikipedia.random(1)
        try:
            p = wikipedia.page(title)
        except wikipedia.DisambiguationError as e:
            random_page = random.choice(e.options)
            text = wikipedia.page(random_page).content
            if not os.path.isdir(output):
                os.mkdir(output)
            with open(os.path.join(output, f"{title}.txt"), "w+", encoding="utf-8") as file:
                file.write(text)