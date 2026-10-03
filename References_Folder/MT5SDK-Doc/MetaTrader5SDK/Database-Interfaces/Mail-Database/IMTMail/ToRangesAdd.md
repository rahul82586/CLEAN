[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / ToRangesAdd

[Previous](ToName.md) | [Next](ToRangesDelete.md)

# IMTMail::ToRangesAdd

Add a range of logins of email recipients.

C++
    
    
    MTAPIRES  IMTMail::ToRangesAdd(
       MTMailRange&  range       // A pointer to the structure of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.ToRangesAdd(
       ref MTMailRange   range       // A structure of the range
       )

### Parameters

**range**  
[in] A reference to theMTMailRange, structure that describes the range of recipients. The structure must be pre-filled. The structure must be pre-filled.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
