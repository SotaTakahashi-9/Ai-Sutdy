import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('DataFrame')

st.write('Display Image')
img = Image.open('AIタイトル.jpg')

st.image(img)