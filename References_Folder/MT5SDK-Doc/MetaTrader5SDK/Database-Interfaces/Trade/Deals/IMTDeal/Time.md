[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Time

[Previous](ContractSize.md) | [Next](Symbol.md)

# IMTDeal::Time

Get the time of a deal.

C++
    
    
    INT64  IMTDeal::Time()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTDeal.Time()

### Return Value

The time of a deal execution in seconds that have elapsed since 01.01.1970.

# IMTDeal::Time

Set the time of a deal.

C++
    
    
    MTAPIRES  IMTDeal::Time(
       const INT64  time      // Deal time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Time(
       long         time      // Deal time
       )

### Parameters

**time**  
[in] The time of a deal execution in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the [IMTDeal::TimeMsc](TimeMsc.md) value will be filled in automatically.
