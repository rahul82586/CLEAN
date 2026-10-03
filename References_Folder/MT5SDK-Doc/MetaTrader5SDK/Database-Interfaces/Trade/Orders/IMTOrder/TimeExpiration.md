[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TimeExpiration

[Previous](TimeSetupMsc.md) | [Next](TimeDone.md)

# IMTOrder::TimeExpiration

Get the order expiration time.

C++
    
    
    INT64  IMTOrder::TimeExpiration()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTOrder.TimeExpiration()

Python
    
    
    MTOrder.TimeExpiration()

### Return Value

Order expiration date and time in seconds which have elapsed since 01.01.1970. The 0 value means that the order has no expiration.

# IMTOrder::TimeExpiration

Set the order expiration time.

C++
    
    
    MTAPIRES  IMTOrder::TimeExpiration(
       const INT64  time      // Expiration time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TimeExpiration(
       long         time      // Expiration time
       )

Python
    
    
    MTOrder.TimeExpiration()

### Parameters

**time**  
[in] Order expiration date and time in seconds which have elapsed since 01.01.1970. The 0 value means that the order has no expiration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The specified expiration time is always rounded to a whole minute. The minimum expiration time is 1 minute.
