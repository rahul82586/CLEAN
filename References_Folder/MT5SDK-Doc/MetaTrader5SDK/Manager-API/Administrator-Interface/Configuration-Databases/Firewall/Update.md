[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Update

[Previous](Unsubscribe.md) | [Next](UpdateBatch.md)

# IMTAdminAPI::FirewallUpdate

Add or update a firewall configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::FirewallUpdate(
       IMTConFirewall*  config      // Firewall configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FirewallUpdate(
       CIMTConFirewall  config      // Firewall configuration object
       )

Python
    
    
    AdminAPI.FirewallUpdate(
       config           # Firewall configuration object
       )

### Parameters

**config**  
[in] The firewall configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.

Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT_RET_ERR_PARAMS](../../../../Return-Codes/Common-errors.md) is returned.
