[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Flags

[Previous](Mode.md) | [Next](Keywords.md)

# IMTConFeeder::Flags

Get the type of information transmitted by the data feed.

C++
    
    
    UINT  IMTConFeeder::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnFeedersFlags  CIMTConFeeder.Flags()

Python (Manager API)
    
    
    MTConFeeder.Flags

### Return Value

One of the values of the [IMTConFeeder::EnFeedersFlags (#enfeederflags)](Enumerations.md#enfeederflags) enumeration.

# IMTConFeeder::Flags

Set the type of information transmitted by the data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::Flags(
       const UINT      flags  // Type of information
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Flags(
       EnFeedersFlags  flags  // Type of information
       )

Python (Manager API)
    
    
    MTConFeeder.Flags

### Parameters

**flags**  
[in] TheIMTConFeeder::EnFeedersFlagsenumeration is used to pass the operation mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
