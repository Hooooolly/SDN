from behave import *
import os
from manager import main

@given('There is incoming traffic')
def step_impl(context):
        pass
@when('All traffic is coming from trusted sources')
def step_impl(context):
        pass
@then('Allow all traffic')
def step_impl(context):
        main()
        pass                   
