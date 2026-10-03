[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGetByGroup

[Previous](PositionGet.md) | [Next](PositionGetByLogins.md)

# IMTManagerAPI::PositionGetByGroup

Get all currently opened positions for one or several client groups.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGetByGroup(
       LPCWSTR            mask,      // group mask
       IMTPositionArray*  positions  // object of the array of positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGetByGroup(
       String^            mask,      // group mask
       CIMTPositionArray  positions  // object of the array of positions
       )

Python
    
    
    ManagerAPI.PositionGetByGroup(
       mask               # group mask
       )
    
    
    ManagerAPI.PositionGetByGroupCSV(
       mask,              # group mask
       fields             # comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionGetByGroupNumPy(
       mask,              # group mask
       fields             # comma-separated list of required fields
       )

### Parameters

**mask**  
[in] The groups the positions are requested for. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**positions**  
[out] An object of positions array. The 'positions' object should be first created usingIMTManagerAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies the data on all open positions belonging to clients in the specified groups to the 'positions' object. The method works only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
