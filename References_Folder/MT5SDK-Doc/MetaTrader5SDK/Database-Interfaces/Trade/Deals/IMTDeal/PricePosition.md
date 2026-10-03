[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / PricePosition

[Previous](ProfitRaw.md) | [Next](TickValue.md)

# IMTDeal::PricePosition

Gets the price of the position that was closed by this deal.

C++
    
    
    double  IMTDeal::PricePosition()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.PricePosition()

### Return Value

The price of the position that was closed by this deal.

### Note

The value can be obtained only for the deals of type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)

# IMTDeal::PricePosition

Sets the price of the position closed by the deal.

C++
    
    
    MTAPIRES  IMTDeal::PricePosition(
       const double  price      // Position price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.PricePosition(
       double        price      // Position price
       )

### Parameters

**price**  
[in] The price of the position closed by the deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value can be set only for the deals of type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)
