import os
import json
import re

regex_type_dict={}
corpus_freq={}
extracted_text=''
tokenized_text=[]

stop_file=open("..\preprocessdata\data_cleaning\stopwords_english").read().lower()
stopwords=stop_file.split()
punctuations = """!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~"""

digits = re.compile('\d+')
email_reg = re.compile('([a-z0-9.-_]+[@][a-z0-9-]+[\.]*[a-z]*|[\w.-]+@+[\w.]+.+[\w.])')
phone_reg = re.compile('(\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]?\d{4}|\d{3}[-\.\s]?\d{4})')
#url_reg=''
time_reg = re.compile('\d{2}:\d{2}[:]*[\d{2}]* [am|pm]*')
date_reg = re.compile('(\d{1,2}[\./-]\d{1,2}[\./-]\d{4}|\d{1,2} [adfjmnos]\w* \d{4}|[adfjmnos]\w* \d{1,2}[,]\d{2,4})')

def remove_regex_pattern(string_text, replace=False):
    regex_type_dict['NUM']=digits.findall(string_text)      #extract all the regex patterns from the input and store it in a dictionary
    regex_type_dict['EMAIL']=email_reg.findall(string_text) #returns the list of all the matches given the regex patterns from the input string
    regex_type_dict['PHONE']=phone_reg.findall(string_text) # and store it in a dictionary as a value for the related property type as a key
    #regex_type_dict['URL']=url_reg.findall(string_text)
    regex_type_dict['TIME']=time_reg.findall(string_text)
    regex_type_dict['DATE']=date_reg.findall(string_text)

    if replace==True:                                 #if replace is true, then patterns will be replaced by the given text
        extracted_text = email_reg.sub('EMAIL', string_text)
        extracted_text = phone_reg.sub('PHONE', extracted_text)
        #extracted_text = url_reg.sub('URL', extracted_text)
        extracted_text = time_reg.sub('TIME', extracted_text)
        extracted_text = date_reg.sub('DATE', extracted_text)
        extracted_text=digits.sub('NUM',extracted_text)

    else:                                             # or else it will just remove it.
        extracted_text = email_reg.sub(" ", string_text)
        extracted_text = phone_reg.sub(" ", extracted_text)
        #extracted_text = url_reg.sub(" ", extracted_text)
        extracted_text = time_reg.sub(" ", extracted_text)
        extracted_text = date_reg.sub(" ", extracted_text)
        extracted_text = digits.sub(" ", extracted_text)


    return extracted_text

def generate_tokens(string_text):  #creates a list of words based on the string input after removing stopwords and punctuations.
    for punctuation in punctuations:
        string_text = string_text.replace(punctuation, " ")
    tokens = string_text.split() #Not converting to lower case if a text prerprocesed by regex_operation may contain a capital replaced text.
    tokenized_text=[token for token in tokens if token not in stopwords]
    return tokenized_text

def create_corpus(token_list, threshold=50):
    token_freq={}           #dictionary containing all the tokens with their word counts
    for word in token_list:
        if word not in token_freq:
            token_freq[word]=1
        token_freq[word]+=1
    corpus_freq={word:count for word, count in token_freq.items() if count> threshold} #dictionary storing only the deduced vocabulary and its count based on parameters
    return corpus_freq

#adding modules as comment for review

#def generate_ngrams(string_list,N):
    #grams = [string_list[i:i + N] for i in range(len(string_list)-N+1)]
    #return grams

#def normalise():  'as mentioned in document to have an option of stemming and lemmatization'


















