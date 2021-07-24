from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_netmiko import netmiko_send_config
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
import textfsm
import csv

## will drop into interactive mode after running
# nr.inventory.hosts
# nr.inventory.hosts['R1']
# nr.inventory.hosts['R1']['facts']
# pp nr.inventory.hosts['R1']['facts']
# pp nr.inventory.hosts['R1']['facts']['version']['switch_num']['1']['system_sn']


# xls header fields
interface_file = "interfaces.csv"
report_fields = ["Device", "Interface", "In_Packets", "Load_Interval"]


def get_facts(task):
    with open(interface_file, 'a') as f:
         # Create a CSV "DictWriter" object providing the list of fields
        writer = csv.DictWriter(f, report_fields)
        # Write the header row to start the file
        writer.writeheader()


        #ipvzero.run(task=netmiko_send_config, config_file= "config_textfile")
        r = task.run(netmiko_send_command, command_string = "show int status", use_genie=True)
        #ipvzero.run(task=netmiko_send_command, command_string = "show clock", use_textfsm=True)
        #ipvzero.run(task=netmiko_send_command, config_file = "commands.txt")
        task.host["facts"] = r.result

# simplified version of script9.py - dont need to specify for loop for interfce range
#instead we are are using. items() to iterate around the dictionary

        for interface,details in task.host['facts'].items():
            print(interface)
            
            print(details["counters"]["in_pkts"])
            writer.writerow(
                {"Device" : task.host,
                "Interface" : interface,
                "In_Packets" : details["counters"]["in_pkts"],
                "Load_Interval" : details["counters"]["rate"]["load_interval"]}
                ) 



def main() -> None:
    nr = InitNornir(config_file="config.yaml") 
    result = nr.run(task = get_facts)
    #print_result(result)
    #print (nr.inventory.hosts["R1"]["facts"])
    

    import ipdb;
    ipdb.set_trace()

if __name__ == '__main__':
    main()    


