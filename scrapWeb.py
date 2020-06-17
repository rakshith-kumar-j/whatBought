#Importing the Libaries

import requests 
from bs4 import BeautifulSoup

class retrieveProducts:
    def __init__(self):
# Initialising the lists for different aspects of the product
        self.productNames=[]
        self.productRatings=[] 
        self.productImage=[]
        self.productURL=[]

# This function searches for products in lowe's website.
# It takes user input (what product user wants to buy) and searches for the product in Lowe's website.
# We scrape the Lowe's website for relavant tags and retrieve list of products (relavant to user search query) along with their details
# Input: Entity Names extracted from User Search Query
# Output: List of relavant products along with their details (name, Image, product url etc.)

    def sendRequest(self,query):
# Setting the necessary headers
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        searchString=query
        searchString=searchString.replace(" ","+")
        URL = "https://www.lowes.com/search?searchTerm="+searchString
#Getting the Web Page after submitting the Search Query
        r = requests.get(URL,headers=headers) 
        soup = BeautifulSoup(r.content, 'html5lib')

#Accessing the Title of Products displayed in the Web Page after submitting the search query
        for i in range(1,7):
            a = soup.findAll('li',attrs={'class':'js-product-wrapper product-wrapper v-spacing-large art-pl-product-'+str(i)+'-non-pvs position-relative'})
            self.productNames.append(a[0]["data-producttitle"])
        
#Accessing Product Ratings
        for i in range(1,7):
            a = soup.findAll('li',attrs={'class':'js-product-wrapper product-wrapper v-spacing-large art-pl-product-'+str(i)+'-non-pvs position-relative'})
            self.productRatings.append(a[0]["data-productrating"])

#Accessing Product URL
        for i in range(1,7):
            a = soup.findAll('li',attrs={'class':'js-product-wrapper product-wrapper v-spacing-large art-pl-product-'+str(i)+'-non-pvs position-relative'})
            self.productURL.append(a[0]["data-producturl"])

#Accessing Product Image
        for i in range(1,7):
            a = soup.findAll('li',attrs={'class':'js-product-wrapper product-wrapper v-spacing-large art-pl-product-'+str(i)+'-non-pvs position-relative'})
            self.productImage.append(a[0]["data-productimg"])

        for i in range(len(self.productURL)):
            self.productURL[i]="https://lowes.com"+self.productURL[i] 

        return self.productNames,self.productRatings,self.productURL,self.productImage 

