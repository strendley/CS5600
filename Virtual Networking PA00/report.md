# Virtual Networking: PA00-Part 1

1. The VirtualBox networking mode that I used was Host-Only networking. This allowed me to create a network of virtual machines that could interface with each other. By connecting them together on a host-only network, I could ping each machine for communication but stay disconnected from the outside networks. A bridged connection was created to communicate with the internet.
2. The MAC addresses were randomized upon creation of the machines in order to create a static IP address. This static IP address was important to make sure the machines were at different addresses for communication between two different devices.
3. 


   ![ip_a_clone1](https://user-images.githubusercontent.com/26886594/63563296-17de2200-c550-11e9-9365-625645404d79.png)

The enp0s3 is the bridge adapter that allows the clone to access the internet. The enp0s8 adapter is the host-only adapter that allows the connection between the two clone Vms. The inet under enp0s8 is the IP address of each cloned VM. The unique IP corresponds to a unique MAC address that allows the connection by specifying a unique address that connections can respond to.

4. To install and configure ssh-server, each of the clones needed to run the commands sudo apt-get update, to make sure each dependency of the libraries are up-to-date, followed by sudo apt-get install openssh-server which installs ssh-server onto the machine, and then restart ssh server by using the command sudo service ssh restart which makes sure the service is running. Once successful, ssh server was enabled on each of the cloned machines and could be ssh-ed into from the main machine.
5. 


   ![clone1_ssh_clone2](https://user-images.githubusercontent.com/26886594/63563217-dc435800-c54f-11e9-85e0-91ab0f28e146.png) 
   ![clone2_ssh_clone1](https://user-images.githubusercontent.com/26886594/63563229-ec5b3780-c54f-11e9-9249-59d35bb4a672.png)


6. 

   ![ssh_traffic](https://user-images.githubusercontent.com/26886594/63563352-5378ec00-c550-11e9-9399-852b8f1d1cc0.png)


The SSH traffic looks like it detects the occurrence of successful logins and keystrokes. Whenever a keystroke was made while SSH-ed into the clone that was running wireshark, wireshark recorded the packet transfer of encrypted data being sent from the server and to the client.

