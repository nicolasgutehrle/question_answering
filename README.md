# Q&A demo application

This is a small demo application to test Q&A models. These models were trained with the `transformers` library from Hugging Face (more specifically, using the `run_squad.py` script).

At the moment, only two models are available : one in English, the other in French. These models were trained as a way to experiment with the library, thus were trained using the `run_squad` default parameters. Newer and better models may then come along later.

This demo application runs with the *Streamlit* library. You can paste some text and ask a question to which the model will give an answer.

## Install
* Clone this repo in the folder of your choice
* Move into the clone repo and create a virtual environment with `python -m venv venv`
* Install the dependencies using `pip install -r requirements.txt`
* Run the application with `streamlit run main.py`