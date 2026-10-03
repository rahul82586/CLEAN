[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Network](../Network.md) / IMTConServerBackup

[Previous](IMTConServerHistory/NewsMax.md) | [Next](IMTConServerBackup/Enumerations.md)

# IMTConServerBackup

The IMTConServerBackup interface contains methods for managing settings that are specific to Backup Servers.

Method | Purpose  
---|---  
[Release](IMTConServerBackup/Release.md) | Delete the current object.  
[Assign](IMTConServerBackup/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConServerBackup/Clear.md) | Clear an object.  
[MasterServer](IMTConServerBackup/MasterServer.md) | Get and set the server ID to backup.  
[BackupPath](IMTConServerBackup/BackupPath.md) | Get and set the path to save backups.  
[BackupFullTime](IMTConServerBackup/BackupFullTime.md) | Get and set the time of creating full backup copies.  
[BackupPeriod](IMTConServerBackup/BackupPeriod.md) | Get and set the frequency of backup creation.  
[BackupTTL](IMTConServerBackup/BackupTTL.md) | Get and set the period of backup keeping.  
[BackupFlags](IMTConServerBackup/BackupFlags.md) | Gets and sets backup flags.  
[BackupLastSync](IMTConServerBackup/BackupLastSync.md) | Get the time of the last data synchronization with the primary server.  
[BackupLastStartup](IMTConServerBackup/BackupLastStartup.md) | Get the creation time of the last database startup copy.  
[BackupLastFull](IMTConServerBackup/BackupLastFull.md) | Get the creation time of the last file copy of all databases.  
[BackupLastArchive](IMTConServerBackup/BackupLastArchive.md) | Get the creation time of the last additional file copy.  
[SQLExportMode](IMTConServerBackup/SQLExportMode.md) | Get and set the mode of data export to an SQL database.  
[SQLExportFlags](IMTConServerBackup/SQLExportFlags.md) | Get and set additional settings of data export to an SQL database.  
[SQLExportPeriod](IMTConServerBackup/SQLExportPeriod.md) | Get and set the frequency of price and profit data export.  
[SQLExportServer](IMTConServerBackup/SQLExportServer.md) | Get and set the address of the server, on which the database is installed.  
[SQLExportLogin](IMTConServerBackup/SQLExportLogin.md) | Get and set the login for connecting to an SQL database.  
[SQLExportPassword](IMTConServerBackup/SQLExportPassword.md) | Get and set the password for connecting to an SQL database.  
[SQLExportFolder](IMTConServerBackup/SQLExportFolder.md) | Get and set the name of the SQL database, to which data is exported.  
[SQLExportLastSync](IMTConServerBackup/SQLExportLastSync.md) | Get the time of the last full synchronization of databases and platform configurations with the SQL database.  
[FoldersAdd](IMTConServerBackup/FoldersAdd.md) | Add a custom folder to the backup directories list.  
[FoldersUpdate](IMTConServerBackup/FoldersUpdate.md) | Change a custom folder in the backup directories list.  
[FoldersDelete](IMTConServerBackup/FoldersDelete.md) | Delete a custom folder from the backup directories list.  
[FoldersClear](IMTConServerBackup/FoldersClear.md) | Clear the list of custom folders for which backup is enabled.  
[FoldersShift](IMTConServerBackup/FoldersShift.md) | Move the backuped custom folder in the list.  
[FoldersTotal](IMTConServerBackup/FoldersTotal.md) | Get the number of custom folders for which backup is enabled.  
[FoldersNext](IMTConServerBackup/FoldersNext.md) | Get a backuped custom folder by index.  
  
The IMTConServerBackup class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnBackupFlags (#enbackupflags)](IMTConServerBackup/Enumerations.md#enbackupflags) | Backup flags.  
[EnBackupPeriod (#enbackupperiod)](IMTConServerBackup/Enumerations.md#enbackupperiod) | Frequency of the backups.  
[EnBackupTTL (#enbackupttl)](IMTConServerBackup/Enumerations.md#enbackupttl) | Period to keep backups.
