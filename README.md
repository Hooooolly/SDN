# Setting up the Environment
Prerequisites: ryu, mininet, and behave

For the best results download the Virtual Machine Image with Ryu and Mininet following the steps here https://github.com/osrg/ryu/wiki/OpenFlow_Tutorial 

Once the virtual machine is ready and running it is time to install the Behave function
To do so run the command "pip install behave"
If you have any issues the guide can be found here http://pythonhosted.org/behave/install.html

Once you have all of this downloaded and running it is time to install our code. 
This picture shows how the file structure should be set up

![screenshot 65](https://user-images.githubusercontent.com/25207378/29027615-0bb0d5f4-7b47-11e7-922d-037beca710b5.png)

# Running the Code
Now that everything is in place we can execute the code
First we need to launch mininet to do so we run to prompt "sudo mn --mac --controller remote --switch ovsk"
This will run an instance of mininet with a basic topology and no running controller
If you have a custom topology you can run the command as shown in the picture, I have included our own as an example



(note: your custom topology files will need to be located in the mininet/custom folder)
