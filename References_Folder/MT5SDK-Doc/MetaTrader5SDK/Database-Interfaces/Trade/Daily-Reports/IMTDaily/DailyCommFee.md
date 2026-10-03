[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyCommFee

[Previous](DailyCommRound.md) | [Next](DailyDividend.md)

# IMTDaily::DailyCommFee

Get the [fee amount (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) charged for the client's deals for the reported day.

C++
    
    
    double  IMTDaily::DailyCommFee()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyCommFee()

### Return Value

The fee amount charged for the client's deals for the reported day.

# IMTDaily::DailyCommInstant

Set the [fee amount (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) charged for the client's deals for the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyCommFee(
       const double  fee       // daily fees
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyCommFee(
       double        fee       // daily fees
       )

### Parameters

**fee**  
[in] The fee amount charged for the client's deals for the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
