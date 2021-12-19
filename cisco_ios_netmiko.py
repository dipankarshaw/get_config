import getpass
import datetime
import os
import concurrent.futures

from netmiko import ConnectHandler

file_path = os.path.dirname(os.path.realpath(__file__))
utc_datetime = datetime.datetime.utcnow()
formated_time = utc_datetime.strftime("%Y_%m_%d_%H%M%SZ")
os.mkdir(f"{formated_time}")


def show_command_fun(ssh_device):
    """show commands"""
    ssh_device = ssh_device.strip()
    ssh_device1 = ssh_device.replace(".", "_")
    os.mkdir(f"{ssh_device1}")
    try:
        net_connect = ConnectHandler(
            device_type="cisco_xr",
            host=ssh_device,
            username=username,
            password=password,
            global_delay_factor=2,
        )
        print(f"***** connected to {ssh_device}")
        for sh_cmd in commands_list:
            output = net_connect.send_command(
                sh_cmd, strip_command=False, strip_prompt=False
            )
            sh_cmd1 = sh_cmd.replace(" ", "_").strip()
            file_name = (
                file_path
                + f"/{formated_time}/{ssh_device1}/{ssh_device1}_{sh_cmd1}.txt"
            )
            with open(file_name, "w+", encoding='UTF-8') as file_open:
                file_open.write(f"Device Name : {ssh_device} >> {sh_cmd} \n")
                file_open.write(f"{output} \n\n")
        net_connect.disconnect()
    except:
        print(f"***** Exception happened while connecting to {ssh_device}")
        file_name = (
            file_path + f"/{formated_time}/{ssh_device1}/{ssh_device1}_Exception.txt"
        )
        with open(file_name, "w+", encoding='UTF-8') as file_open:
            file_open.write(f"{ssh_device} Device Not Rechable \n")


username = input("Enter username : ")
password = getpass.getpass("Enter Password : ")
with open("commands.txt", encoding='UTF-8') as commands, open("hostname.txt",encoding='UTF-8') as hostnames:
    commands_list = commands.readlines()
    iq_device_list = hostnames.readlines()
os.chdir(f"{file_path}/{formated_time}")
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(show_command_fun, iq_device_list)
print(f"**** Program Ended, get the outputs at : {file_path}/{formated_time}")
