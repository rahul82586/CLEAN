[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Module

[Previous](Name.md) | [Next](FeedServer.md)

# IMTConFeeder::Module

Get the name of the data feed module.

C++
    
    
    LPCWSTR  IMTConFeeder::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.Module()

Python (Manager API)
    
    
    MTConFeeder.Module

### Return Value

If successful, it returns a pointer to a string with the name of the data feed module. Otherwise, it returns NULL.

### Note

It returns the name of the module (exe-file) that corresponds to the data feed.

# IMTConFeeder::Module

Set the name of the data feed module.

C++
    
    
    MTAPIRES  IMTConFeeder::Module(
       LPCWSTR  name      // The name of the data feed module
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Module(
       string   name      // The name of the data feed module
       )

Python (Manager API)
    
    
    MTConFeeder.Module

### Parameters

**name**  
[in] The name of the data feed module.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
