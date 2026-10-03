[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ClientOriginLogin

[Previous](ClientOrigin.md) | [Next](ClientExternalID.md)

# IMTClient::ClientOriginLogin

Get the trading account number, based on which the client was created.

C++
    
    
    UINT64  IMTClient::RecordID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTClient.RecordID()

### Return Value

Trading account number.

# IMTClient::RecordID

Set the trading account number, based on which the client was created.

C++
    
    
    MTAPIRES  IMTClient::Login(
       const UINT64  login      // Account number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.Login(
       ulong         login      // Account number
       )

### Parameters

**login**  
[in] Trading account number. The account number is equal toIMTUser::Login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
