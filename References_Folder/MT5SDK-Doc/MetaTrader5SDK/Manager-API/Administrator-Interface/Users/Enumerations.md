[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / Enumerations

[Previous](../Users.md) | [Next](UserCreate.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The following enumerations are available for working with users in IMTAdminAPI:

  * [IMTAdminAPI::EnExternalSyncModes (#enexternalsyncmodes)](Enumerations.md#enexternalsyncmodes)



<a id="enexternalsyncmodes"></a>
## IMTAdminAPI::EnExternalSyncModes (#enexternalsyncmodes)

Modes of synchronizing client's trading status with an external system are enumerated in IMTAdminAPI::EnExternalSyncModes.

ID | Value | Description  
EXTERNAL_SYNC_ALL | 0 | Full synchronization of trading status including current pending orders, open positions and balance.  
EXTERNAL_SYNC_BALANCE | 1 | Synchronizing balance.  
EXTERNAL_SYNC_POSITIONS | 2 | Synchronizing open positions.  
EXTERNAL_SYNC_ORDERS | 3 | Synchronizing current pending orders.  
EXTERNAL_SYNC_LAST |  | End of enumeration. It corresponds to EXTERNAL_SYNC_ORDERS.  
  
The enumeration is used in [IMTAdminAPI::UserExternalSync](UserExternalSync.md) method.
