[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealPrice

[Previous](Requests-DealVolumeRemaindExt.md) | [Next](Requests-DealReason.md)

# IMTExecution::DealPrice

Gets the price of a deal.

C++
    
    
    double  IMTExecution::DealPrice()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.DealPrice()

### Return Value

Deal execution price.

# IMTExecution::DealPrice

Sets the price of a deal.

C++
    
    
    MTAPIRES  IMTExecution::DealPrice(
       const double  price      // Deal price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealPrice(
       double        price      // Deal price
       )

### Parameters

**price**  
[in] Deal execution price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
