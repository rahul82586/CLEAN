[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) / BidMarkup

[Previous](Symbol.md) | [Next](AskMarkup.md)

# IMTConGatewayTranslate::BidMarkup

Gets a markup value for the Bid price received for a symbol from the data source to which the gateway connects.

C++
    
    
    INT  IMTConGatewayTranslate::BidMarkup()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGatewayTranslate.BidMarkup()

Python (Manager API)
    
    
    MTConGatewayTranslate.BidMarkup

### Return Value

A markup value for the Bid price received for a symbol from the data source to which the gateway connects.

# IMTConGatewayTranslate::BidMarkup

Sets a markup value for the Bid price received for a symbol from the data source to which the gateway connects.

C++
    
    
    MTAPIRES  IMTConGatewayTranslate::BidMarkup(
       const INT  markup      // Bid price conversion value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayTranslate.BidMarkup(
       int        markup      // Bid price conversion value
       )

Python (Manager API)
    
    
    MTConGatewayTranslate.BidMarkup

### Parameters

**markup**  
[in] Bid price conversion value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The markup function allows to split prices. A negative (or zero) value should be specified for the Bid price, ans a positive (or zero) value should be specified for [Ask](AskMarkup.md). In other cases transmitted prices may be incorrect (negative spread).
