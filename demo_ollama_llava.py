# code from ollama documentation
#https://github.com/ollama/ollama-python
import ollama
import sys


def query_image(query: str, image_list: list[str]) -> ollama.chat:
    try:
        res = ollama.chat(
            model='llava-phi3',#'llava:7b-v1.6-vicuna-q2_K', #'llava:7b',
            messages=[
                {
                'role': 'user',
                'content': query,
                'images': image_list,
                }
            ]
        )
    except Exception as e:
        print(f"Error: {e}")
        return None
    return res['message']['content']


import time
import os
for img in os.listdir("images")[:10]:
    img = f"images/{img}"
    start = time.time()
    print(query_image("Precisely count the number of chairs. Answer only with the literal number", [img]))
    print('', query_image("What is the color of the chair? only answer with the color", [img]))
    # display image as 64x64
    display(Image.open(img).resize((64, 64)))
    print(f"Time taken: {time.time()-start}")
    print('')


