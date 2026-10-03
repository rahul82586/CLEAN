[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / MQID

[Previous](ID.md) | [Next](ClientID.md)

# IMTUser::MQID

Gets the client's MetaQuotes ID.

C++
    
    
    LPCWSTR  IMTUser::MQID(
       MTAPISTR&  mqid      // MetaQuotes ID
       )

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.MQID()

### Parameters

**mqid**  
[out] A string with the client's MetaQutes ID.

### Return Value

A pointer to the mqid string passed as a parameter.

### Note

MetaQuotes ID is a unique identifier of the mobile client terminal (MetaTrader 4/5 for iPhone and Android), which is used to send push notifications directly to the client.
