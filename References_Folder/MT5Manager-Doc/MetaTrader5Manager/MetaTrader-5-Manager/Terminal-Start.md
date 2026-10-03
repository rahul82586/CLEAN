[🏠 Document Start](../README.md) / [MetaTrader 5 Manager](../MetaTrader-5-Manager.md) / Terminal Start

[Previous](../MetaTrader-5-Manager.md) | [Next](Connecting-to-the-Server.md)

<a id="terminal-start"></a>
# Terminal Start (#terminal-start)

As soon as installation is complete, a group of programs of the Manager terminal is created in the Start menu, and the program shortcut is created on the desktop. Use them to run the platform.

> You cannot run two copies of the terminal from the same directory simultaneously. If you need to run multiple copies at the same time, install the appropriate number of programs in different directories.

There are two modes of starting the Manager terminal.

<a id="guest"></a>
## Main launch mode (#guest)

Starting from MS Windows Vista, applications installed to Program Files are not allowed to store their data in the installation folder on default. All data should be stored in a separate Windows user directory.

Thus, if the terminal is installed in the Program Files directory and the user's rights to write to that directory are limited, it is run in the main mode. The main mode is also used in the following situations:

  * If the UAC (User Activity Control) system is enabled.
  * If remote connection to a computer is used (RDP, Remote Desktop Protocol).



In this mode, the editable files of the terminal are stored in a specific Windows user directory, and the immutable files are stored in Program Files. The immutable files include executable file of the terminal, built-in help files, etc. Editable files are:

  * all settings of the terminal, configuration files
  * all databases (news, mails)
  * terminal operation [journal (#journal)](../User-Interface/Toolbox.md#journal)
  * email templates



All the editable files of the terminal are stored in the following directory: C:\Users\username\AppData\Roaming\MetaQuotes\MetaTrader 5 Manager\instance_id\\.

Here 'C' is the letter of the logical drive Windows OS is installed at, "username" — account name in the operating system, under which the terminal has been installed, "instance_id" — a unique identifier generated based on the path to the directory where you installed terminal.

For quick access to these folders, use the "![Open Data Folder](images/open_data_folder_button.png) Open Data Folder" command in the [File (#file)](../User-Interface/Main-Menu.md#file) menu. Each data folder contains a special origin.txt text file. This file contains the path to the terminal installation folder, which corresponds to this data directory.

  * In the main mode, the catalog where editable files are stored is different for each Windows account.
  * A detailed description of the platform file structure and their purpose is given in the [appropriate section](For-Advanced-Users/Files-and-Folders.md). 

  
---  
  
<a id="portable"></a>
## Portable mode (#portable)

When installed to Program Files, the platform works in the main mode described above on default. All the terminal data are stored in a special Windows user directory. However, you can force the terminal to store its data in the installation folder. To do it, run the platform in the portable mode. To use this mode, start terminal from the command line with the additional /portable key. For example, "D:\Program Files\MetaTrader 5 Manager\mt5manager64.exe /portable".

> To run the terminal in Portable mode, the following conditions should be met:
