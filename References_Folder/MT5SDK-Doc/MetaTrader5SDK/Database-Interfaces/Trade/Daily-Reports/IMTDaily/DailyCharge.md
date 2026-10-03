[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyCharge

[Previous](DailyCredit.md) | [Next](DailyCorrection.md)

# IMTDaily::DailyCharge

Get the amount of other charges to the client's balance during the reported day.

C++
    
    
    double  IMTDaily::DailyCharge()

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyCharge()

### Return Value

The amount of other charges to the client's balance during the reported day.

# IMTDaily::DailyCharge

Sets the amount of other charges to the client's balance during the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyCharge(
       const double  charge      // Other charges for the day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyCharge(
       double        charge      // Other charges for the day
       )

### Parameters

**charge**  
[in] The amount of other charges to the client's balance during the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
