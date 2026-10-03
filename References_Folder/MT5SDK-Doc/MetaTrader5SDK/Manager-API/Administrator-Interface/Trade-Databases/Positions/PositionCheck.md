[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionCheck

[Previous](PositionBackupRestore.md) | [Next](PositionFix.md)

# IMTAdminAPI::PositionCheck

Checking the correctness of a client's positions based on the history of deals.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionCheck(
       const UINT64       login,        // The user's login
       IMTPositionArray*  current,      // Current positions
       IMTPositionArray*  invalid,      // Unmatched positions
       IMTPositionArray*  missed,       // Missing positions
       IMTPositionArray*  nonexist      // Odd positions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionCheck(
       ulong              login,        // The user's login
       CIMTPositionArray  current,      // Current positions
       CIMTPositionArray  invalid,      // Unmatched positions
       CIMTPositionArray  missed,       // Missing positions
       CIMTPositionArray  nonexist      // Odd positions
       )

Python
    
    
    AdminAPI.PositionCheck(
       int                login         # The user's login
       )

### Parameters

**login**  
[in] The login of a user.

**current**  
[out] An array of the client's current positions.

**invalid**  
[out] During the check, the platform calculates what positions a client should have based on his history of trades. Calculated positions are compared with actual ones. If the calculate list contains positions that do not match actual positions, such records will be passed to the invalid array.

**missed**  
[out] Positions that were calculated based on the client's history and that are not found among actual positions are placed into this array. In other words, missing positions are placed into the 'missed' array.

**nonexist**  
[out] The client's actual positions that are not found in the calculated list based on the history of deals are added to this array. In other words, the client's odd positions that do not exist in the history are added to the 'nonexist' array.

### Return Value

An indication of a successful check is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Disclaimer

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code does not indicate that the client;s positions are correct. Positions can be considered correct if you receive the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) code and empty 'invalid', 'missed' and 'nonexsit' arrays.
