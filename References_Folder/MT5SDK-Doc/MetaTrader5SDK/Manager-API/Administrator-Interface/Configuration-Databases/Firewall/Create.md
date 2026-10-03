[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Create

[Previous](../Firewall.md) | [Next](Subscribe.md)

# IMTAdminAPI::FirewallCreate

Create an object of the firewall configuration.

C++
    
    
    IMTConFirewall*  IMTAdminAPI::FirewallCreate()

.NET
    
    
    CIMTConFirewall  CIMTAdminAPI.FirewallCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFirewall](../../../../Configuration-Interfaces/Firewall/IMTCon.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConFirewall::Release](../../../../Configuration-Interfaces/Firewall/IMTConFirewall/IMTCon-Release.md) method of this object.
