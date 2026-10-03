[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Backup Server](../Backup-Server.md) / Backup Features

[Previous](../Backup-Server.md) | [Next](Switching-to.md)

<a id="backup-features"></a>
# Backup Features (#backup-features)

All critical trade and history server data is backed up in real time. Some non-critical trade server data, as well as history server data are backed up every hour. Critical and non-critical data are displayed in the table below:

Data | Trade server | History server  
Critical (real time backup) | User base Order base Deal base Configuration databases | Trade execution base (executions) and custom settings (settings.dat) of running gateways Tick flow  
Non-critical (backup every hour) | mt5sendmail64.exe and mt5trade64.exe files Plugins (DLL, INI, DAT files including subdirectories) Reports (DLL, INI files without subdirectories) Templates (HTML, HTM files without subdirectories) | mt5history(64).exe file Gateways and data feeds (EXE, DLL, INI, DAT, JAR, CMD, BAT, PS1,VBS and PY files including subdirectories) Plugins (DLL, INI, DAT files including subdirectories)  
User directories and files specified in the [Folders (#folders)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#folders) section in backup server settings  
Non-critical (backup every five hours) | Archive databases Mail database Daily report database | Minute bar history  
Non-critical (backup every 24 hours) |  | Tick history  
  
The installation directory of the backup server contains the same folders as the server, whose backups it creates, except for the logs folder that contains the journal entries and crash logs of the backup server itself. In addition, the following executable files are available in the directory:

  * mt5srvupdater64.exe — the executable file of the live update system of the backup server;
  * mt5backup64.exe — the executable file of the backup server.



<a id="file"></a>
## Periodic file backup (#file)

Apart from synchronizing with the main server in real time, the backup server creates database file copies on the disk for certain points in time. The path for saving files and the creation time are set in the [backup server settings (#enable-backups)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#enable-backups).

To save time and disk space, backups are performed incrementally:

  * The first copy is made for all data of the backed up server. That copy is placed to ["[Backups path (#enable-backups)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#enable-backups)"]\base\\. The folder and file structure there fully matches the one of the backed up server.
  * Each subsequent day (hour of 4 hours, depending on the "[Additional backups (#archive-backup-period)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#archive-backup-period)"), an incremental copy of the data is created. Such a copy contains only the changes as compared to the first (base) copy. Such copies are placed to ["[Backups path (#enable-backups)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#enable-backups)"]\\[YYYY.MM.DD_HH.MM.SS]\\.



Thus, the server does not need to copy all the data during each backup.

Let us consider an example with a trade database. Backup was enabled on 2019.11.06. The server created a database copy on this day. It is shown on the left in the figure below. The entire history of deals is contained under the 'base' directory. It is divided by months and is presented as ZIP files. During the next day, traders performed deals through the platform, as well as the administrator edited a trade which was executed in January 2019. The next day, the backup server created an incremental copy in the catalog 2019.11.07_17.10.00 (on the right). You can see that only two ZIP archives are included in the incremental copy directory, i.e. those which have changed relative to the base copy:

![Trade database backup example: base copy and incremental copy](images/backup_base_increment.png)

The server is able to automatically delete old copies to ensure that the backups do not take up all the free disk space over time. The storage depth is set by the "[Keep backups (#enable-backups)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#enable-backups)" parameter in the backup server settings. When deleting an old backup copy, it is preliminarily applied to the main one. In fact, its files are combined with the files from the "base" directory. After that, the "base" directory will have the same status as the databases on the server at the time of creation of the deleted incremental copy. Subsequent incremental copies will already be created relative to the new base copy. This approach also reduces the amount of data copied during backup.

Let us consider this procedure using the previous example. Suppose, the "Keep backups" parameter is set to "3 days".

  * The backup was enabled on 2019.11.06 and the server created a backup copy ("base" folder). the following three days, the server was creating incremental copies in separated directories.
  * On 2019.11.11, when it is time to create the next copy, the server copies data from the incremental archive of 2019.11.07 into the base copy.



![Before deletion, the incremental copy is merged with the base copy](images/backup_base_increment_merge_1.png)

Then, the incremental archive of 2019.11.07 is deleted, while the incremental archive dated 2019.11.11 is created based on the updated base copy:

![The old incremental copy is deleted, the new one is created based on the updated base copy](images/backup_base_increment_merge_2.png)

> In addition to backup copies, the server saves the "mt5backupinfo.txt" file under the directory [backup server installation directory]\base\\. The file contains backup service information. Do not delete or modify this file. The file is not required for [database recovery (#restore)](Backup-Features.md#restore), so there is no need to copy it.

The ["Enable backups" (#enable-backups)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#enable-backups) parameter allows you to completely disable creating backup copies on the disk. The backup server status synchronization with the main one is not disabled. The backup server still remains its full copy. Disabling creation of copies on the disk may be needed if the backup server is used only to [export data to SQL](SQL-Export.md).

<a id="working-with-file-copies"></a>
### Working with file copies (#working-with-file-copies)

If you want to save the database status as of a certain point in time (for example, in order to move it to the long-term archive on another server), simply copy the basic and incremental copies for the desired date. Together, they represent the complete database status of the backed up server as of the certain point in time.

To request data from a file copy, go to the necessary section of MetaTrader 5 Administrator ([Orders (#backup)](../../Platform-Setup/Orders.md#backup), [Deals (#backup)](../../Platform-Setup/Deals.md#backup), [Positions (#backup)](../../Platform-Setup/Positions.md#backup), [Accounts](../../Platform-Setup/Accounts/Archive-and-Backup-Bases.md)) and select a copy for the desired date in the query line. The terminal collects and presents data from the basic and selected incremental copies. Such requests actually restore the state of the database as at the selected point in time.

<a id="restore"></a>
### Database recovery for a specific date (#restore)

To restore server databases as on a specific date, stop all the servers within the cluster. Next, unzip and copy the necessary databases from the \base\ directory of the backup server to the corresponding directories of the primary server.

![Unzip and copy files from the 'base' directory to the main server](images/backup_restore_base.png)

Then unzip and copy the required data from the incremental copy directory for the desired date (its format is [YYYY.MM.DD_HH.MM.SS]) to the relevant directories of the main server.

![Unzip and copy files from the incremental copy to the main server](images/backup_restore_increment.png)

> It is not recommended to restore trading databases separately. Orders, deals and positions are interrelated and should match each other.

<a id="journal"></a>
## Moving the current day logs (#journal)

The backup server is a copy of the backed up one since it stores the same data and features the same file and directory structure. In particular, it stores its logs in directories and files with the same names (Logs\*.log)

The special mechanism prevents mixing of the both servers' current day logs when [switching to the backup server](Switching-to.md).

When switching the servers, the current day log file of the previous backed up server is renamed by adding the .failover extension to its name. The backup server to replace it starts keeping the current day log from scratch. The *.failover file is generated only at the previous backed up server. The server, to which the switching is performed, simply creates its log file from scratch.

If a reverse switching is performed the same day, the .failover file is renamed back to .log and the backup server goes on keeping the log in it.

Let's consider an example of switching the main trade server to the backup one and vice versa.

Contents of \MainTrade\logs\ | Contents of \Backup\logs\  
---|---  
Current day log: 20170330.log  
  
first entry: 10:56:16.265 Startup service start initialized   
last entry: 10:57:55.421 Exit shutdown finished | Current day log: 20170330.log  
  
first entry: 10:56:16.265 Startup service start initialized   
last entry: 10:56:17.888 192.168.0.131 Config: network config synchronized  
Switching the servers, the backup server is active here now | Switching the servers, the trade server is active here now  
The previous trade server log is renamed to 20170330.log.failover:  
  
first entry: 10:56:16.265 Startup service start initialized   
last entry: 10:57:55.421 Exit shutdown finished  
The new file of the backup server log: 20170330.log  
  
first entry: 10:57:52.507 Startup service start initialized   
last entry: 10:57:55.401 192.168.0.131 Config: network config synchronized | The new file of the trade server log 20170330.log:  
  
first entry: 10:57:52.507 Startup service start initialized   
last entry: 11:02:28.433 Exit shutdown finished  
  
  
Reverse switching, the trade server is active here again | Reverse switching, the backup server is active here again  
20170330.log.failover is renamed back to 20170330.log and the new trade server entries are added to it:  
  
first entry: 10:56:16.265 Startup service start initialized   
10:57:55.421 Exit shutdown finished   
11:02:25.454 Startup service start initialized   
last entry: 11:04:01.157 192.168.0.131 Config: network config synchronized | The previous trade server log is renamed to 20170330.log.failover:  
  
first entry: 10:57:52.507 Startup service start initialized   
last entry: 11:02:28.433 Exit shutdown finished  
The backup server resumes adding entries in its former 20170330.log file:  
  
first entry: 10:56:16.265 Startup service start initialized   
last entry: 11:04:01.157 192.168.0.131 Config: network config synchronized  
  
<a id="emergency-situations-during-the-backup-process"></a>
## Emergency Situations During the Backup Process (#emergency-situations-during-the-backup-process)

Creation of backup copies by the server can be tracked by its [journal](../../Platform-Setup/Network-cluster/Journal.md). This section contains examples of journal entries describing emergency situations during backup.

2012.06.13 17:19:57 TradeOrders: invalid index header timestamp  
---  
  
Such a journal entry means that orders base index (order.idx) does not correspond to the orders base data (order.dat). A possible reason for such entry may be a backup server abnormal shutdown (for example, power cut or server manual shutdown).

This situation is not dangerous. The backup server will reconstruct the index and continue its operation. The data in the database remains fully intact. However, the reason of the abnormal server shutdown should be found out.

2012.06.13 17:19:57 TradeDeals: deals_2012.06.dat: base has invalid hash  
---  
  
This entry indicates that the deals base on a backup server differs from the one on a trading server after synchronization. In this case, the backup server will remove the indicated base and synchronize it again.

Such backup server journal entries are permissible for deals base (deals_*) after weekends (when databases optimization compaction are performed on the main server). The reason is that a backup server cannot always synchronize a month deals base in saving mode (delete the entries that were deleted during a trading server optimization) after optimizing the base on a trading server. In that case, the backup server performs the full database synchronization.

For the rest of the databases such a situation is not acceptable in any time.
