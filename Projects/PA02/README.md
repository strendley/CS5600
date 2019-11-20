# PA02 - smtp email server
* Please see the website for specifications. 
* Edit this file for any notes you would like me to see, including images of how you ran, configuration details, etc.

# Your report goes below here:

In order to run the script, the python file first needed to be granted execute permissions using the command:
sudo chmod +x smtp_client.py

Next, the script was run with a basic ./smtp_client.py.

An attempt was made to avoid authentication using Gmail's gmail-smtp-in-l-google.com server on port 25. The EHLO hello command was then used to query the google smtp server. Next, The start TLS command was executed second, which receives the proper 220 response code. The next step would be to wrap the client socket before sending the MAILFROM, RCPTTO, DATA, & QUIT commands. 

The result of the script was success in getting th HELO response and TLS 220 response, but fails in the next steps after
wrapping the socket due to a "Syntax Error" 505 followed by 503 MAIL first errors. 

OUTPUT (as of 9/27):

![pa02_smtp](https://user-images.githubusercontent.com/26886594/65812268-66ec2800-e18a-11e9-9447-a4615866c78a.PNG)
