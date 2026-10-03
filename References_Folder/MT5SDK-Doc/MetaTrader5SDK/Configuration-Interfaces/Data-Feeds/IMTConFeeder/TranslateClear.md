[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TranslateClear

[Previous](TranslateDelete.md) | [Next](TranslateShift.md)

# IMTConFeeder::TranslateClear

Clear the list of data conversion parameters of a data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::TranslateClear()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TranslateClear()

Python (Manager API)
    
    
    MTConFeeder.TranslateClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of symbols of a data feed.
