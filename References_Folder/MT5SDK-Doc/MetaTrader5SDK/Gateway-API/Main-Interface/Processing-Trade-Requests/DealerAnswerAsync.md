[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerAnswerAsync

[Previous](DealerLockAsync.md) | [Next](DealerExecuteAsync.md)

# IMTGatewayAPI::DealerAnswerAsync

Return the results of the captured request processing.

C++
    
    
    MTAPIRES  IMTGatewayAPI::DealerAnswerAsync(
       IMTConfirm*  confirm      // Request confirmation object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.DealerAnswerAsync(
       CIMTConfirm  confirm      // Request confirmation object
       )

### Parameters

**confirm**  
[in]Request confirmation object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Each trade request can only be responded once using this method. The only exceptions are some [response codes](../../../Database-Interfaces/Trade/Trade-Requests/IMTConfirm/Requests-Retcode.md) (MT_RET_REQUEST_REQUOTE, MT_RET_REQUEST_PRICES) in Instant and Request [execution modes](../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md).

### An example of a response to a SL/TP activation request, if such a request should be processed on the exchange side
    
    
    //+------------------------------------------------------------------+
    //| SL/TP control on the exchange side                               |
    //+------------------------------------------------------------------+
    void CMTGatewayApp::PreAnswerExchangeNoSLTP(const IMTRequest* request)
      {
       IMTConfirm*   confirm={0};
       IMTExecution* execution={0};
       MTAPISTR      str={0};
       //--- Checks
       if(m_api_gateway)
         {
          confirm=m_api_gateway->DealerConfirmCreate();
          execution=m_api_gateway->DealerExecutionCreate();
         }
       else
         {
          ExtLogger.Out(MTLogErr, L"failed to create confirm and execution interface");
          return;
         }
       //--- Response to a client that the request has been accepted
       confirm->ID(request->ID());
       confirm->Retcode(MT_RET_REQUEST_PLACED);
       confirm->Volume(request->Volume());
       confirm->Price(request->PriceOrder());
       confirm->Comment(L"pre confirmed message by ExampleGateway");
       //--- Send a response, the order gets the 'started' state, response 10008 will be sent to the terminal
       if(m_api_gateway->DealerAnswerAsync(confirm)!=MT_RET_OK)
          ExtLogger.Out(MTLogErr, L"confirm preanswer for request failed. Preanswer: %s", confirm->Print(str));
       else
          ExtLogger.Out(MTLogErr, L"Confirm preanswer: %s", confirm->Print(str));
       //--- Inform the MetaTrader server that a new order request will be sent to the exchange
       execution->ID(request->ID());
       execution->Order(request->ResultOrder());
       execution->OrderType(request->Type());
       execution->OrderVolume(request->Volume());
       execution->OrderPrice(request->PriceOrder());
       execution->Action(IMTExecution::TE_ORDER_NEW_REQUEST);
       execution->OrderActivationFlags(IMTOrder::ACTIV_FLAGS_NO_SL | IMTOrder::ACTIV_FLAGS_NO_TP);
       //--- Send the first response about the execution to the platform, the order gets the 'request adding' state
       if(m_api_gateway->DealerExecuteAsync(execution)!=MT_RET_OK)
          ExtLogger.Out(MTLogErr, L"Send DealerExecuteAsync for request failed. Answer: %s", execution->Print(str));
       else
          ExtLogger.Out(MTLogErr, L"PreAnswer: %s", execution->Print(str));
        //--- Clear objects
        if(confirm)
           confirm->Release();
        if(execution)
           execution->Release();
      }
    //+------------------------------------------------------------------+

After that, signals about further SL/TP triggering will not be sent to the gateway. As soon as the request is processed by the exchange, send the trade execution to the platform to complete the deal:
    
    
    //+------------------------------------------------------------------+
    //| Close position by SL/TP when response from exchange is received  |
    //+------------------------------------------------------------------+
    void CMTGatewayApp::AnswerCloseWithoutRequest(void)
      {
       IMTExecution* execution={0};
       MTAPISTR      str={0};
       //--- Checks
       if(m_api_gateway)
          execution=m_api_gateway->DealerExecutionCreate();
       else
         {
          ExtLogger.Out(MTLogErr, L"failed to create execution interface");
          return;
         }
        //--- Fill the execution object (pass your values to it)
        execution->Clear();
        execution->Login(1000);
        execution->Symbol(L"EURUSD");
        execution->Position(25983);
        execution->DealAction(IMTDeal::DEAL_SELL);
        execution->DealVolume(10000);
        execution->DealVolumeRemaind(0);
        execution->DealPrice(0.75000);
        execution->Digits(5);
        execution->Action(IMTExecution::TE_DEAL_EXTERNAL);
        //--- 
        if(m_api_gateway->DealerExecuteAsync(execution)!=MT_RET_OK)
           ExtLogger.Out(MTLogErr, L"AnswerCloseWithoutRequest: send DealerExecuteAsync for request failed. Answer: %s", execution->Print(str));
        else
           ExtLogger.Out(MTLogErr, L"AnswerCloseWithoutRequest answer: %s", execution->Print(str));
        //--- Clear the object
        if (execution)
            execution->Release();
      }
    //+------------------------------------------------------------------+
