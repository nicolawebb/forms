#!C:\Users\niick\AppData\Local\Programs\Python\Python36\python.exe
import cgi
import cgitb      #use for error traces
cgitb.enable()    #use for error traces

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields  
name = form.getvalue('name')        # name of the field is same as in client form
module  = form.getvalue('module')   # name of the field is same as in client form

print ("Content-type:text/html\n")
print ("<HTML>")
print ("<HEAD>")
print ("<TITLE>Hello - Form processing</TITLE>")
print ("</HEAD>")
print ("<BODY>")
print ("<H1>Hello ", name, ". You're enrolled to study ", module, ". Enjoy!</H1>")
print ("</BODY>")
print ("</HTML>")
