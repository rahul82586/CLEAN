[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupLastSync

[Previous](BackupFlags.md) | [Next](BackupLastStartup.md)

# IMTConServerBackup::BackupLastSync

Get the time of the last data synchronization with the primary server.

C++
    
    
    INT64  IMTConServerBackup::BackupLastSync()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerBackup.BackupLastSync()

### Return Value

The time of the last data synchronization in seconds since 01.01.1970.
