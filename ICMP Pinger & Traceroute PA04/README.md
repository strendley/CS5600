# PA04 - ICMP ping and traceroute using scapy
* Please see the website for specifications. 
* Edit this file for any notes you would like me to see, including images of how you ran, configuration details, etc.

# Your report goes below here (include screenshots of you running and output!):

For the ICMP Pinger, I was able to impot the sr1, IP, and ICMP functions from scapy.all for usage inside the program. I requested user input for the target/hostname that the user
would choose to ping, and then use the IP function with the destination being the user-defined target to ping. Then, I was able to use the sr1 function to send the packets. 
If no response was received, the user would be notified that the packets were dropped. Otherwise, the report listed the successful packet arrival. Successful execution looked like
this:

![screenshots_imcp-pinger](https://user-images.githubusercontent.com/26886594/69200385-92dbb800-0b00-11ea-9466-2be08e2232c5.png)


For the ICMP Traceroute, I was able to import * from scapy.all for usage inside the program. I request user input for the target/hostname that user would choose to traceroute, and
chose to make the maximum amount of hops to 30. Next, I used the sr1 function to start sending packets towards the desired hostname and loop through the range to ssee how the source
 of the packet's reply changed as the traceroute was executed. If the source did not send a reply, then the output would just be "* * *" to simulate the traceroute functionality.
 Successful execution looked like this:

![screenshots_icmp-traceroute](https://user-images.githubusercontent.com/26886594/69200358-7fc8e800-0b00-11ea-96a0-a3937e313c5a.png)





