[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / ToRangesNext

[Previous](ToRangesTotal.md) | [Next](Time.md)

# IMTMail::ToRangesNext

Get a range of logins of email recipients by the index.

C++
    
    
    MTAPIRES  IMTMail::ToRangesNext(
       const UINT        pos,      // Position of the range
       MTMailRange&      range     // A pointer to the structure of the range
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.ToRangesNext(
       uint              pos,      // Position of the range
       out MTMailRange   range     // A structure of the range
       )

### Parameters

**pos**  
[in] Position of the range of logins, starting with 0.

**range**  
[out] A reference to theMTMailRangestructure that describes the range of recipients.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
