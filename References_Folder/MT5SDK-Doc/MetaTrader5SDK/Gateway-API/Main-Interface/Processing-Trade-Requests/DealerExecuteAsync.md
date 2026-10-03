[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerExecuteAsync

[Previous](DealerAnswerAsync.md) | [Next](../Controlling-Positions-in-External-System.md)

# IMTGatewayAPI::DealerExecuteAsync

The platform notification on the order trade execution in the external system.

C++
    
    
    MTAPIRES  IMTGatewayAPI::DealerExecuteAsync(
       IMTExecution*  execution      // Trade execution object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.DealerExecuteAsync(
       CIMTExecution  execution      // Trade execution object
       )

### Parameters

**execution**  
[in]Trade execution object.

### Return Value

If the command is successfully sent to the execution queue, the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code is returned. Otherwise, an error has occurred, which corresponds to the response code.

### Note

During the execution of this method the operation is carried out in the trading platform that corresponds to the executed one in the external environment.

### Example of partial Stop Loss execution and cancellation of activation for the remaining volume
    
    
    //+------------------------------------------------------------------+
    //| Partial position closing upon Stop Loss activation & cancellation|
    //| of StopLoss activation for remaining volume. Position with the |
    //| remaining volume stays in the platform till next SL activation   |
    //+------------------------------------------------------------------+
    void CExchange::AnswerExSLPartialFilled(const IMTRequest *request)
      { 
       MTAPISTR str              ={0};
       UINT64   volume           =request->Volume();  // Volume in the request to close by SL
       UINT64   filled_ex_volume =0;                  // Volume confirmed by the exchange
       UINT64   remaind_ex_volume=0;                  // volume which remained unfilled
       UINT64   delta            =5000;               // suppose the exchange always fills 0.5 lot less, 1 lot = 10000 units
       //---
       if(request->Volume()<=5000)
         {
          ExtLogger.Out(MTLogErr,L"Request volume =%I64u, exchange fill full volume",volume);
          filled_ex_volume=volume;
          remaind_ex_volume=0;
         }
       else
         {
          filled_ex_volume=volume - delta;
          remaind_ex_volume=delta;
          ExtLogger.Out(MTLogErr,L"Request volume =%I64u, exchange filled volume =%I64u, remained volume =%I64u,",volume,filled_ex_volume,remaind_ex_volume);
         }
       //---
       if((m_execution=m_api_gateway->DealerExecutionCreate())==NULL)
         {
          ExtLogger.Out(MTLogErr,L"failed to create execution interface");
          return;
         }
       //--- Process the executed part
       m_execution->Clear();
       m_execution->Order(request->ResultOrder());
       m_execution->Symbol(request->Symbol());
       m_execution->DealAction(request->Type());
       m_execution->DealVolume(filled_ex_volume);
       m_execution->DealVolumeRemaind(remaind_ex_volume);  // Set the remaining (unfilled) volume
       m_execution->DealPrice(request->PriceOrder());
       m_execution->Action(IMTExecution::TE_ORDER_FILL);
       //---
       if((m_api_gateway->DealerExecuteAsync(m_execution))!=MT_RET_OK)
         {
          ExtLogger.Out(MTLogErr,L"Send DealerExecuteAsync for request failed. Answer: %s",m_execution->Print(str));
         }
       else
         {
          ExtLogger.Out(MTLogErr,L"Answer: %s",m_execution->Print(str));
         }
       //--- Reset activation of the remaining volume for re-processing
       m_execution->Action(IMTExecution::TE_ORDER_CANCEL);
       //---
       if((m_api_gateway->DealerExecuteAsync(m_execution))!=MT_RET_OK)
         {
          ExtLogger.Out(MTLogErr,L"Send DealerExecuteAsync for OrderActivationMode failed. Answer: %s",m_execution->Print(str));
         }
       else
         {
          ExtLogger.Out(MTLogErr,L"Answer for OrderActivationMode: %s",m_execution->Print(str));
         }
       //---
       m_execution->Release();
    }

### Example of partial pending order execution and cancellation of activation for the remaining volume
    
    
    //+------------------------------------------------------------------+
    //| Partial execution of a pending order upon activation and         |
    //| canceling activation for remaining volume. Order with remaining |
    //| volume stays in the platform till next activation    |
    //+------------------------------------------------------------------+
    void CExchange::AnswerExPendingPartialFilled(const IMTRequest *request)
      {
       MTAPISTR    str              ={0};
       UINT        request_type;
       UINT64      volume           =request->Volume(); // Volume in the pending order request
       UINT64      filled_ex_volume =0;                 // Volume confirmed by the exchange
       UINT64      remaind_ex_volume=0;                 // volume which remained unfilled
       UINT64      delta            =5000;              // suppose the exchange always fills 0.5 lot less, 1 lot = 10000 units
       //---
       if(request->Volume()<=5000)
         {
          ExtLogger.Out(MTLogErr,L"Request volume =%I64u, exchange fill full volume",volume);
          filled_ex_volume=volume;
          remaind_ex_volume=0;
         }
       else
         {
          filled_ex_volume=volume - delta;
          remaind_ex_volume=delta;
          ExtLogger.Out(MTLogErr,L"Request volume =%I64u, exchange filled volume =%I64u, remaind volume =%I64u,",volume,filled_ex_volume,remaind_ex_volume);
         }
       //--- Change the pending order type to Market
       if(request->Type()==IMTOrder::OP_BUY_LIMIT || request->Type()==IMTOrder::OP_BUY_STOP)
         {
          request_type=IMTOrder::OP_BUY;
         }
       //---
       if(request->Type()==IMTOrder::OP_SELL_LIMIT || request->Type()==IMTOrder::OP_SELL_STOP)
         {
          request_type=IMTOrder::OP_SELL;
         }
       //---
       if((m_execution=m_api_gateway->DealerExecutionCreate())==NULL)
         {
          ExtLogger.Out(MTLogErr,L"failed to create execution interface");
          return;
         }
       //--- Process the executed part
       m_execution->Clear();
       m_execution->Order(request->ResultOrder());
       m_execution->Symbol(request->Symbol());
       m_execution->DealAction(request_type);
       m_execution->DealVolume(filled_ex_volume);
       m_execution->DealVolumeRemaind(remaind_ex_volume);  // Set the remaining (unfilled) volume
       m_execution->DealPrice(request->PriceOrder());
       m_execution->Action(IMTExecution::TE_ORDER_FILL);
       //---
       if((m_api_gateway->DealerExecuteAsync(m_execution))!=MT_RET_OK)
         {
          ExtLogger.Out(MTLogErr,L"Send DealerExecuteAsync for request failed. Answer: %s",m_execution->Print(str));
         }
       else
         {
          ExtLogger.Out(MTLogErr,L"Answer: %s",m_execution->Print(str));
         }
       //--- Reset activation of the remaining volume for re-processing
       m_execution->Action(IMTExecution::TE_ORDER_MODIFY);
       m_execution->OrderActivationMode(IMTOrder::ACTIVATION_NONE);
       //---
         if((m_api_gateway->DealerExecuteAsync(m_execution))!=MT_RET_OK)
           {
            ExtLogger.Out(MTLogErr,L"Send DealerExecuteAsync for OrderActivationMode failed. Answer: %s",m_execution->Print(str));
           }
         else
           {
            ExtLogger.Out(MTLogErr,L"Answer for OrderActivationMode: %s",m_execution->Print(str));
           }
         //---
         m_execution->Release();
    }
