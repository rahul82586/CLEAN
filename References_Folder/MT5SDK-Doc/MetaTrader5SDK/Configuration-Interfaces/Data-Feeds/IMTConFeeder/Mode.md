[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Mode

[Previous](GatewayPassword.md) | [Next](Flags.md)

# IMTConFeeder::Mode

Get the data feed operation mode.

C++
    
    
    UINT  IMTConFeeder::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnFeedersMode  CIMTConFeeder.Mode()

Python (Manager API)
    
    
    MTConFeeder.Mode

### Return Value

One of the values of the [IMTConFeeder::EnFeedersMode (#enfeedersmode)](Enumerations.md#enfeedersmode) enumeration.

# IMTConFeeder::Mode

Set the data feed operation mode.

C++
    
    
    MTAPIRES  IMTConFeeder::Mode(
       const UINT     mode   // Operation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Mode(
       EnFeedersMode  mode   // Operation mode
       )

Python (Manager API)
    
    
    MTConFeeder.Mode

### Parameters

**mode**  
[in] TheIMTConFeeder::EnFeedersModeenumeration is used to pass the operation mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
