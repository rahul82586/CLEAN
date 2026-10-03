[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Type

[Previous](Requests-TimeExpiration.md) | [Next](Requests-TypeFill.md)

# IMTRequest::Type

Get the order type specified in a request.

C++
    
    
    UINT  IMTRequest::Type()  const

.NET (Gateway/Manager API)
    
    
    EnOrderType  CIMTRequest.Type()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Orders/IMTOrder/Enumerations.md#enordertype) enumeration. For balance operations ([IMTRequest::TA_DEALER_BALANCE (#entradeactions)](Requests-Enumerations.md#entradeactions)), the following values of the [IMTDeal:EnDealAction (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) enumeration are used:

  * DEAL_BALANCE — balance operations
  * DEAL_CREDIT — credit operations
  * DEAL_CHARGE — additional charges
  * DEAL_CORRECTION — correction operations
  * DEAL_BONUS — bonuses
  * DEAL_COMMISSION — commissions



# IMTRequest::Type

Set the order type in a request.

C++
    
    
    MTAPIRES  IMTRequest::Type(
       const UINT  type      // Order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Type(
       EnOrderType type      // Order type
       )

### Parameters

**type**  
[in] Order type. To pass the type, theIMTOrder::EnOrderTypeenumeration is used. For balance operations (IMTRequest::TA_DEALER_BALANCE), the following values of theIMTDeal:EnDealActionenumeration are used:

  * DEAL_BALANCE — balance operations
  * DEAL_CREDIT — credit operations
  * DEAL_CHARGE — additional charges
  * DEAL_CORRECTION — correction operations
  * DEAL_BONUS — bonuses
  * DEAL_COMMISSION — commissions



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
