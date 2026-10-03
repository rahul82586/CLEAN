[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRequestAdd

[Previous](OnTradeSplit.md) | [Next](HookTradeRequestRoute.md)

# IMTTradeSink::HookTradeRequestAdd

A hook for adding a checked [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) in the requests queue.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRequestAdd(
       IMTRequest*          request,      // A pointer to the request object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       const IMTPosition*   position,     // A pointer to the position object
       const IMTOrder*      order,        // A pointer to the order object
       IMTOrder*            order_new     // A pointer to the object of the modified order
       )

### Parameters

**request**  
[in][out] A pointer to the object ofa trade request.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the request is being processed.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, which request is being processed.

**position**  
[in] A pointer to the object of atrade position, which corresponds to the client and symbol, for which a request is being processed.

**order**  
[in] A pointer to the object of atrade order, which corresponds to the request being processed. It is filled only if atrade requestrelates to changing an already existing order (modifying, removing or activating):

**order_new**  
[in/out] A pointer to the object of atrade orderto be created as a result of the execution of a trade request. It is filled only for requests related to generating a new trade order rather than modifying an existing one (the full list of request types is provided below). The order placed in order_new is ready for adding to the trading database. It has all necessary fields filled except for a ticket (IMTOrder::Order). Creating a new order (in the database) and assigning a ticket to it occur only after the API confirms the operation (by returning MT_RET_OK from the hook). This saves resources that would have been spent on adding the orders that are to be rejected and removed from the hook to the database.

  * TA_MODIFY
  * TA_REMOVE
  * TA_ACTIVATE
  * TA_ACTIVATE_STOPLIMIT
  * TA_STOPOUT_ORDER
  * TA_EXPIRATION
  * TA_DEALER_ORD_MODIFY
  * TA_DEALER_ORD_REMOVE
  * TA_DEALER_ORD_ACTIVATE
  * TA_DEALER_ORD_SLIMIT



### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook.

### Note

Depending on the type of a received request, the hook allows modifying the request as well as rejecting or accepting it without changes. The type also affects the order_new parameter value. The following trade request types (described in [IMTRequest::EnTradeActions (#entradeactions)](../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Enumerations.md#entradeactions)) can be changed using this hook. The order_new parameter is filled for them:

  * TA_REQUEST
  * TA_INSTANT
  * TA_MARKET
  * TA_EXCHANGE
  * TA_PENDING
  * TA_DEALER_POS_EXECUTE
  * TA_DEALER_POS_EXECUTE
  * TA_ACTIVATE_SL
  * TA_ACTIVATE_TP
  * TA_STOPOUT_POSITION


  * TA_PRICE
  * TA_SLTP
  * TA_TRANSFER
  * TA_DEALER_POS_MODIFY
  * TA_DEALER_BALANCE


