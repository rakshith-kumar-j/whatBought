#importing the Libraries

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

class getProductList:
    def __init__(self):
        self.productList=""

#This function returns list of Entity names from the User Input. For example, if the user input is "I want Red Tshirt", this function returns "Red Tshirt" as output
    
    def preprocess(self,sent):
        sent = nltk.word_tokenize(sent)
        sent = nltk.pos_tag(sent)

        for i in sent:
            if i[1]=="NNP" or i[1]=="NN" or i[1]=="NNS" or i[1]=="NNPS" or i[1]=="VBG" or i[1]=="JJ":
                self.productList+=i[0]+" "
        
        return self.productList 






