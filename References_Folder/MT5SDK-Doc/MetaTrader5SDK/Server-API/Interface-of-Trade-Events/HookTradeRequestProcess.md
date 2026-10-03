[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRequestProcess

[Previous](HookTradeRequestRoute.md) | [Next](HookTradeRequestProcessCloseBy.md)

# IMTTradeSink::HookTradeRequestProcess

A hook of [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) execution.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRequestProcess(
       const IMTRequest*    request,      // A pointer to the request object
       const IMTConfirm*    confirm,      // A pointer to the confirmation object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       IMTPosition*         position,     // A pointer to the position object
       IMTOrder*            order,        // A pointer to the order object
       IMTDeal*             deal          // A pointer to the deal object
       )

### Parameters

**request**  
[in] A pointer to the object of atrade request.

**confirm**  
[in] A pointer to the object ofconfirmation of a trade request, as a result of which a deal is executed.

**group**  
[in] A pointer to the object of theconfiguration of the group of a client, for whom the request is being processed.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, which request is being processed.

**position**  
[in][out] A pointer to the object of atrade position, which corresponds to the client and symbol, for which a request is being processed. The parameter passes the future state of the position as if the processed request has been executed. Accordingly, when processing a request to completely close the position, zero values are passed in the object for all fields except direction and symbol, since the request results in the position liquidation. For more data on the position, useIMTServerAPI::PositionGetorIMTServerAPI::PositionGetByTicket.

**order**  
[in][out] A pointer to the object of atrade order, which corresponds to the request being processed: a newly created or modified order.

**deal**  
[in][out] A pointer to the object of atrade dealcreated as a result of the execution of a trade request.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook.

### Note

Depending on the request type, parameters symbol, position and order can be equal to NULL.

### Example of canceling a pending order activation and removing the activated pending order
    
    
    MTAPIRES CPluginInstance::HookTradeRequestProcess(const IMTRequest* request, const IMTConfirm* confirm, const IMTConGroup* group, const IMTConSymbol* symbol, IMTPosition* position, IMTOrder* order, IMTDeal* deal)
      {
       MTAPISTR      str;
       IMTRequest*   request_new=NULL;
    //--- check
       if(!request || !m_api) return(MT_RET_ERR_PARAMS);
    //--- notify
       m_api->LoggerOut(MTLogOK,L"HookTradeRequestProcess New request: %s",request->Print(str));
    //--- check order
       if(!position)
         {
          m_api->LoggerOut(MTLogOK,L"HookTradeRequestProcess position = NULL");
         }
       else
         {
          m_api->LoggerOut(MTLogOK,L"HookTradeRequestProcess position = %s",position->Print(str));
         }
     
       if(request->Action()==IMTRequest::TA_ACTIVATE)
         {
            {
             m_api->LoggerOut(MTLogErr,L"TA_ACTIVATE");
             request_new=m_api->TradeRequestCreate();
             //--- 
             request_new->Clear();
             request_new->Login(request->Login());
             request_new->Action(IMTRequest::TA_DEALER_ORD_REMOVE);
             request_new->Type(request->Type());
             request_new->Symbol(request->Symbol());
             request_new->Order(request->Order());
             request_new->Comment(L"TestCancel");
             request_new->SourceLogin(1001); // 1001 is a used dealer account
     
             MTAPIRES retcodes=m_api->TradeRequest(request_new);
             m_api->LoggerOut(MTLogOK,L"[test-log]protect, retcodes[%u]",retcodes);
     
             if(retcodes==MT_RET_OK)
               {
                return (MT_RET_REQUEST_CANCEL);
               }
             request_new->Release();
            }
         }
    //---
       return(MT_RET_OK);
      }
