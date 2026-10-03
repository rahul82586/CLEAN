[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_network_backup_folders

[Previous](mt5-network-backup-servers.md) | [Next](mt5-firewall.md)

# mt5_network_backup_folders

Data on the [backed up custom directories (#folders)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#folders) is exported to this table. The table contains the following fields:

Name | Type | Description  
Folder_ID | Integer | Unique entry ID.  
Login | Integer | Backup server ID.  
Folder | String | The path to the backed up folder relative to the backup server installation directory.  
Masks | String | List of copied files (comma-separated). Files can be specified by masks.  
Filter | String | List of ignored files (comma-separated). Files can be specified by masks.
