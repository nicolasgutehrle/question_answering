from transformers import pipeline
import os

class QuestionAnswering():
    def __init__(self):
        # self.fquad = pipeline('question-answering', model='models/camembert_fquad', tokenizer='models/camembert_fquad')
        self.models = self.load_models()

    def load_models(self):
        """
        Return keys : value dictionnary where key is a language code and
        value is the question_answering pipeline associated with it
        :return:
        """
        list_dir = os.listdir('models')
        models = {dir: pipeline('question-answering', model="models/{}".format(dir),
                                tokenizer="models/{}".format(dir)) for dir in list_dir}

        return models

    def question_answering(self, question, context, lg):
        """
        Call Hugging Face question-answering pipeline for given language and returns the answer to the question
        :param question:
        :param context:
        :param lg:
        :return:
        """
        if lg in self.models.keys():
            model = self.models[lg]
            return model(question=question, context=context)
        else:
            return "Please select one of the language available : fr or en"
