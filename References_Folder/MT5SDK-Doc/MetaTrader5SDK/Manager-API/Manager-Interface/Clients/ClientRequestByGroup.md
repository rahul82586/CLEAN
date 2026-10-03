[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientRequestByGroup

[Previous](ClientRequest.md) | [Next](ClientRequestHistory.md)

# IMTManagerAPI::ClientRequestByGroup

Get clients by groups.

C++
    
    
    MTAPIRES  IMTManagerAPI::ClientRequestByGroup(
       LPCWSTR          groups,  // groups
       IMTClientArray*  clients  // object of clients array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ClientRequestByGroup(
       string           groups,  // groups
       CIMTClientArray  clients  // object of clients array
       )

Python
    
    
    ManagerAPI.ClientRequestByGroup(
       str              groups   # groups
       )

### Parameters

**groups**  
[in] The preferred group (TradingGroup) specified for the client. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex. The following clients are returned when filter by groups is used:

**clients**  
[out] An object of an array of clients. The 'clients' object must be previously created using theIMTManagerAPI::ClientCreateArraymethod.

  * Clients for whom TradingGroup is specified and this group corresponds to the request mask
  * Clients for whom TradingGroup is not specified, but there is at least one [bound account](../../../Web-API/Manager-Interface-(Rest-API)/Clients/Bind-Account.md) from the requested group
  * Clients for whom TradingGroup is not specified and there are no bound accounts (to prevent the clients from being lost)



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
