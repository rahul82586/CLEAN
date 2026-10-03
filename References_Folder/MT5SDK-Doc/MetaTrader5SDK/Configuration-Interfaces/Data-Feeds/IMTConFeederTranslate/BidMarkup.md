[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederTranslate](../IMTConFeederTranslate.md) / BidMarkup

[Previous](Symbol.md) | [Next](AskMarkup.md)

# IMTConFeederTranslate::BidMarkup

Get a correction to the Bid price arriving for a symbol from a data feed.

C++
    
    
    INT  IMTConFeederTranslate::BidMarkup()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConFeederTranslate.BidMarkup()

Python (Manager API)
    
    
    MTConFeederTranslate.BidMarkup

### Return Value

A correction to the Bid price arriving for a symbol from a data feed.

# IMTConFeederTranslate::BidMarkup

Set a correction to the Bid price arriving for a symbol from a data feed.

C++
    
    
    MTAPIRES  IMTConFeederTranslate::BidMarkup(
       const INT  markup      // Value of the Bid price correction
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederTranslate.BidMarkup(
       int        markup      // Value of the Bid price correction
       )

Python (Manager API)
    
    
    MTConFeederTranslate.BidMarkup

### Parameters

**markup**  
[in] The value of correction of the Bid price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
