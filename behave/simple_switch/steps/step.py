from behave import *
from manager import main
import os
import socket
@given('There is incoming traffic')
def step_impl(context):

        #Check if there is an incoming packet if there is pass
        ip = socket.gethostbyname(socket.gethostname())
        message = 'nmap -p 80 ' + ip
        recorded = os.popen(message).read()
        strOpen = "80/tcp open"
        Value = recorded.find(strOpen)
        if (Value != -1):
                pass


@when('All traffic is coming from trusted sources')
def step_impl(context):
        pass

@then('Allow all traffic')
def step_impl(context):
        main()
        pass
                 
