[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / GatewayPassword

[Previous](GatewayLogin.md) | [Next](Mode.md)

# IMTConFeeder::GatewayPassword

Gets a password for the authorization of the history server on the gateway server.

C++
    
    
    LPCWSTR  IMTConFeeder::GatewayPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.GatewayPassword()

Python (Manager API)
    
    
    MTConFeeder.GatewayPassword

### Return Value

If successful, it returns a pointer to a string with a password for authorization on the data source. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeeder](../IMTConFeeder.md) object.

# IMTConFeeder::GatewayPassword

Sets a password for the authorization of the history server on the gateway server.

C++
    
    
    MTAPIRES  IMTConFeeder::GatewayPassword(
       LPCWSTR  password      // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.GatewayPassword(
       string   password      // Password
       )

Python (Manager API)
    
    
    MTConFeeder.GatewayPassword

### Parameters

**password**  
[in] Password for authentication on the data feed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The password must meet minimum security requirements (be no less than six symbols long and contain at least two of three symbols types: lower-case letters, upper-case letters or digits).
