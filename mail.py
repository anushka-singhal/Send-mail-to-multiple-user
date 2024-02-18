import smtplib as s 

ob = s.SMTP('smtp.gmail.com',port)
ob.ehlo()
ob.starttls()
ob.login('ixyz@gmail.com','password')
subject = "HEllO"
body = "I am python"
message = "subject:{}/n/n{}".format(subject,body)
listadd=['abc@gmail.com',"pqr@gmail.com"]
ob.sendmail('ixyz@gmail.com',listadd,message)
print("send mail")
ob.quit()

