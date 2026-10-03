[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TimeSetupMsc

[Previous](TimeSetup.md) | [Next](TimeExpiration.md)

# IMTOrder::TimeSetupMsc

Gets the order placing time in milliseconds.

C++
    
    
    INT64  IMTOrder::TimeSetupMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTOrder.TimeSetupMsc()

Python
    
    
    MTOrder.TimeSetupMsc()

### Return Value

Date and time when the order is placed, in milliseconds that have elapsed since January 1, 1970.

### Note

If the order is processed in an external trading system, this property contains the time of order placing in the external system (not in the MetaTrader 5 platform). When Stop Limit orders are triggered, a new value is written to this field, instead of the time the order was placed by the client: the time when the corresponding limit order was placed.

# IMTOrder::TimeSetupMsc

Sets the order placing time in milliseconds.

C++
    
    
    MTAPIRES  IMTOrder::TimeSetupMsc(
       const INT64  time      // Expiration time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TimeSetupMsc(
       long         time      // Expiration time
       )

Python
    
    
    MTOrder.TimeSetupMsc()

### Parameters

**time**  
[in] Date and time when the order is placed, in milliseconds that have elapsed since January 1, 1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

If the value of this field is specified, the [IMTOrder::TimeSetup](TimeSetup.md) value will be filled in automatically.
