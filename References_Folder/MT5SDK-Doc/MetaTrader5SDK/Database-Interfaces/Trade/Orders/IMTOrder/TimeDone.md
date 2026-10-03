[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TimeDone

[Previous](TimeExpiration.md) | [Next](TimeDoneMsc.md)

# IMTOrder::TimeDone

Get the order execution time.

C++
    
    
    INT64  IMTOrder::TimeDone()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTOrder.TimeDone()

Python
    
    
    MTOrder.TimeDone()

### Return Value

Date and time of the execution of an order, in seconds that have elapsed since 01.01.1970. The 0 value means that the order has not yet been executed.

### Note

If the order is processed in an external trading system, this property contains the time of order execution in the external system (not in the MetaTrader 5 platform).

# IMTOrder::TimeDone

Set the order execution time.

C++
    
    
    MTAPIRES  IMTOrder::TimeDone(
       const INT64  time      // Execution time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TimeDone(
       long         time      // Execution time
       )

Python
    
    
    MTOrder.TimeDone()

### Parameters

**time**  
[in] Date and time of the execution of an order, in seconds that have elapsed since 01.01.1970. The 0 value means that the order has not yet been executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the [IMTOrder::TImeDoneMsc](TimeDoneMsc.md) value will be filled in automatically.
