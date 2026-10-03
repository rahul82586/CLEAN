[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / Enumerations

[Previous](../Users.md) | [Next](UserCreate.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The following enumerations are available for working with users in IMTManagerAPI:

  * [IMTManagerAPI::EnExternalSyncModes (#enexternalsyncmodes)](Enumerations.md#enexternalsyncmodes)



<a id="enexternalsyncmodes"></a>
## IMTManagerAPI::EnExternalSyncModes (#enexternalsyncmodes)

Modes of synchronizing client's trading status with an external system are enumerated in IMTManagerAPI::EnExternalSyncModes.

ID | Value | Description  
EXTERNAL_SYNC_ALL | 0 | Full synchronization of trading status including current pending orders, open positions and balance.  
EXTERNAL_SYNC_BALANCE | 1 | Synchronizing balance.  
EXTERNAL_SYNC_POSITIONS | 2 | Synchronizing open positions.  
EXTERNAL_SYNC_ORDERS | 3 | Synchronizing current pending orders.  
EXTERNAL_SYNC_LAST |  | End of enumeration. It corresponds to EXTERNAL_SYNC_ORDERS.  
  
The enumeration is used in [IMTManagerAPI::UserExternalSync](UserExternalSync.md) method.
