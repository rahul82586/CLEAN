[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerBackupFolderCreate

[Previous](NetServerClusterStateCreate.md) | [Next](NetServerSubscribe.md)

# IMTAdminAPI::NetServerBackupFolderCreate

Create an object describing the user directory to back up.

C++
    
    
    IMTConBackupFolder*  IMTAdminAPI::NetServerBackupFolderCreate()

.NET
    
    
    CIMTConBackupFolder  CIMTAdminAPI::NetServerBackupFolderCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConBackupFolder](../../../../Configuration-Interfaces/Network/IMTConBackupFolder.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConBackupFolder::Release](../../../../Configuration-Interfaces/Network/IMTConBackupFolder/Release.md) method of this object.
