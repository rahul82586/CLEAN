[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Create

[Previous](../Firewall.md) | [Next](Subscribe.md)

# IMTServerAPI::FirewallCreate

Create an object of the firewall configuration.
    
    
    IMTConFirewall*  IMTServerAPI::FirewallCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFirewall](../../../../Configuration-Interfaces/Firewall/IMTCon.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConFirewall::Release](../../../../Configuration-Interfaces/Firewall/IMTConFirewall/IMTCon-Release.md) method of this object.
