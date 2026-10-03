[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerBackupFolderCreate

[Previous](NetServerAddressRangeCreate.md) | [Next](NetServerSubscribe.md)

# IMTServerAPI::NetServerBackupFolderCreate

Create an object describing the user directory to back up.
    
    
    IMTConBackupFolder*  IMTServerAPI::NetServerBackupFolderCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConBackupFolder](../../../../Configuration-Interfaces/Network/IMTConBackupFolder.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConBackupFolder::Release](../../../../Configuration-Interfaces/Network/IMTConBackupFolder/Release.md) method of this object.
