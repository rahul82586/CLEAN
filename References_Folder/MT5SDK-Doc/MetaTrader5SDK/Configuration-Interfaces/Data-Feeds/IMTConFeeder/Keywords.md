[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Keywords

[Previous](Flags.md) | [Next](Categories.md)

# IMTConFeeder::Keywords

Get the key words for the news received from a data feed.

C++
    
    
    LPCWSTR  IMTConFeeder::Keywords()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.Keywords()

Python (Manager API)
    
    
    MTConFeeder.Keywords

### Return Value

Key words for the news received from a data feed.

### Note

This method is reserved for future use and is not currently implemented.

# IMTConFeeder::Keywords

Set the key words for the news received from a data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::Keywords(
       LPCWSTR  keywords      // Keywords
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Keywords(
       string   keywords      // Keywords
       )

Python (Manager API)
    
    
    MTConFeeder.Keywords

### Parameters

**keywords**  
[in] Key words separated by a comma.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is reserved for future use and is not currently implemented.
