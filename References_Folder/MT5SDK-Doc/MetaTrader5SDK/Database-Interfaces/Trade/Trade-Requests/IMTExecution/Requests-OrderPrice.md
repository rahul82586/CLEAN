[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderPrice

[Previous](Requests-OrderVolumeExt.md) | [Next](Requests-OrderActivationFlags.md)

# IMTExecution::OrderPrice

Gets an order price.

C++
    
    
    double  IMTExecution::OrderPrice()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.OrderPrice()

### Return Value

Order price.

# IMTExecution::OrderPrice

Set the order price.

C++
    
    
    MTAPIRES  IMTExecution::OrderPrice(
       const double  price      // Order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderPrice(
       double        price      // Order price
       )

### Parameters

**price**  
[in] Order price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
