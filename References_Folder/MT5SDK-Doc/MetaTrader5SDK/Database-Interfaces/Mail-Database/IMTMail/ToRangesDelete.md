[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / ToRangesDelete

[Previous](ToRangesAdd.md) | [Next](ToRangesClear.md)

# IMTMail::ToRangesDelete

Delete a range of logins of email recipients by the index.

C++
    
    
    MTAPIRES  IMTMail::ToRangesDelete(
       const UINT  pos      // Position of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.ToRangesDelete(
       uint        pos      // Position of the range
       )

### Parameters

**pos**  
[in] Position of the range of logins, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
