[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / TimeFrom

[Previous](Symbol.md) | [Next](TimeTo.md)

# IMTConSpreadLeg::TimeFrom

Getting the beginning of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg.

C++
    
    
    INT64  IMTConSpreadLeg::TimeFrom()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConSpreadLeg.TimeFrom()

Python (Manager API)
    
    
    MTConSpreadLeg.TimeFrom

### Return Value

The beginning of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg. The date is specified in seconds since January 1, 1970.

# IMTConSpreadLeg::TimeFrom

Setting the beginning of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::TimeFrom(
       const INT64  from      // Beginning of the period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.TimeFrom(
       long         from      // Beginning of the period
       )

Python (Manager API)
    
    
    MTConSpreadLeg.TimeFrom

### Parameters

**from**  
[in] The beginning of a period for filtering symbols by expiration time when specifying a basic asset for a spread leg. The date is specified in seconds since January 1, 1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is used when specifying trade symbols for a spread leg as a basic asset ([IMTConSpreadLeg::LEG_MODE_FUTURES (#enlegmode)](Enumerations.md#enlegmode)).
