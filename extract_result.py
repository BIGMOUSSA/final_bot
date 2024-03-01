import json
import pandas as pd

def reporting(folder, rubrique):
    with open(f"gridresults/{folder}/{rubrique}_report.json", "r") as file :
        report = json.load(file)
    pd.DataFrame(report).to_excel(f"gridresults/{folder}_{rubrique}.xlsx")


if __name__ == "__main__":
    #reporting("config-labse", "intent")
    #reporting("config-labse", "response_selection")
    reporting("config_merge", "intent")
    reporting("config_merge", "response_selection")
    #reporting("config2", "intent")
    #reporting("config2", "response_selection")
    reporting("config3", "intent")
    reporting("config3", "response_selection")
    #reporting("config4", "intent")
    #reporting("config4", "response_selection")
    #reporting("config5", "intent")
    #reporting("config5", "response_selection")
    #reporting("config6", "intent")
    #reporting("config6", "response_selection")
    reporting("config7", "intent")
    reporting("config7", "response_selection")
