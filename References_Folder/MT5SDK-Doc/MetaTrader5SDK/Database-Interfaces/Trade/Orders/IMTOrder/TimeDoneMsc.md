[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TimeDoneMsc

[Previous](TimeDone.md) | [Next](Type.md)

# IMTOrder::TimeDoneMsc

Gets the order execution time in milliseconds.

C++
    
    
    INT64  IMTOrder::TimeDoneMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTOrder.TimeDoneMsc()

Python
    
    
    MTOrder.TimeDoneMsc()

### Return Value

Date and time of the execution of an order, in milliseconds that have elapsed since January 1, 1970. The 0 value means that the order has not yet been executed.

### Note

If the order is processed in an external trading system, this property contains the time of order execution in the external system (not in the MetaTrader 5 platform).

# IMTOrder::TimeDoneMsc

Sets the order execution time in milliseconds.

C++
    
    
    MTAPIRES  IMTOrder::TimeDoneMsc(
       const INT64  time      // Execution time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TimeDoneMsc(
       long         time      // Execution time
       )

Python
    
    
    MTOrder.TimeDoneMsc()

### Parameters

**time**  
[in] Date and time of the execution of an order, in milliseconds that have elapsed since January 1, 1970. The 0 value means that the order has not yet been executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the [IMTOrder::TimeDone](TimeDone.md) value will be filled in automatically.
