from getProductList import getProductList
from scrapWeb import retrieveProducts

class driver:
    def __init__(self):
        self.productNames=[]
        self.productRatings=[]
        self.productImage=[]
        self.productURL=[] 

    def takeInput(self,query):
        productObj=getProductList()
 #Getting the Entity names from the User's Search Query
 #For example, if user's search query is "I want Red Tshirt", entity names returned by this object will be "Red Tshirt"
        productList=productObj.preprocess(query)
        scrapObj=retrieveProducts()
#Getting the list of products from Lowe's Website which are relavant to Entity Names extracted from User's search query 
        self.productNames,self.productRatings,self.productURL,self.productImage=scrapObj.sendRequest(productList)
        return self.productNames,self.productRatings,self.productURL,self.productImage 

