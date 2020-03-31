# Q&A demo application

This is a small demo application to test Q&A models. These models were trained with the `transformers` library from Hugging Face (more specifically, using the `run_squad.py` script).

At the moment, only two models are available : one in English, the other in French. These models were trained as a way to experiment with the library, thus were trained using the `run_squad` default parameters. Newer and better models may then come along later.

This demo application runs with the *Streamlit* library. You can paste some text and ask a question to which the model will give an answer.

## Q&A models

This `models` folder contains different Q&A models in multiple languages. These models were trained using the `run_squad.py` script from Hugging Face. The main goal was to try this library and see how the finetuning process works, so the script was run with the default parameters. 

The English model was finetuned on a `bert-base-uncased` pretrained-model while the French model was finetuned on a `camembert-base` pretrained model, both coming from the Hugging Face repository. The English model was finedtuned on the SQuAD version 2.0 dataset while the French model was finetuned on the FQuAD dataset.

You can look at the finetuning steps for each model in the `notebook` folder of this repository.


## Requirements
* Python >= 3.5

## Install
* Clone this repo in the folder of your choice
* Move into the cloned repo and create a virtual environment with `python -m venv <name-of-environment>
* Activate the environment with source `<name-of-environment>/bin/activate` or `conda activate <name-of-environment>`
* Install the dependencies using `pip install -r requirements.txt`
* Run the application with `streamlit run main.py`
