[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / Pumping Modes

[Previous](../Connection-to-the-Server.md) | [Next](Connect.md)

# Pumping Mode

Enabled pumping mode means that the application will synchronize the appropriate server database with a locally created database. Possible pumping modes are enumerated in IMTAdminAPI::EnPumpModes. The pumping mode in which we want to connect is specified in the pump_mode parameter of the [IMTAdminAPI::Connect](Connect.md) method.

ID | Value | Description  
PUMP_MODE_MAIL | 0x00000004 | Mail pumping.  
PUMP_MODE_NEWS | 0x00000020 | News pumping.  
PUMP_MODE_FULL | 0xffffffff | News and mail pumping.  
  
> The pumping mode does not affect the operation of those methods, which request data directly from the server (such as [IMTAdminAPI::UserRequest](../Users/UserRequest.md), [IMTAdminAPI::OrderRequest](../Trade-Databases/Orders/OrderRequest.md) etc.). Such methods can be used in any pumping mode.
