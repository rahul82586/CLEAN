[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Name

[Previous](Clear.md) | [Next](Module.md)

# IMTConFeeder::Name

Gets the name of the data feed.

C++
    
    
    LPCWSTR  IMTConFeeder::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.Name()

Python (Manager API)
    
    
    MTConFeeder.Name

### Return Value

If successful, it returns a pointer to a string with the name of the data feed. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeeder](../IMTConFeeder.md) object.

# IMTConFeeder::Name

Sets the name of the data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::Name(
       LPCWSTR  name      // Data feed name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Name(
       srting   name      // Data feed name
       )

Python (Manager API)
    
    
    MTConFeeder.Name

### Parameters

**name**  
[in] The name of a data feed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
