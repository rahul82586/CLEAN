[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultRetcode

[Previous](Requests-Comment.md) | [Next](Requests-ResultDealer.md)

# IMTRequest::ResultRetcode

Get the current state of a trade request.

C++
    
    
    MTAPIRES  IMTRequest::ResultRetcode()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.ResultRetcode()

### Return Value

[Return code](../../../../Return-Codes/Trade-Requests.md) that corresponds to the current state of a trade request.

### Note

When a request state change, the return value changes accordingly.
