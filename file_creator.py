import requests
import wikipedia
import os
import random


def create_files(count, output):
    for i in range(count):
        title = wikipedia.random(1)
        is_error = True
        page = ""
        while is_error:
            try:
                page = wikipedia.page(
                    title, auto_suggest=False, redirect=True, preload=False)
                is_error = False
            except wikipedia.DisambiguationError as e:
                continue
            if not os.path.isdir(output):
                os.mkdir(output)
            with open(os.path.join(output, f"{title}.txt"), "w+", encoding="utf-8") as file:
                file.write(page)
