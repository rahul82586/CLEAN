[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / FeedPassword

[Previous](FeedLogin.md) | [Next](GatewayServer.md)

# IMTConFeeder::FeedPassword

Get a password for the authorization of a data feed on the source server.

C++
    
    
    LPCWSTR  IMTConFeeder::FeedPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.FeedPassword()

Python (Manager API)
    
    
    MTConFeeder.FeedPassword

### Return Value

If successful, it returns a pointer to a string with a password for authorization on the source server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeeder](../IMTConFeeder.md) object.

# IMTConFeeder::FeedPassword

Set a password for the authorization of a data feed on the source server.

C++
    
    
    MTAPIRES  IMTConFeeder::FeedPassword(
       LPCWSTR  password      // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.FeedPassword(
       string   password      // Password
       )

Python (Manager API)
    
    
    MTConFeeder.FeedPassword

### Parameters

**password**  
[in] A password for authorization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum password length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
