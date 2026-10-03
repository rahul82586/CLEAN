[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [MetaTrader 5 Administrator](../../MetaTrader-5-Administrator.md) / [Getting Started](../Getting-Started.md) / Start Terminal

[Previous](Install-Terminal.md) | [Next](Structure-of-Directories-and-Files.md)

<a id="start-terminal"></a>
# Start Terminal (#start-terminal)

After the installation has been completed, a group of the administrator terminal programs is created in the "Start" menu, and the program shortcut is additionally located on the desktop. They will help to start the terminal.

> You cannot run two copies of the administrator terminal from the same directory simultaneously, including running in the [console mode (#console)](Start-Terminal.md#console). If you need to run multiple terminals at the same time, install the appropriate number of programs in different directories.

The administrator terminal can be launched in two modes.

<a id="guest"></a>
## Main launch mode (#guest)

Starting from MS Windows Vista, applications installed to Program Files are not allowed by default to store their data in the installation folder. All data should be stored in a separate Windows user directory.

Thus, if the terminal is installed in the Program Files directory and user rights to write to that directory are limited, it is run in the main mode. The main mode is also used in the following situations:

  * If the UAC (User Activity Control) system is enabled.
  * If remote connection to a computer is used (RDP, Remote Desktop Protocol).



In this mode, the editable files of the terminal are stored in a specific Windows user directory, and the immutable files are stored in Program Files. The immutable files include the executable terminal file, built-in help files, etc. Editable files are:

  * all settings of the terminal, configuration files
  * all databases (news, mails)
  * terminal operation logs
  * email templates



All the editable files of the terminal are stored in the following directory: C:\Users\username\AppData\Roaming\MetaQuotes\MetaTrader 5 Administrator\instance_id\\.

Here 'C' is the logical drive letter on which Windows is installed, "username" is the account name in the operating system under which the terminal has been installed, "instance_id" means a unique identifier generated based on the path to the directory where you installed 0terminal.

For quick access to these folders, use the command "![Open data folder](images/open_data_folder_button.png) Open Data Folder" in the [File](../User-Interface/Main-Menu/File.md) menu. Each data folder contains a special text file origin.txt. This file contains the path to the terminal installation folder, which corresponds to this data directory.

  * In the main mode, the catalog where editable files are stored is different for each Windows account.
  * A detailed description of the file structure of the administrator terminal and of the files purpose are given in the [appropriate section](Structure-of-Directories-and-Files.md). 

  
---  
  
<a id="portable"></a>
## Portable Mode (#portable)

When installed to Program Files, the terminal operates by default in the main mode described above. All data are stored in a special Windows user directory. However you can force the terminal to store its data in the installation folder. To do it, run the platform in the portable mode. To use this mode, start terminal from the command line with the additional /portable key. For example, "D:\Program Files\MetaTrader 5 Manager\mt5manager64.exe /portable".

> To run the terminal in Portable mode, the following conditions must be met:

<a id="console"></a>
## Console Mode (#console)

The administrator terminal can be used in the console mode, without the user interface. This mode enables the automation of some processes when operating with the trading platform.

Use the /console key to launch the terminal in the console mode:

/console /server:<trade server address:port> /login:<login> /password:<password> /action:<command> [command arguments]  
---  
  
Specify platform connection details in the 'server', 'login' and 'password' parameters. The type of the cation to perform is specified in 'action':

<a id="server-restart"></a>
### Server restart (#server-restart)

Command /action:restart [/name:<server name>]. Optionally the server name can be specified (History, Access...). If the name is specified, the appropriate sever will be searched (case insensitive). If the name is not specified, the specified command will be performed for the currently connected server.

<a id="platform-configuration-export-to-json"></a>
### Platform configuration export to JSON (#platform-configuration-export-to-json)

Command /action:export /file:<path> [/type:<type> /config:<mask>]. If optional arguments are not specified, the entire configuration of the connected server is exported.

Argument /file:<path> sets the destination file path. Argument /type:<type> is used for exporting a selected configuration branch and it may have the following values:

common  
network  
firewall  
time   
holidays  
groups  
managers  
routing  
gateways  
plugins  
feeders  
reports  
symbols  
spreads  
historysync  
---  
  
Argument /config:<mask> sets a search criterion to search for a particular configuration structure by a string mask (this may contain *,!). Search by mask can be used for the configurations of servers, groups, managers, trade requests, gateways, plugins, data feeds, reports and symbols. The following rule applies to other configurations: if a mask is set, the configuration should be skipped, if no mask is specified, the configuration should be processed.

<a id="platform-configuration-import"></a>
### Platform configuration import (#platform-configuration-import)

Command /action:import /file:<path> [/type:<type> /config:<mask>]. All arguments are similar to those applied to exports, except for the /type argument. The [common](../../Platform-Setup/Start-Page.md) branch (common platform settings) cannot be imported.

> In console mode, log files are saved in the directory where the Administrator terminal executable file is located: [directory with mt5admin64.exe]\Logs\\.
