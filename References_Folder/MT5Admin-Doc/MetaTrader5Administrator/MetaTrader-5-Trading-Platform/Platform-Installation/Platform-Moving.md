[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Installation](../Platform-Installation.md) / Platform Moving

[Previous](Console-Setup.md) | [Next](Platform-Uninstall.md)

# Platform migration to new hardware

If you move the platform to other hardware/hosting provider, in addition to proper platform installation and configuration, it is important to perform a number of actions to ensure uninterrupted service for traders.

## Migration via a backup server

The back-up server replicates the main server data in real time and features its full copy. At any time you can switch to using it manually — this is a quick and automatic procedure. In addition to emergency cases, the procedure can be used for migrating servers to new hardware.

[Install the backup server (#backup)](Installation.md#backup) on the computer, to which you plan to migrate the server. After installation, run it for a few days on the new hardware to make sure it operates well.

Restart the backup server right before you switch to it. This will help avoid loss of data [backed up once an hour](../Platform-Components/Backup-Server/Backup-Features.md). As long as the server copies data, its icon will display ![Backup in process](images/backup_server_backuping_icon.png)(the icon will look like![Backup in process](images/backup_server_backuping_icon2.png)). Wait until the process is completed and run the "![Switch to backup server](images/switch_to_bakcup_icon.png)Switch to backup server" command in the context menu:

![Switching to the backup server](images/switching_to_backup.png)

To avoid accidental switching, the platform requires an additional confirmation. In the dialog that appears, enter the required characters and click "Switch".

![Confirming the switching to the backup server](images/switch_to_backup_confirm.png)

After the procedure is complete, you will see that the main server and the backup server have swapped their places in the Network section:

Run the same procedure for all other history and trade servers. Then [install new backup servers (#backup)](Installation.md#backup) and [access servers (#access)](Installation.md#access). This can be conveniently done using the [fast deployment](Fast-Deployment.md) procedure.

  * Desktop terminals receive up-to-date information about access points during each account connection. It is recommended to keep at least one old access point operating during 1-2 weeks after migrating the platform to other equipment/hosting provider, so that terminals can receive such information.
  * Server migration must only be performed in non-trading hours. When switching to the backup server, it does not copy data which the main server continues to receive.
  * In order to prevent important data from being lost, trading operations and changes in the client base are not allowed on the main server right after the start of switching to the backup server. The ban is valid for one minute. If the platform fails to switch to a backup server within this period, the ban is removed.

  
---  
  
## Platform activation after migration

When migration is complete, go to "Services" menu and click "Start Live Update". Go to the [App Store\Licenses](https://support.metaquotes.net/en/market/licenses) section and make sure the activation is available in the list. Two types of platform [activations](Activation.md) are available: main and non-main.

  * Client terminals can only connect to a platform with the main activation.
  * To enable connections of client terminals to the platform, the platform sends information about its access points (installed access servers) to the server every hour. Information is sent to the server regardless of the activation type, but only access points of the main activation are transmitted to terminals.
  * Servers with non-main activation are not shown in the broker selection dialogs when opening accounts through terminals.



Thus, to ensure full-featured platform operation, you need to set the new activation as main. To do this, please contact [Service Desk](../Technical-Support.md) after completing platform installation.

## Update of Installers

When switching an activation to the main type, support specialists will recompile the client terminal installer for you, i.e. they will include new access points. If you distribute the installer file by yourself, be sure to download its new version from the [Download](https://support.metaquotes.net/en/download) section and update the file on your resources.

> To allow your traders to download the latest installer version any time, we recommend providing them direct terminal download links from the "Download" section. Thus, you will not need to update the files on your resources manually.
