[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / ToRangesClear

[Previous](ToRangesDelete.md) | [Next](ToRangesTotal.md)

# IMTMail::ToRangesClear

Clear the ranges of logins of email recipients.

C++
    
    
    MTAPIRES  IMTMail::ToRangesClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.ToRangesClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method clears all ranges of logins of email recipients.
