[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Installation](../Platform-Installation.md) / Installation

[Previous](System-Preparation.md) | [Next](Activation.md)

<a id="installation-of-the-metatrader-5-platform"></a>
# Installation of the MetaTrader 5 Platform (#installation-of-the-metatrader-5-platform)

Before you start platform installation, you need to rent servers from hosting providers keeping in mind [system requirements](System-Requirements.md). Required [preparatory works](System-Preparation.md) should be performed on these servers. After that you can proceed to platform installation:

  * Complete platform installation on the main server
  * First connection to the platform and necessary actions
  * Installation of additional backup servers
  * Additional access servers
  * Additional trade servers
  * Installation of a platform for testing new features and developing own solutions



<a id="full"></a>
## Complete platform installation on the main server (#full)

The platform installer allows you to deploy a required set of servers on one local computer, including the main trade server, its backup server, the history server and the access server. This option should be used during the first platform installation on the main server. After that, you will be able to connect to the platform using the MetaTrader 5 Administrator and proceed to the installation and configuration of additional components.

Run the mt5srvsetup.exe platform installer and select "Full installation":

![Selecting the installation type](images/platform_installation_type.png)

Read the license agreement and, if you agree, check "Yes, I agree with all terms of this license agreement". Next, specify the path to the platform license file *.lic. Information from the license is displayed at this stage, including the product (license expiration date), the company for which the license has been issued, and the domain name.

![Platform Installation](images/platform_installation_settings.png)

At the next stage, specify the installation parameters:

  * Installation folder — click "Browse" and select the folder to which you want to install the trading platform.
  * Program group — specify the group name for the trading platform; this name will be displayed in the Start menu.
  * IP address — choose one of the IP addresses available on the server. Connection to the platform will be established using this address.
  * Profile — choose one of the port profiles for connection. The 441-444 range is used by default, and the port 443 will be used for public access (access server). Other ports are allocated for the trade server, the history server, and the backup server. There are also some additional profiles. For example, the range of 1950-1953, in which port 1950 is used for the access server.



  * If all ports specified in the profiles are occupied by other applications, you should install the platform components one by one. In this case, you can specify any other port manually.


  * Full Installation is not possible if at least one of the ports from the selected range (profile) is busy. In this case, it does not matter what network interface it is used for. The installer checks all available interfaces to prevent any network conflicts. If you receive a message about a busy port during Full Installation, install the platform components one by one.

  
---  
  
A click on the Next button will launch the platform installation process:

![Completing the Installation](images/platform_installation_finish.png)

At the end of the installation procedure, a dialog box will appear showing details for the first connection to the platform using MetaTrader 5 Administrator: a login and password for the automatically created administrator entry, and the address for connection. Be sure to save this data in a safe place, otherwise you will not be able to connect to the platform without this information.

To complete platform installation, press "Finish". After that, a program group specified during installation, with the commands to launch and stop platform components will appear in the Start menu.

<a id="first-connection"></a>
## First connection to the platform and necessary actions (#first-connection)

One [administrator account](../Platform-Setup/Managers.md) with login "1000" and a random password is automatically created during platform installation. These data, as well as the address of the server to connect to, are displayed on the last step of the platform installation. Be sure to save this data in a safe place, because without it you will not be able to connect to the platform using the MetaTrader 5 Administrator.

The password to the automatically created administrator account is also saved in the log file of the main trade server (the /Logs folder).

