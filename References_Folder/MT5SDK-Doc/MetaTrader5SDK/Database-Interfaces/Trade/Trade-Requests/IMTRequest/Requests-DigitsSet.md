[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests DigitsSet

[Previous](Requests-Digits.md) | [Next](Requests-Action.md)

# IMTRequest::DigitsSet

Sets the number of decimal places in the trade request price.

C++
    
    
    MTAPIRES  IMTRequest::DigitsSet(
       const UINT  digits   // Number of decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.DigitsSet(
       uint        digits   // Number of decimal places
       )

### Program Parameters

**digits**  
[in] The number of decimal places in the trade request price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
