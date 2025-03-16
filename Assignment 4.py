import requests
def supermarket():
  try:
    url="http://demo3278802.mockable.io/Super_Market_Data"
    response=requests.get(url)
    print(response.status_code)
    if response.status_code==200:
      get_data=response.json()
      print(get_data)
      Fruitname=get_data["Fruitname"]
      Price=get_data["Price"]
      Quantity=int(input(f"How much quantity of {Fruitname} you want:"))
      Total_Price=Price*Quantity
      GST=(Total_Price*5)/100
      print(f"The Total bill is {Total_Price} and the GST Amount {GST} is also included in the bill")
      Bill_Method=int(input("Do you want email bill press 1 or printed bill press 2:"))
      if Bill_Method==1:
        import smtplib
        sender_email ="anil@gmail.com"
        receiver_email ="sunil.com"
        password = "@456"
        msg = EmailMessage()
        msg["Subject"] = "Your Bill Invoice"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(f"Your bill")
        print(f"The Total bill is {Total_Price} and the GST Amount {GST} is also included in the bill")
        try:
           with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
              server.login(sender_email, password)
              server.send_message(msg)
              print("Email sent successfully!")
        except Exception as e:
          print(f"Error: {e}")
      elif Bill_Method==2:
        f=open("customer_bill. csv", "r")
        print(f.read())
        f.close
      else:
        print("invalid input")
 except Exception as e:
   print("Error: {e}")
supermarket()

    
        
        

        