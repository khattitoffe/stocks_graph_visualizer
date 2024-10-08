import numpy as np
import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

class stocks():
 def get_data(stock,period):
  
   stockdata=pd.DataFrame()
  
   data=yf.download(stock,period=period)

   stockdata=data #stock data is a data frame

  #fig,ax=plt.subplot(figsize=(16,9))
  #for i in stockdata.columns.values:

   stockdata=stockdata.rename_axis('Date').reset_index()
  
   print(stockdata)

   stocks.saveData(stockdata)

   return stockdata
   #basic_info(stock)
   #balance_sheet(stock)

 def saveData(stockdata):
   choice=int(input(print("Enter 1 to Save Data into a CSV file \nEnter 2 If don't wish to save Data\n")))
   if choice == 1:
      filename=str(input("Enter Filename : "))
      filename=filename+".csv"
      stockdata.to_csv(filename)   


 def basic_info(stockdata,stock):
    ticker=yf.Ticker(stock)
    info=ticker.info
   
    for key, value in info.items():
     print(str(key)+" : "+str(value))
    stocks.show_menu(stockdata,stock) 
 
 def balance_sheet(stockdata,stock):
    ticker=yf.Ticker(stock)
    sheet=ticker.balance_sheet
   
    choice=int(input("Enter 1 to Save as CSV \nEnter 0 to not Save\n"))
    if choice==1:
      filename=str(input("Enter Unique Filename : "))
      exten=".csv"
      filename=filename+exten
      sheet.to_csv(filename)
    if choice!=1:
      print("Not Saving File.. Exiting")  
      exit() 
    stocks.show_menu(stockdata,stock)  
      
 def getreturn(stockdata,stock):
    newdata=stockdata
    newdata['Returns']=((newdata['Close']-newdata['Open'])/newdata['Open'])*100


    plt.figure(figsize=(20,18))
    plt.title("DAILY STOCK RETURN FOR "+str(stock))
    plt.plot(newdata.Date,newdata.Returns,'r.-')
    plt.show()
    stocks.show_menu(stockdata,stock)


 def highvlow(stockdata,stock):
   
   plt.figure(figsize=(20,19))
   plt.title("HIGH VS CLOSE PRICE FOR "+str(stock))
   plt.plot(stockdata.Date,stockdata.High,'b.-')
   plt.plot(stockdata.Date,stockdata.Close,'r.-')
   plt.show()
   stocks.show_menu(stockdata,stock)

 def openvclose(stockdata,stock):
    
    #plotting data
    plt.figure(figsize=(20,18))
    plt.title("OPENING PRICE,CLOSING PRICE vs DATE FOR "+str(stock))
    plt.plot(stockdata.Date,stockdata.Open,'b.-') 
    plt.plot(stockdata.Date,stockdata.Close,'r.-')
    plt.legend()
    plt.show()

    stocks.show_menu(stockdata,stock)

 def show_volume(stockdata,stock):
   
   date=stockdata['Date'].to_numpy()
   volume=stockdata['Volume'].to_numpy()
   plt.figure(figsize=(20,18))
   bins=date
   plt.title("VOLUME DATA FOR "+str(stock))
   #plt.hist(volume,bins=bins)
   stockdata['Volume'].hist(bins=bins)
   plt.xlabel('Date')
   plt.ylabel('Volume')
   plt.show()

 def show_menu(dataset,stockname):
    choice=int(input(" Enter 1 to see Basic Info of Stock \n Enter 2 to save Balance sheet of a Stock\n Enter 3 to see Open vs Close Price Data as a Graph \n ENTER 4 to see Daily Return Data of Stock \n Enter 5 to see Volume Data.\n ENTER 6 to High vs Low price Data as Graph \n Enter 7 to Exit\n"))
    if choice == 7: 
      exit()
    if choice == 1:
      stocks.basic_info(dataset,stockname)
    if choice == 2:
      stocks.balance_sheet(dataset,stockname)
    if choice == 3:
      stocks.openvclose(dataset,stockname)
    if choice == 4:
      stocks.getreturn(dataset,stockname)
    if choice == 5:
       stocks.show_volume(dataset,stockname)
    if choice == 6:
       stocks.highvlow(dataset,stockname)   
 def volumeData():
    #data=stockData.get_data()
    return
 
 def startpoint():
    print("********WELCOME********")
    stockname=str(input("Enter Stock Symbol : "))
    period=str(input("Enter Time period : "))

    dataset=pd.DataFrame()
    dataset=stocks.get_data(stockname,period)
    stocks.show_menu(dataset,stockname)
 def __init__(self) -> None:
    stocks.startpoint()
 


class login():
 def login():
    username=str(input("Enter Username  : "))
    check=" " in username
    if(check):
      username=str(input("Enter Userame without space."))
    
    password=str(input("Enter Password  : "))
    check=" " in password
    if(check):
       password=str(input("Enter Password without space"))
    return login.checkcredentials(username,password)

 def checkcredentials(user, password):
    creden=open("login.txt",'r')
    for cred in creden:
       if user in cred:
          if password in cred:
             return True
          else:
             return False
    creden.close()      
    return False
          

 def createuser():
    username=str(input("Enter Username  : "))
    check=" " in username
    if(check):
      username=str(input("Enter Userame without space."))
    
    password=str(input("Enter Password  : "))
    check=" " in password
    if(check):
       password=str(input("Enter Password without space"))
    login.addcredentials(username,password)
    

 def addcredentials(user,password):
   creden=open("login.txt","a")
   creden.write(user+":"+password+"\n")
   creden.close()
   print("User created successful")

 def menu__():
   user_input=int(input("Enter 1 to Login\nEnter 2 to Sign-up\n"))
   if user_input==1:
      if login.login():
         print("User Login Successful")
         stock=stocks()
         stock.startpoint()
      else:
         user_in=int(input("No such User.Enter 1 to Exit   2 To create User"))
         if(user_in==2):
            login.createuser()
         else:
            exit()
   if user_input==2:
      login.createuser()

 def __init__(self) -> None:
    login.menu__()



login()
