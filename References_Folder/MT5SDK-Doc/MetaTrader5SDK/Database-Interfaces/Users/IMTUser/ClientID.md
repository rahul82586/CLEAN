[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / ClientID

[Previous](MQID.md) | [Next](VisitorID.md)

# IMTUser::ClientID

Get the client ID with which the trading account is associated.

C++
    
    
    UINT64  IMTUser::ClientID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTUser.ClientID()

### Return Value

The ID of the client to whom the trading account corresponds. The client ID is equal to the [IMTClient::RecordID](../../Clients/IMTClient/RecordID.md) value.

# IMTUser::ClientID

Set the client ID with which the trading account is associated.

C++
    
    
    MTAPIRES  IMTUser::ClientID(
       const UINT64  id         // Client ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ClientID(
       ulong         id         // Client ID
       )

### Program Parameters

**id**  
[in] Client ID with which the trading account is associated. The client ID is equal to theIMTClient::RecordIDvalue.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
