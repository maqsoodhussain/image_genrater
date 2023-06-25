import streamlit as st
import openai
import requests
import PIL
import io
from PIL import Image

st.set_page_config (
        page_title="Image generater using Ai",
        page_icon="imag.png"
    )


openai.api_key=""


def image_gen(text):
    responce = openai.Image.create(
        prompt =f"{text}",
        n=1,
        size = "1024x1024"
    )
    image_url = responce.data[0]['url']

    image_content = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_content))
    return image

#prompt = "car in mars with man"
#img = image_gen(prompt)

st.title("WRITE TEXT AND AI WILL GENERATE IMAGE OF THAT TEXT")

# model = 'gpt-3.5-turbo'
# st.text(model)
prompt= st.text_input("ENTER TEXT:", value ="pink dog in water") 

if st.button('Submit'):
    #we create a spinner that continues runs and get responce
    with st.spinner('processing in Progress Wait...... '):
        img = image_gen(prompt)
        st.write("Created By: MAQSOOD HUSSAIN WANI")
        st.success("SUCCESSFULLY GENERATED : ")
        st.image(img)





#footer
st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            color: #6c757d;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            CREATED BY MAQSOOD HUSSAIN WANI
        </div>
        """,True
    
    )

