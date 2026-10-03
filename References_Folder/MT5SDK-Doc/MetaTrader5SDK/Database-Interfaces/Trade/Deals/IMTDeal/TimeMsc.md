[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / TimeMsc

[Previous](Flags.md) | [Next](Reason.md)

# IMTDeal::TimeMsc

Gets the time of a deal execution in milliseconds.

C++
    
    
    INT64  IMTDeal::TimeMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTDeal.TimeMsc()

### Return Value

The time of a deal execution in milliseconds that have elapsed since January 1, 1970.

# IMTDeal::TimeMsc

Sets the time of a deal execution in milliseconds.

C++
    
    
    MTAPIRES  IMTDeal::TimeMsc(
       const INT64  time      // Deal time in milliseconds
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.TimeMsc(
       long         time      // Deal time in milliseconds
       )

### Parameters

**time**  
[in] The time of a deal execution in milliseconds that have elapsed since January 1, 1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the [IMTDeal::Time](Time.md) value will be filled in automatically.
