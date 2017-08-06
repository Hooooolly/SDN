# SDN

These files should be outside of the Ryu folders which can be gotten from https://github.com/osrg/ryu

Once you have ryu and these files installed you are ready to run. 
To launch Mininet use the command "sudo mn --mac --controller remote --switch ovsk"
In a seperate window go to the folder which contains the .feature file and run "behave"
This will run the ryu controller in mininet 
