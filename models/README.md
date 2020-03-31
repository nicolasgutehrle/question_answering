# Q&A models

This folder contains different Q&A models in multiple languages. These models were trained using the `run_squad.py` script from Hugging Face. The main goal was to try this library and see how the finetuning process works, so the script was run with the default parameters. 

The English model was finetuned on a `bert-base-uncased` pretrained-model while the French model was finetuned on a `camembert-base` pretrained model, both coming from the Hugging Face repository. The English model was finedtuned on the SQuAD version 2.0 dataset while the French model was finetuned on the FQuAD dataset.

You can look at the finetuning steps for each model in the notebook folder of this repository.
