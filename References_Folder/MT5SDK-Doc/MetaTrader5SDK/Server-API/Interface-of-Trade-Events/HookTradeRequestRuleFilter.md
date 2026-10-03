[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRequestRuleFilter

[Previous](HookTradeRequestProcessCloseBy.md) | [Next](HookTradeRequestRuleApply.md)

# IMTTradeSink::HookTradeRequestRuleFilter

Hooks checking of whether a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) matches a [routing rule](../../Configuration-Interfaces/Routing/IMTConRoute.md). The hook is called before a check of request's correspondence to each of existing rules, and allows the dynamic change of request routes. For example, a plugin may route a request by its own rule during such a check, even if the request does not initially match this rule.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRequestRuleFilter(
       IMTRequest*          request,      // A pointer to the request object
       IMTConRoute*         rule,         // A pointer to the routing rule object
       const IMTConGroup*   group         // A pointer to the group configuration object
       )

### Parameters

**request**  
[in/out] A pointer to thetrade requestobject.

**rule**  
[in/out] A pointer to the object of therouting rule, compliance with which is being checked, is input. An object of the changed routing rule which will be actually applied for processing the request can be output (ifMT_RET_OKis returned). The new rule only applies to the current request.

**group**  
[in] A pointer to the object of theconfiguration of the group of a client, for whom the request is being processed.

### Return Value

To process a request according to a regular rule, return [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md). If the request meets the rule conditions, this rule will be applied, otherwise the rule will be skipped.

### Note

Actions applied to a request according to a routing rule can be divided into two types: ultimate and intermediate. Ultimate actions complete the routing of a request (execution, rejection, requote or forwarding to a dealer). Intermediate actions make some changes, and the routing continues according to the next rule (SL/TP clearing or delay). The compliance of each request to each rule is checked until an ultimate action is applied to the request. HookTradeRequestRuleFilter is also called for all rules until an ultimate action is applied to the request.

  * Rule 1 is checked. The hook is called. The plugin returns the MT_RET_OK_NONE response. The rule is processed in the standard way. The request does not meet the rule, checking proceeds to the next one.
  * Rule 2 is checked. The hook is called. The plugin returns MT_RET_ERROR. The rule is skipped, checking proceeds to the next one.
  * Rule 3 is checked. The hook is called. The plugin returns the MT_RET_OK response and changes the current rule's action to [IMTConRoute::ACTION_DELAY_TICK (#enrouteaction)](../../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#enrouteaction). The rule is applied regardless of whether the request matches the rule. The request is delayed and the check is returned to rule 3.
  * Rule 3 is checked one more time. The hook is called. The plugin returns MT_RET_OK_NONE. The rule is processed in the standard way. The request matches to the rule, the action defined the rule is applied — confirming the request at the market price. This is the ultimate action, so routing is complete. HookTradeRequestRuleFilter will no longer be called for this request.



### Example
    
    
    //+------------------------------------------------------------------+
    //| Hook of checks of whether a request matches the routing rule     |
    //| Called before checking rule conditions                           |
    //+------------------------------------------------------------------+
    MTAPIRES CPluginInstance::HookTradeRequestRuleFilter(IMTRequest* request,IMTConRoute* rule,const IMTConGroup* group)
      {
    //--- Check
       if(!request || !rule)
         return(MT_RET_OK_NONE);
    //--- check the request
       if(request->Action()==IMTRequest::TA_INSTANT ||
          request->Action()==IMTRequest::TA_MARKET  ||
          request->Action()==IMTRequest::TA_EXCHANGE)
          if(request->Type()==IMTOrder::OP_BUY)
            {
             //--- Change the rule and forward the request to a dealer
             rule->Clear();
             rule->Name(L"plugin route to online dealers");
             rule->Action(IMTConRoute::ACTION_DEALER_ONLINE);
             //--- adding a dealer
             ....
             //--- Processing the request according to a new rule
             return(MT_RET_OK);
            }
    //--- Other requests will be processed in the normal way
       return(MT_RET_OK_NONE);
      }
