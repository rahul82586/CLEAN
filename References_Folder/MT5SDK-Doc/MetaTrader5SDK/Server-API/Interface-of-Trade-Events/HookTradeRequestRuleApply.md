[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRequestRuleApply

[Previous](HookTradeRequestRuleFilter.md) | [Next](HookTradeRollover.md)

# IMTTradeSink::HookTradeRequestRuleApply

A hook of the application of a [routing rule](../../Configuration-Interfaces/Routing/IMTConRoute.md) to a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md). The hook is called after a check of request's correspondence to a rule, and allows the dynamic redefinition of the route. For example, a request that should be processed by a plugin in accordance with the routing rule can instead be sent to a dealer for processing.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRequestRuleApply(
       IMTRequest*          request,      // A pointer to the request object
       IMTConRoute*         rule,         // A pointer to the routing rule object
       const IMTConGroup*   group         // A pointer to the group configuration object
       )

### Parameters

**request**  
[in/out] A pointer to thetrade requestobject.

**rule**  
[in/out] A pointer to the object of therouting rule, in accordance with which the request should be processed, is input. An object of the changed routing rule which will be actually applied for processing the request can be output (ifMT_RET_OKis returned). The new rule only applies to the current request.

**group**  
[in] A pointer to the object of theconfiguration of the group of a client, for whom the request is being processed.

### Return Value

To process a request according to a regular rule, return [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md). The request will be processed in accordance with the original routing rule.

### Note

Actions applied to a request according to a routing rule can be divided into two types: ultimate and intermediate. Ultimate actions complete the routing of a request (execution, rejection, requote or forwarding to a dealer). Intermediate actions make some changes, and the routing continues according to the next rule (SL/TP clearing or delay). The compliance of each request to each rule is checked until an ultimate action is applied to the request. HookTradeRequestRuleApply is also called for all rules until an ultimate action is applied to the request.

  * Rule 1 is checked. The request does not meet the rule conditions, the hook is not called, and checking proceeds to the next one.
  * Rule 2 is checked. The request matches the rule, so the hook is called. The plugin returns the MT_RET_ERROR code. The rule is skipped, checking proceeds to the next one.
  * Rule 3 is checked. The request matches the rule, so the hook is called. The plugin returns the MT_RET_OK response and changes the current rule's action to [IMTConRoute::ACTION_DELAY_TICK (#enrouteaction)](../../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#enrouteaction). A delayed is applied to the request and the check is returned to rule 3.
  * Rule 3 is checked one more time. The plugin returns MT_RET_OK_NONE from the hook. The rule is processed in the standard way. An action confirming the request at a market price is applied. This is the ultimate action, so routing is complete. HookTradeRequestRuleApply will no longer be called for this request.



### Example
    
    
    //+------------------------------------------------------------------+
    //| Hook of checks of whether a request matches the routing rule     |
    //| Called before checking rule conditions                  |
    //+------------------------------------------------------------------+
    MTAPIRES CPluginInstance::HookTradeRequestRuleApply(IMTRequest* request,IMTConRoute* rule,const IMTConGroup* group)
      {
    //--- Check
       if(!request || !rule)
         return(MT_RET_OK_NONE);
    //--- Checking the request
       if(request->Action()==IMTRequest::TA_INSTANT ||
          request->Action()==IMTRequest::TA_MARKET  ||
          request->Action()==IMTRequest::TA_EXCHANGE)
          if(request->Type()==IMTOrder::OP_BUY)
            {
             //--- Changing the rule and sending the request to a dealer
             rule->Clear();
             rule->Name(L"plugin route to online dealers");
             rule->Action(IMTConRoute::ACTION_DEALER_ONLINE);
             //--- Adding a dealer
             ....
             //--- Processing the request according to the new rule
             return(MT_RET_OK);
            }
    //--- Other requests will be processed in the normal way
       return(MT_RET_OK_NONE);
      }
