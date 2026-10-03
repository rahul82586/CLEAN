[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) / AskMarkup

[Previous](BidMarkup.md) | [Next](Digits.md)

# IMTConGatewayTranslate::AskMarkup

Gets a markup value for the Ask price received for a symbol from the data source to which the gateway connects.

C++
    
    
    INT  IMTConGatewayTranslate::AskMarkup()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGatewayTranslate.AskMarkup()

Python (Manager API)
    
    
    MTConGatewayTranslate.AskMarkup

### Return Value

A markup value for the Ask price received for a symbol from the data source to which the gateway connects.

# IMTConGatewayTranslate::AskMarkup

Gets a markup value for the Ask price received for a symbol from the data source to which the gateway connects.

C++
    
    
    MTAPIRES  IMTConGatewayTranslate::AskMarkup(
       const INT  markup      // Ask price conversion value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayTranslate.AskMarkup(
       int        markup      // Ask price conversion value
       )

Python (Manager API)
    
    
    MTConGatewayTranslate.AskMarkup

### Parameters

**markup**  
[in] Ask price conversion value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The markup function allows to split prices. A negative (or zero) value should be specified for the [Bid](BidMarkup.md) price, ans a positive (or zero) value should be specified for Ask. In other cases transmitted prices may be incorrect (negative spread).
