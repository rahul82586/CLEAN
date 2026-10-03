[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Client Connection](../Client-Connection.md) / ClientAllowIP

[Previous](ClientAdd.md) | [Next](../Quote-and-News-Feeds.md)

# IMTGatewayAPI::ClientAllowIP

Adding permission for the connection from a specified IP address.

C++
    
    
    MTAPIRES  IMTGatewayAPI::ClientAllowIP(
       LPCWSTR  address      // IP address
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.ClientAllowIP(
       string   address      // IP address
       )

### Parameters

**address**  
[in] IP address, from which connection must be allowed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

By default, connection from any IP addresses is allowed. In case at least one address is added, connections from all addresses, except from the added ones, are forbidden.
