[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TimeSetup

[Previous](ReasonSet.md) | [Next](TimeSetupMsc.md)

# IMTOrder::TimeSetup

Get the order placing time.

C++
    
    
    INT64  IMTOrder::TimeSetup()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTOrder.TimeSetup()

Python
    
    
    MTOrder.TimeSetup()

### Return Value

Date and time when the order is placed, in seconds that have elapsed since 01.01.1970.

### Note

If the order is processed in an external trading system, this property contains the time of order placing in the external system (not in the MetaTrader 5 platform). When Stop Limit orders are triggered, a new value is written to this field, instead of the time the order was placed by the client: the time when the corresponding limit order was placed.

# IMTOrder::TimeSetup

Set the order placing time.

C++
    
    
    MTAPIRES  IMTOrder::TimeSetup(
       const INT64  time      // Expiration time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TimeSetup(
       long         time      // Expiration time
       )

Python
    
    
    MTOrder.TimeSetup()

### Parameters

**time**  
[in] Date and time when the order is placed, in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

If the value of this field is specified, the [IMTOrder::TimeSetupMsc](TimeSetupMsc.md) value will be filled in automatically.
