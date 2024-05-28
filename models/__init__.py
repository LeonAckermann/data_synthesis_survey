#from .PromptRoberta import PromptRoberta
#from .PromptBert import PromptBert
from .goggle.src.goggle.GoggleModel import GoggleModel


model_list = {
    #"PromptRoberta": PromptRoberta,
    #"PromptBert": PromptBert,
    "GOGGLE": GoggleModel,

}

def get_model(model_name):
    if model_name in model_list.keys():
        return model_list[model_name]
    else:
        raise NotImplementedError