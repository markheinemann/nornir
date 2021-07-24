cdfrom nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
import textfsm


#this script works 


print("Example: show ip int brief, show ip route, show version >")

commands = input ("\nEnter Commands: ")
cmds = commands.split(",")

for cmd in cmds:
    nr = InitNornir()

    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd,
        use_genie=True
        )
    print_result(result)



 #alternative way
'''nr = InitNornir()
def labeveryday(task):
    task.run(task=netmiko_send_command, name="LAB EVERYDAY!!", command_string="show ip int brief")

results = nr.run(task=labeveryday)
print_result(results)'''   
