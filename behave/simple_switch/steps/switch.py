from behave import *
import os
from manager import main
from simple_switch import SimpleSwitch

@given('1')
def step_impl(context):
	pass

@when('2')
def step_impl(context):
	main()
	pass		
@then('3')
def step_impl(context):
	pass
