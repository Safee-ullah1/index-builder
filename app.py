import streamlit as st
import os
from file_creator import create_files
from indexer import create_index

# create the index
files = []
index = {}
def on_create_index():
    global files
    global index
    if os.path.isdir("files"):
        files = os.listdir("files")
        index = create_index("files", "index.json")
        st.write("Index created")

# search for words
search = st.text_input("Search")
if search:
    if len(index.items()) == 0:
        on_create_index()
    print(search)
    for word in search.split(" "):
        if word in index:
            print(word)
            files_info = index[word]
            file_with_count = {}
            for file_info in files_info:
                if file_info not in file_with_count:
                    file_with_count[file_info] = 0
                file_with_count[file_info] += 1
            for file, count in file_with_count.items():
                st.write(f"{file} - {count}")



st.button("Add Files", on_click=create_files, args=(10, "files"))
# display the files

st.write(files)
