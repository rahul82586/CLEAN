[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / FeedLogin

[Previous](FeedServer.md) | [Next](FeedPassword.md)

# IMTConFeeder::FeedLogin

Get a login for the authorization of a data feed on the source server.

C++
    
    
    LPCWSTR  IMTConFeeder::FeedLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.FeedLogin()

Python (Manager API)
    
    
    MTConFeeder.FeedLogin

### Return Value

If successful, it returns a pointer to a string with login for authorization on the source server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeeder](../IMTConFeeder.md) object.

# IMTConFeeder::FeedLogin

Set a login for the authorization of a data feed on the source server.

C++
    
    
    MTAPIRES  IMTConFeeder::FeedLogin(
       LPCWSTR  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.FeedLogin(
       string   login      // Login
       )

Python (Manager API)
    
    
    MTConFeeder.FeedLogin

### Parameters

**login**  
[in] A login for authorization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum login length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
