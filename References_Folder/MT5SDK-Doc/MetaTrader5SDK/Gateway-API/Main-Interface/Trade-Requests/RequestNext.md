[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestNext

[Previous](RequestTotal.md) | [Next](RequestGet.md)

# IMTGatewayAPI::RequestNext

Get a trade request by a queue position.

C++
    
    
    MTAPIRES  IMTGatewayAPI::RequestNext(
       const UINT   pos,         // Trade request position
       IMTRequest*  request      // An object of a trade request
       IMTUser*     user         // An object of the client record
       IMTAccount*  account      // An object of a trading account
       IMTOrder*    order        // An order object
       IMTPosition* position     // Position object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.RequestNext(
       uint         pos,         // Trade request position
       CIMTRequest  request      // An object of a trade request
       CIMTUser     user         // An object of the client record
       CIMTAccount  account      // An object of a trading account
       CIMTOrder    order        // An order object
       CIMTPosition position     // Position object
       )

### Parameters

**pos**  
[in] Position of a trade request in a queue, starting with 0.

**request**  
[out] An object of a trade request. The request object must first be created using theIMTGatewayAPI::RequestCreatemethod.

**user**  
[out] An object of the client login. The user object must first be created using theIMTGatewayAPI::UserCreatemethod.

**account**  
[out] An object of a client trading account. The account object must first be created using theIMTGatewayAPI::UserCreateAccountmethod.

**order**  
[out] An object of a trade order. The order object must first be created using theIMTGatewayAPI::OrderCreatemethod.

**position**  
[out] A trade position object of a trade request. The position object must first be created using theIMTGatewayAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method copies trade request data at the specified queue position to the request object. [IMTGatewayAPI::DealerStart](../Processing-Trade-Requests/DealerStart.md) must be preliminarily called for making the method work.
