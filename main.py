import streamlit as st
import numpy as np
import pandas as pd
import time
import numpy as np
import time
from qa_models.qa import QuestionAnswering
from transformers import pipeline
import time

@st.cache(allow_output_mutation = True)
def init_model():
    return QuestionAnswering()

def main():
    st.title('Question-Answering systems')
    model = init_model()

    lg_options = st.selectbox('Langue / Language',
                 ('fr', 'en'))


    if lg_options == "en":
        progess_message = "Predicting ..."
        sucess_message = "Done !"
        context = st.text_area(label = "Context :")
        question = st.text_input(label = 'Question :', )
        answer = st.button("Answer")
    else:
        progess_message = "Prédictions en cours ..."
        sucess_message = "Terminé !"

        context = st.text_area(label = "Contexte :")
        question = st.text_input(label = 'Question :', )
        answer = st.button("Répondre")

    if answer:
        with st.spinner(progess_message):
            pred = model.question_answering(question=question, context = context, lg=lg_options)

        st.success(sucess_message)
        st.write(pred['answer'])

if __name__ == "__main__":
    main()