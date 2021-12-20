# get_config
get_config.cisco_ios_netmiko module
This code helps user to collect show command Output’s in very effective way.

Input
List of nodes in hostname.txt file

List of commands, whose output is to be collected, to be kept in commands.txt file.

Output
Show output’s are stored in a efficient folder structure.

get_config.cisco_ios_netmiko.show_command_fun(ssh_device)[source]
Purpose
This function takes one node Data.

Parameters
ssh_device – IP/Name of the device.

Logs into the node.
creates the directory structure.

collect show command output’s & save them in text file.

If exception happen then it generats a file saying not reachable.

Returns
Dictonary , containing the stats.

# Sample use
![Smaple_use](https://user-images.githubusercontent.com/61518346/145091364-3d8004bd-059c-4281-a4f2-dd4b5adfdebd.png?raw=true)
