from behave import *
from manager import main
import os
import socket
@given('There is incoming traffic')
def step_impl(context):

        ip = socket.gethostbyname(socket.gethostname())
        message = 'nmap -p 80 ' + ip
        recorded = os.popen(message).read()
        strOpen = "80/tcp open"
        Value = recorded.find(strOpen)
        if (Value != -1): #if port 80 is open/reciving traffic
                pass

@when('A dangerous IP is detected')
def step_impl(context):
        pass

@then('Block traffic')
def step_impl(context):
        main()
        pass
