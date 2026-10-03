[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeExecution

[Previous](OnTradeRequestRefuse.md) | [Next](OnTradeSplit.md)

# IMTTradeSink::OnTradeExecution

A handler of the event of receiving a trade execution from a gateway.
    
    
    virtual void  IMTTradeSink::OnTradeExecution(
       const IMTConGateway* gateway,      // A pointer to the gateway configuration
       const IMTExecution*  execution,    // A pointer to the trade execution object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       const IMTPosition*   position,     // A pointer to the position object
       const IMTOrder*      order,        // A pointer to the order object
       const IMTDeal*       deal          // A pointer to the deal object
       )

### Parameters

**gateway**  
[in] A pointer to the object of agateway configurationthe trade execution is received from. This parameter is not used and is always equal to NULL. To get the information about the gateway from which the execution has been received, analyze the "execution" parameter (IMTExecution::GatewayID).

**execution**  
[in] A pointer to the object of thetrade executionreceived.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the trade execution is being processed.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, for which the trade execution is being processed.

**position**  
[in] A pointer to the object of atrade position, which corresponds to the client and symbol, for which the trade execution is being processed.

**order**  
[in] A pointer to the object of atrade order, which corresponds to the trade execution being processed: a newly created or modified order.

**deal**  
[in] A pointer to the object of atrade dealcreated as a result of applying the trade execution.

### Note

Depending on the request type, parameters symbol, position and order can be equal to NULL.
