import streamlit as st
import os
from file_creator import create_files
st.button("Add Files", on_click=create_files, args=(10, "files"))
# display the files
files = os.listdir("files")
st.write(files)
