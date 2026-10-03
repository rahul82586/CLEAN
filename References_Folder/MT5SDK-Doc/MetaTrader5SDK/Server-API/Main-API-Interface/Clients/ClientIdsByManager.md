[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientIdsByManager

[Previous](ClientIdsByGroup.md) | [Next](ClientUserAdd.md)

# IMTServerAPI::ClientIdsByManager

Get the list client identifiers available to the manager.
    
    
    MTAPIRES  IMTServerAPI::ClientIdsByManager(
       const UINT64   manager,   // Manager
       UINT64*&       ids,       // Array of identifiers
       UINT&          ids_total  // Number of identifiers
       )

### Parameters

**manager**  
[in] The login of the manager whose clients you wish to obtain.A client record is available to the manager if one of the following conditions is met:

**ids**  
[out] An array with client identifiers in the server database (IMTClient::RecordID).

**ids_total**  
[out] The number of identifiers in the 'ids' array.

  * The client is created by this manager
  * The client is explicitly assigned to the manager ([IMTClient::AssignedManager](../../../Database-Interfaces/Clients/IMTClient/AssignedManager.md))
  * The preferred trading group ([IMTClient::TradingGroup](../../../Database-Interfaces/Clients/IMTClient/TradingGroup.md)) set for the client is available to the manager (the manager has [permissions for the group](../../../Configuration-Interfaces/Managers/IMTConManager/GroupAdd.md))


  * Any of the [trading accounts bound to the client](ClientUserAdd.md) is available to the manager (the manager has [permissions for the group](../../../Configuration-Interfaces/Managers/IMTConManager/GroupAdd.md) in which the account is located)



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

The method allocates and fills an array of identifiers. A pointer to the passed block is placed to the 'ids' parameter. After use, the array placed in the 'ids' variable must be released using the [IMTServerAPI::Free](../Common-Functions/Free.md) Server API method.
