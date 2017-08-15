from behave import *
from manager import main

@given('There is incoming traffic')
def step_impl(context):
        pass

@when('A dangerous IP is detected')
def step_impl(context):
        pass

@then('Block traffic')
def step_impl(context):
        main()
        pass

