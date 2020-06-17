#importing the Libraraies

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from driver import driver 
from getProductList import getProductList
from getCorrectSpelling import getCorrectSpelling

#initialising Flask 

app = Flask(__name__)
searchTerm=""

#Global list to store the URL's of products sent to users
productURL=[]

#Function to append Product Name, URL Ratings and Image
#l1 corresponds to list of Product Titles
#l2 corresponds to list of Product Ratings
#l3 corresponds to list of Product URL's
#l4 corresponds to list of Product Images

def sendProducts(l1,l2,l3,l4):
    maxSize=0
    if len(l1)>=4:
        maxSize=3 
    else:
        maxSize=len(l1)
    global productURL
    product=""
    for i in range(0,maxSize):
        product+="Name: "+l1[i]+"\n\nRatings: "+l2[i]+"/5\n\nProduct URL: "+l3[i]+"\n"
        productURL.append(l3[i])
    return product,l4[0]

#Routing

@app.route('/bot', methods=['POST','GET'])
def bot():

#Get User Message
    global productURL
    global searchTerm
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False 

#Greetings

    if "hey" in incoming_msg or "hello" in incoming_msg or "hi" in incoming_msg:
        msg.body("Hello There !")
        responded=True

#This is the responce when the User wants to order the product
    if "order" in incoming_msg:
        if len(productURL)>0:
            msg.body("Which product would you like to order ? First one, second one or third one ?")
            responded=True  
        else:
            msg.body("We are Sorry but You haven't browsed for any Products yet") 
            responded=True
    if "first" in incoming_msg or "1" in incoming_msg or "one" in incoming_msg:
        if len(productURL)>0:
            msg.body("Please click the following link to place the order\n\n"+productURL[0])
            responded=True
        else:
            msg.body("We are Sorry but You haven't browsed for any Products yet") 
            responded=True
    if "second" in incoming_msg or "2" in incoming_msg or "two" in incoming_msg:
        if len(productURL)>0:
            msg.body("Please click the following link to place the order\n\n"+productURL[1])
            responded=True
        else:
            msg.body("We are Sorry but You haven't browsed for any Products yet") 
            responded=True
    if "third" in incoming_msg or "3" in incoming_msg or "three" in incoming_msg:
        if len(productURL)>0:
            msg.body("Please click the following link to place the order\n\n"+productURL[2])
            responded=True
        else:
            msg.body("We are Sorry but You haven't browsed for any Products yet") 
            responded=True

#Responce when User wants to know the price of the items

    if "price" in incoming_msg or "prices" in incoming_msg or "cost" in incoming_msg or "costs" in incoming_msg:
        if len(productURL)>0:
            msg.body("Please click the relavant product link to check out the latest prices and customised discounts !") 
            responded=True 
        else:
            msg.body("We are Sorry but You haven't browsed for any Products yet") 
            responded=True

#Response when User wants to see more of the products

    if "more" in incoming_msg:
        if len(searchTerm)>0:
            productObj=getProductList()
            tempProductList=productObj.preprocess(searchTerm)
            tempProductList=tempProductList.replace(" ","+")
            tempProductList=tempProductList[:len(tempProductList)-1]
            msg.body("Please visit https://lowes.com/search?searchTerm="+tempProductList+" for more such amazing products !")
            responded=True
        else:
            msg.body("We are Sorry but You haven't browsed for any Products yet")
            responded=True
    if "list" in incoming_msg or ("see" in incoming_msg and "more" not in incoming_msg and "price" not in incoming_msg) or "have" in incoming_msg or "browse" in incoming_msg or ("show" in incoming_msg and "more" not in incoming_msg and "price" not in incoming_msg) or ("want" in incoming_msg and "price" not in incoming_msg and "order" not in incoming_msg):
    
    #Taking User Query as input and getting product list as output
    #It also stores the User Search Query into CSV file called "customerRequest.csv"
        productURL=[]
        driver1=driver()
        searchTerm=incoming_msg
        productObj=getProductList()
        tempProductList=productObj.preprocess(searchTerm)
        tempProductList=tempProductList.replace(" ","+")
        tempProductList=tempProductList[:len(tempProductList)-1]
        custReq=open('customerRequest.csv','a+') 
        custReq.write(tempProductList+"\n")
        l1,l2,l3,l4=driver1.takeInput(incoming_msg)
        print(l1)
        if len(l1)==0:
            msg.body("We are Sorry. We do not have the products you asked for. We will make a note of it and get back to you once the product is available !\n\n Thank you for using Lowe's")
        print(l1)
        product,productImage=sendProducts(l1,l2,l3,l4)

    #Sending the Product List through WhatsApp

        msg.body(product)
        msg.media(productImage)
        msg.media(l4[1])
        msg.media(l4[2])
        responded=True
    if "thank you" in incoming_msg or "thanks" in incoming_msg:
        msg.body("Your Welcome !")
        responded=True
    
    if not responded:
        driver2=getCorrectSpelling()
        correctStatement=driver2.correctStatement(incoming_msg)
        msg.body(correctStatement)

    return str(resp)

if __name__=="__main__":
    app.run()