[Add](../MetaTrader-5-Administrator/Getting-Started/Add-or-Remove-Servers.md) the newly installed platform to the MetaTrader 5 Administrator, and then [connect](../MetaTrader-5-Administrator/Getting-Started/Connect-to-Server.md) to it using the administrator account. For security reasons, you will immediately need to [change your password (#change-password)](../MetaTrader-5-Administrator/Getting-Started/Connect-to-Server.md#change-password).

At the next step, you need to [activate licenses](Activation.md), in order to remove all functional limitations of the platform.

> The password generated for the first administrator account is also used by all components of the platform for internal authentication. If necessary, change it on the [Common (#password)](../Platform-Setup/Network-cluster/Configuring-Servers.md#password) tab of each server.

<a id="backup"></a>
## Installation of additional backup servers (#backup)

Once the main platform part is installed, it is recommended to configure appropriate backup servers. The ability to ensure uninterrupted business operation is one of the main requirements set by financial regulators.

The MetaTrader 5 platform provides a separate component responsible for data security, which is the [backup server](../Platform-Components/Backup-Server.md). It runs in parallel as an exact copy of the primary trade or history server. The state of the backup server is constantly synchronized with the primary server, allowing any time to switch to the backup server. However, the backup creation process is resource efficient:

  * Critical and frequently changing data are synchronized in real time. These include client and trade databases, platform settings, configurations and databases of gateway trade executions.
  * The remaining data are backed up every hour, including mail and news databases, files, executable files and gateways and data feeds, plug-ins, etc.



  * Always install backup servers — it is a mandatory component of the platform. The trade and history servers do not create backups of data bases.
  * Several backup servers can be created for each trade and history server, which reduces the risk of system failure to a minimum.

  
---  
  
During the complete platform installation, a backup server is only created for the main trade server. It is installed on the same computer/disk, where the main components are installed. It only provides the minimum level of protection, for example against the accidental deletion of the main server databases. However, in case of hardware failure, the main and the backup server will be unavailable.

In order to provide a reliable platform operation, it is recommended to manually add backup servers for the history server, as well as additional trade servers (if any). Such backup servers must be installed separately from the main servers, and always on separate computers.

The easiest way to install the server is to configure it first in the MetaTrader 5 Administrator terminal, and then to use the [deployment](Fast-Deployment.md) function.

Before deploying a server, make sure to configure the server network parameters: the password that will be used by other cluster components for connection to the backup server, as well as the IP addresses, through which the new server will send and receive data. All these parameters will be registered in the server installation package. Thus, all remaining cluster components will be able to connect to the backup server immediately after installation, while you will be able to manage the server via the Administrator terminal.

> Make sure that [network parameters (#network-connection)](System-Preparation.md#network-connection) are correctly configured and all the [required ports (#firewall)](System-Preparation.md#firewall) are open. It is important, because during deployment, an instant connection to all the required servers of the cluster will be required.

All other parameters can be configured after installation.

![Server Settings](images/deploy_configure_1.png)

After creating a configuration, run the server deployment command:

![Deploy...](images/deploy_menu_1.png)

After that you will receive an executable file. Copy it to the directory to which you want to install the new server and then run from the command line with the /install key. For example:

D:\MetaTrader 5 Platform\Backup History\Deploy_5_Backup_Server.exe /install  
---  
  
The file will install the backup server with the parameters that were pre-configured in the MetaTrader 5 Administrator. Then you should [configure the rest backup parameters](../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md):

![Backup Settings](images/network_add_backup.png)

When configuring parameters of backup servers, you should find balance between the frequency of backups and the available disk space on the computer where the backup server is installed:

  * Backup time — time of creating file copies. Apart from synchronizing with the main server in real time, the backup server creates [database file copies (#file)](../Platform-Components/Backup-Server/Backup-Features.md#file) on the disk on a daily basis. Such copies allow [restoring (#restore)](../Platform-Components/Backup-Server/Backup-Features.md#restore) the main server status on a specific day.
  * Additional backups — frequency of creating additional file copies. By default, file copies are created every 24 hours, but you can set this to happen more often — once per hour or once per 4 hours. Keep in mind that this will require more server resources and more disk space. This option is only available for the backup of trading servers; backup copies of history servers are always created once every 24 hours.
  * Keep backups — file copies storage period. All backup copies older than a period specified in this field are automatically deleted.
  * Enable tick backups — this parameter should be enabled with caution, because tick data take up too much space. If you back up tick data, set short copy storing period so that they do not consume all the available disk space.



  * Repeat the procedure and install backup servers for other platform components , including the history server and all other trade servers. Install backup servers separately from the main ones, and always on separate computers.


  * Install assess servers close to the backup ones. These access servers will be used for client connections in case the platform switches to the backup servers.

  
---  
  
<a id="access"></a>
## Additional access servers (#access)

It is recommended to install additional access servers in order to improve system performance and reliability. Access servers process client connections, cache data, and protect the platform against DDOS attacks. They also monitor the availability of the trade and history servers to enable the operation of the [automatic failover system (#auto)](../Platform-Components/Backup-Server/Switching-to.md#auto).

Connection to the entire trading platform is only available through access servers. If you decide to use one server, and it fails, neither administrators nor traders will be available to connect to the platform. In addition, the entire connection processing load will be handled by one server, which may affect negatively the system performance.

It is recommended to install several access servers on separate computers. The platform [analyzes the current load](../Platform-Components/Access-Server/Priority.md) on each server, and effectively distributes client connections between them. 

Access servers can be installed using the earlier described deployment procedure. After the installation, configure all other parameters in the [Network cluster](../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md) section.

<a id="trade"></a>
## Additional trade servers (#trade)

If the company becomes larger and the number of active clients increases, you can install additional trade servers in order to remove some load from the main server. It is recommended to install an additional trade server in the same data center, where the main and history servers are installed. Trade servers should not be far from the history server, in order to avoid delays when delivering quotes and sending trading operations to external systems through gateways.

After the installation of an additional trade server, it is recommended to install its backup server in a different data center, where the backup servers of the main and history servers are running.

Additional trade servers can be installed using the earlier described deployment procedure. After the installation, configure all other parameters in the [Network cluster](../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md) section.

<a id="automatic-creation-of-the-first-administrator-account"></a>
### Automatic creation of the first administrator account (#automatic-creation-of-the-first-administrator-account)

The platform architecture allows an administrator/manager to only work with accounts and databases on the trade server, where the administrator or manager account (its group) is located. For example, when connected to the main server, the administrator/manager cannot create accounts on additional trade servers. In order to connect to the additional trade server and manage accounts on it, the administrator or manager needs to have an account on this server.

During the installation of an additional trade server, one administrator account is automatically created on it. The first free login available in the [range of accounts (#accounts)](../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#accounts) set for the server will be given to the administrator account:

![Range of accounts](images/install_additional_trade_range.png)

In addition to the administrator account, [groups](../Platform-Setup/Groups.md) linked to this account are also created automatically on the server:

  * demo\demoforex-ID
  * managers\dealers-ID
  * managers\administrators-ID
  * real\real-ID



Here ID is the [internal identifier (#identifier)](../Platform-Setup/Network-cluster/Configuring-Servers.md#identifier) of the added trade server.

  * The administrator account and groups can only be created after you specify the range of accounts. It can be specified when adding a server or when editing it. In other words, once a trade server with the specified account range is added, groups and a manager account are automatically created for this server. If you configure the range before running the deployment, the administrator account and the group will be created during server installation.
  * A password for the manager account is generated randomly. The login and password of the created account are written to the server's log file (the /Logs folder). The following entry is added: default manager with login '1000' and password 'lfd5fircvs' added
  * When you first connect using the automatically created administrator account, you will need to complete the [forced password change (#change-password)](../MetaTrader-5-Administrator/Getting-Started/Connect-to-Server.md#change-password) procedure.

  
---  
  
<a id="launching-the-server"></a>
### Launching the server (#launching-the-server)

For the newly added server to start functioning, you need to restart the entire platform (the main trade server). After the system reboot, the following operations are performed automatically:

  * An account in the manager\administrators-ID group is created for the automatically generated administrator account. If the group does not exist for some reasons, an account will be created in another manager group available on the server.
  * If additional accounts were created in the Manager section before restarting the system, and the logins of these accounts fall into the account range of the added server, accounts in appropriate groups will also be created for them.



<a id="dev-license"></a>
## Installation of a platform for testing new features and developing own solutions (#dev-license)

In addition to the main operating platform, you can install a test (developer) platform for free. Use it to test new platform settings and develop applications using MetaTrader 5 API, without affecting workflow processes and real client operations. It is also recommended to use this platform for installing updates released in beta mode. This will allow you to explore new features in advance and test the operation of third-party applications before updating your main platform.

Please contact [Service Desk](../Technical-Support.md) to receive the test platform license. 

A test license is a complete analog of the main license (including the limitation on the number of accounts), but it has several specific features:

  * The server name in the license contains "Test". This name is displayed in all terminals.
  * [Activations of servers (#manage)](Activation.md#manage) installed under the test license cannot be set as main.



The following limitations apply to servers installed under the test license:

  * The server is not included in the list of available servers in the desktop terminal. To connect to the server, specify the access server address manually.
  * Connection to the server from mobile terminals and the [web terminal](../Platform-Components/WebTerminal.md) is not possible.
  * The server does not allow sending [push notifications](https://support.metaquotes.net/en/docs/mt5/manager/push_notifications) through the Manager terminal and API.
  * [Virtual hosting](https://www.mql5.com/en/vps) cannot be allocated for an account opened on the server with the test license.
  * An account opened on the server with the test license cannot be registered as a [trading signal](https://www.mql5.com/en/signals).



> For application development using [MetaTrader 5 API](https://support.metaquotes.net/en/docs/mt5/api), the platform provides [debug versions of the trading and history servers](https://support.metaquotes.net/en/articles/437) (regardless of the license type).
