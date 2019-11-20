Note: 
We did this assignment later during the semester in the past, 
so it may feel out of order.
By popular demand, we're trying it earlier.
Doing it now will allow us to not only utilize these all semester, 
and learn the full details later.


# Part 1: Install VirtualBox (campus) or KVM (an alternate on your own machine), setup a VM

Read: 
https://taylor.git-pages.mst.edu/index_files/DataStructuresLab/Content/VirtualMachines.html

For this class, any Linux distro will do, though Debian 10 or Fedora 30 are the two most foundational distros.
I will use Debian 10 for demos and grading.

If you are using the CLC campus computers, VirtualBox is accessible via apps anywhere.
If you want the VM to be persistent, either store it on your SDRIVE, or store the files on a USB stick.
If you store on the local drive, all your files will dissapear when the CLC computer is rebooted.

We will be using these VMs during our Wireshark labs in class, 
so you may want to actually do this on the campus machines, 
if you won't be bringing your laptop.


# Part 2: Basic virtual network

## Summary: Clone your VM (there should now be two), set up a virtual network between the two machines, setup ssh, ssh from one VM to the other, and setup ssh keys.
This particular task is very common: 
For example, you get a VPS ( https://en.wikipedia.org/wiki/Virtual_private_server ) or remote machine at a company, 
setup the basic OS, install SSH, and begin your remote administration. 
This is the foundation of remote machine management. 

Note: this part of the assignment is intentionally somewhat open-ended.
One of the goals is to get some practice finding guides/howtos to complete a task, 
filtering out the junk, and finding a modern and correct solution among those that are not. 
Having to execute such a task from merely high-level instructions is a very common task at work!
You've all ssh'ed before -- recall putty and cssubmit?

1. Learn some background information:
    * Fully read the following documentation on virtual networking in VirtualBox: https://www.virtualbox.org/manual/ch06.html 
    * Watch some videos videos on VirtualBox virtual networks and ssh:
        * https://www.youtube.com/results?search_query=virtualbox+ssh+ 
        * For example: How to Create a Network of Machines in VirtualBox with SSH Access  https://www.youtube.com/watch?v=S7jD6nnYJy0
    * Read some articles on the same: https://duckduckgo.com/?q=virtualbox+ssh+debian+guest+to+guest&t=ffab&ia=web 
        * For example: https://linuxhint.com/enable-ssh-server-debian/ 

2. Set up the network
    * Clone your VM. Read about whether or not you should update the MAC address of the NIC in the new VM you cloned.
    * Configure VirtualBox network settings for each VM, and VM internal network settings (if needed).
    * Make sure you can https://en.wikipedia.org/wiki/Ping_(networking_utility)  between the two guest machines.
    * Install ssh server in one machine, enable it, reboot.
    * Test the ssh server by ssh'ing from one guest to the other guest machine.

3. Write a report, `report.md`:
    * Which VirtualBox networking mode did you use? Why? Justify the logic.
    * What did you do with the MAC addresses of the VMs when you cloned? Why?
    * Include a screenshot of each of your VMs' network settings. Describe what the captured fields mean.
    * How did you install and configure your ssh server? What does each sub-step of installation and configuration do?
    * Include screenshots of successfully sshing from one machine to the other.
    * What would you guess the ssh traffic look like?

Note: Since we're manually grading this one, there are no re-grades.

