[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederTranslate](../IMTConFeederTranslate.md) / AskMarkup

[Previous](BidMarkup.md) | [Next](Digits.md)

# IMTConFeederTranslate::AskMarkup

Get a correction to the Ask price arriving for a symbol from a data feed.

C++
    
    
    INT  IMTConFeederTranslate::AskMarkup()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConFeederTranslate.AskMarkup()

Python (Manager API)
    
    
    MTConFeederTranslate.AskMarkup

### Return Value

A correction to the Ask price arriving for a symbol from a data feed.

# IMTConFeederTranslate::AskMarkup

Set a correction to the Ask price arriving for a symbol from a data feed.

C++
    
    
    MTAPIRES  IMTConFeederTranslate::AskMarkup(
       const INT  markup      // Value of the Ask price correction
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederTranslate.AskMarkup(
       int        markup      // Value of the Ask price correction
       )

Python (Manager API)
    
    
    MTConFeederTranslate.AskMarkup

### Parameters

**markup**  
[in] The value of correction of the Ask price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
