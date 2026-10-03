[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / TimeTo

[Previous](TimeFrom.md) | [Next](Ratio.md)

# IMTConSpreadLeg::TimeTo

Getting the end of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg.

C++
    
    
    INT64  IMTConSpreadLeg::TimeTo()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConSpreadLeg.TimeTo()

Python (Manager API)
    
    
    MTConSpreadLeg.TimeTo

### Return Value

The end of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg. The date is specified in seconds since January 1, 1970.

# IMTConSpreadLeg::TimeTo

Setting the end of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::TimeTo(
       const INT64  to      // End of period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.TimeTo(
       long         to      // End of period
       )

Python (Manager API)
    
    
    MTConSpreadLeg.TimeTo

### Parameters

**to**  
[in] The end of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg. The date is specified in seconds since January 1, 1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is used when specifying trade symbols for a spread leg as a basic asset ([IMTConSpreadLeg::LEG_MODE_FUTURES (#enlegmode)](Enumerations.md#enlegmode)).
