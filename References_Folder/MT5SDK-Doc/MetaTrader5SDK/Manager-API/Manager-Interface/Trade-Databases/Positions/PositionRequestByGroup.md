[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByGroup

[Previous](PositionRequest.md) | [Next](PositionRequestByGroupSymbol.md)

# IMTManagerAPI::PositionRequestByGroup

Request from the server open positions related to a client group.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionRequestByGroup(
       LPCWSTR            group,         // Group
       IMTPositionArray*  positions      // An object of positions array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionRequestByGroup(
       string             mask,          // Group
       CIMTPositionArray  positions      // An object of positions array
       )

Python
    
    
    ManagerAPI.PositionRequestByGroup(
       mask               # Group
       )
    
    
    ManagerAPI.PositionRequestByGroupCSV(
       mask,              # Group
       fields             # An object of positions array
       )
    
    
    ManagerAPI.PositionRequestByGroupNumPy(
       mask,              # Group
       fields             # An object of positions array
       )

### Parameters

**group**  
[in] The groups the positions are requested for. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex. The maximum length of the string is 127 characters.

**positions**  
[out] An object of the array of trade positions. The 'position' object must be first created using theIMTManagerAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'positions' object the data of all open positions belonging to clients in the specified groups.
