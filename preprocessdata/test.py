from data_cleaning import data_extraction
import json

with open(r'..\preprocessdata\response.json', 'r') as fh: 
    datapoints=json.load(fh)
#print(type(datapoints))

datastring=json.dumps(datapoints)
#print(type(datastring))

retrieve_data=data_extraction.remove_regex_pattern(datastring,True)
#print(retrieve_data)

retrieve_tokens=data_extraction.generate_tokens(retrieve_data)
#print(retrieve_tokens)

retrieve_corpus=data_extraction.create_corpus(retrieve_tokens)
print(retrieve_corpus)
