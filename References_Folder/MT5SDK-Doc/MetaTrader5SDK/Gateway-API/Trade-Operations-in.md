[🏠 Document Start](../README.md) / [Gateway API](README.md) / Trade Operations in

[Previous](Interaction-of-the-Platform-and.md) | [Next](Development-and-Debugging-of-Gateways.md)

<a id="trade-operations-in-gateway-api"></a>
# Trade Operations in Gateway API (#trade-operations-in-gateway-api)

In the trade interaction of the Gateway API and the MetaTrader 5 trading platform, two main entities can be singled out — a trade request and a trade execution.

A trade request ([IMTRequest](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md)) is formed on the side of the MetaTrader 5 platform as a result of a trade order sent by a client. A trade request notifies the Gateway API of trade operations on the platform side.

A trade execution ([IMTExecution](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md)) is formed on the side of the Gateway API. It is used to notify the MetaTrader 5 platform of events in an external trading system. Based on the trade execution, the appropriate action is performed in MetaTrader 5.

<a id="queue-of-trade-requests"></a>
## Queue of Trade Requests (#queue-of-trade-requests)

In accordance with the ideology of the MetaTrader 5 trading platform, customer request management is carried out through a queue of trade requests. A gateway written with the help of the Gateway API acts as a dealer, who works with the queue, receiving the queue status, capturing and processing trade requests, and then reporting the results of their processing.

> Trade queues of all trade servers of one platform are gathered into one common queue, with which the gateway works.

To connect to the queue of trade requests, the Gateway API uses the method [IMTGatewayAPI::DealerStart](Main-Interface/Processing-Trade-Requests/DealerStart.md). After the execution of the method, the queue of trade requests is downloaded in the application, and [events associated with trade requests](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) (IMTRequestSink::OnRequestAdd, IMTRequestSink::OnRequestUpdate and IMTRequestSink::OnRequestDelete) start arriving.

After connecting to the queue, the gateway can start [to handle trade requests](Trade-Operations-in.md).

In general, the procedure of processing trade requests from an application in Gateway API is as follows:

<a id="receiving-a-trade-request-from-the-queue"></a>
## Receiving a Trade Request from the Queue (#receiving-a-trade-request-from-the-queue)

The first step is to receive a trade request from the queue and to determine its type:

  * To connect to the queue of trade requests, the method [IMTGatewayAPI::DealerStart](Main-Interface/Processing-Trade-Requests/DealerStart.md) is used on the server. When connecting, you should also specify the flag of automatic capturing of new trade requests from the queue [IMTGatewayAPI::DEALER_FLAG_AUTOLOCK (#endealerrequestflags)](Main-Interface/Enumerations.md#endealerrequestflags).
  * After that trade requests will be locked in the queue for executing trade operations and will be forwarded to the handler [IMTGatewaySink::OnDealerLock](Event-Interface/OnDealerLock.md).
  * Upon receiving a request in the handler, you should analyze the type of action performed by the request, using the [IMTRequest::Action](../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Action.md) method, as well as the request type using the [IMTRequest::Type](../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Type.md) method.



When connecting to the queue of requests, it is not recommended to use the flags for receiving additional information ([DEALER_FLAG_USER, DEALER_FLAG_ACCOUNT (#endealerrequestflags)](Main-Interface/Enumerations.md#endealerrequestflags) etc.) without the need. This reduces the overall performance of the application.  
---  
  
<a id="mt5-side"></a>
## Processing Trade Operations on the Side of MetaTrader 5 (#mt5-side)

If a request does not require any action on the side of an external trading system (for example, if a Buy Stop Limit order is placed, which should be handled on the side of MetaTrader 5), the request should be confirmed. To do this, use the [IMTGatewayAPI::DealerConfirmCreate](Main-Interface/Processing-Trade-Requests/DealerConfirmCreate.md) method to form the confirmation object [IMTConfirm](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) with the response code [MT_RET_REQUEST_DONE](../Return-Codes/Trade-Requests.md) ([IMTConfirm::Retcode](../Database-Interfaces/Trade/Trade-Requests/IMTConfirm/Requests-Retcode.md)) and pass it in the [IMTGatewayAPI::DealerAnswerAsync](Main-Interface/Processing-Trade-Requests/DealerAnswerAsync.md) method. After that the processing of a trade request is completed.

<a id="processing-trade-operations-in-an-external-system"></a>
## Processing Trade Operations in an External System (#processing-trade-operations-in-an-external-system)

If a request requires some actions on the side of an external trading system, it should be confirmed with the response code [MT_RET_REQUEST_PLACED](../Return-Codes/Trade-Requests.md). Confirmation with this response code is used to notify the platform that this request will be processed in an external system.

Use the [IMTGatewayAPI::DealerConfirmCreate](Main-Interface/Processing-Trade-Requests/DealerConfirmCreate.md) method to form the confirmation object [IMTConfirm](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) with the response code [MT_RET_REQUEST_PLACED](../Return-Codes/Trade-Requests.md) ([IMTConfirm::Retcode](../Database-Interfaces/Trade/Trade-Requests/IMTConfirm/Requests-Retcode.md)) and pass it in the [IMTGatewayAPI::DealerAnswerAsync](Main-Interface/Processing-Trade-Requests/DealerAnswerAsync.md) method.
    
    
    //+------------------------------------------------------------------+
    //| Confirm request for the client                                   |
    //+------------------------------------------------------------------+
    MTAPIRES SendRequestConfirm(const IMTRequest *request)
      {
       MTAPIRES    res=MT_RET_OK;
       IMTConfirm* confirm;
    //--- checks
       if(!m_api_gateway || !request)
          {
           ExtLogger.Out(MTLogErr,L"failed to confirm trade request");
           return(MT_RET_ERR_PARAMS);
          }
    //--- create and sent a confirmation object
       if(confirm=m_api_gateway->DealerConfirmCreate())
          {
           confirm->ID(request->ID();
           confirm->Retcode(MT_RET_REQUEST_PLACED);
           if(m_api_gateway->DealerAnswerAsync(confirm)!=MT_RET_OK)
              {
               ExtLogger.Out(MTLogErr,L"failed to confirm trade request");
               res=MT_RET_ERROR;
              }
         }
       confirm->Release();
    //--- return result
       return(res);
      }

Next, depending on the type of the request being processed, you should notify the trading platform of what operation will be performed on the side of the external trading system. Use the [IMTGatewayAPI::DealerExecutionCreate](Main-Interface/Processing-Trade-Requests/DealerExecutionCreate.md) method to create an object of trade execution [IMTExecution](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md) and specify the appropriate type of operation [IMTExecution::Action](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Action.md) in it (the type of operation is passed as a value of the [IMTExecution::EnTradeExecutions (#entradeexecutions)](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions)) enumeration. For example, at an attempt to place a new order in the external system, you must create an object of trade execution of type IMTExecution::TE_ORDER_NEW_REQUEST. The execution object should be passed in the [IMTGatewayAPI::DealerExecuteAsync](Main-Interface/Processing-Trade-Requests/DealerExecuteAsync.md) method.

> Unlike IMTConfirm based [request execution on the platform side (#mt5-side)](Trade-Operations-in.md#mt5-side), processing of requests via trade executions (IMTExecution) is fully asynchronous. It means that a change in the order state in the platform fully depends on the gateway by which the order was placed. It is guaranteed that after returning control from the IMTGatewayAPI::DealerExecuteAsync method, the execution will be delivered to the MetaTrader 5 trading server, even if the trading server and/or gateway is restarted.
    
    
    //+------------------------------------------------------------------+
    //| Notify the platform about sending a request to external system   |
    //+------------------------------------------------------------------+
    MTAPIRES SendExecutionConfirm(const IMTRequest *request)
      {
       MTAPIRES      res=MT_RET_OK;
       IMTExecution* execution;
    //--- checks
       if(!m_api_gateway || !request)
          {
           ExtLogger.Out(MTLogErr,L"failed to create execution");
           return(MT_RET_ERR_PARAMS);
          }
    //--- create trade execution
       if(execution=m_api_gateway->DealerExecutionCreate())
          {
    //--- specify the order ticket (using initial request) and the execution type only
           execution->Order(request->ResultOrder());
           execution->Action(IMTExecution::TE_ORDER_NEW_REQUEST);
           if(m_api_gateway->DealerExecuteAsync(execution)!=MT_RET_OK)
              {
               ExtLogger.Out(MTLogErr,L"failed to send execution");
               res=MT_RET_ERROR;
              }
         } 
       execution->Release();
    //--- return result
       return(res);
      }

Then you can send a command to the external trading system to execute the corresponding operation (for example, through the FIX protocol).

If the external trading system reports that the operation succeeded, you will need to create another confirmation object of the appropriate type. For example, if a new order has been successfully placed in an external trading system, you should use the method [IMTGatewayAPI::DealerExecutionCreate](Main-Interface/Processing-Trade-Requests/DealerExecutionCreate.md) to create an object of trade execution and specify the type of operation [IMTExecution::TE_ORDER_NEW (#entradeexecutions)](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions) in it. Next, you need to pass this object in the [IMTGatewayAPI::DealerExecuteAsync](Main-Interface/Processing-Trade-Requests/DealerExecuteAsync.md) method. After this, the appropriate order will be created in the MetaTrader 5 platform.
    
    
    //+------------------------------------------------------------------+
    //| Notify about placing an order in external system                 |
    //+------------------------------------------------------------------+
    MTAPIRES SendExecutionNewOrder(const ExchangeOrder &exchange_order)
      {
       MTAPIRES      res=MT_RET_OK;
       IMTExecution* execution;
    //--- check
       if(!m_api_gateway)
          {
           ExtLogger.Out(MTLogErr,L"failed to create new order execution");
           return(MT_RET_ERR_PARAMS);
          }
    //--- create trade execution
       if(execution=m_api_gateway->DealerExecutionCreate())
          {
    //--- fill fields according to the trade execution type
          execution->Order(exchange_order.mt_ticket);
          execution->OrderExternalID(exchange_order.ext_ticket);
          execution->Login(exchange_order.mt_login);
          execution->OrderVolume(exchange_order.volume);
          execution->Symbol(exchange_order.symbol);
          execution->Action(IMTExecution::TE_ORDER_NEW);
           if(m_api_gateway->DealerExecuteAsync(execution)!=MT_RET_OK)
              {
               ExtLogger.Out(MTLogErr,L"failed to send new order execution");
               res=MT_RET_ERROR;
              }
         } 
       execution->Release();
    //--- return result
       return(res);
      }

In case of order execution (full or partial) on the side of the external trading system, you should form a confirmation object of type [IMTExecution::TE_ORDER_FILL (#entradeexecutions)](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions), with its [IMTExecution::Deal*](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-DealVolume.md) parameters filled.
    
    
    //+------------------------------------------------------------------+
    //| Notify about filling an order in external system                 |
    //+------------------------------------------------------------------+
    MTAPIRES SendExecutionOrderFill(const ExchangeOrder &exchange_order)
      {
       MTAPIRES      res=MT_RET_OK;
       IMTExecution* execution;
    //--- check
       if(!m_api_gateway)
          {
           ExtLogger.Out(MTLogErr,L"failed to create new order execution");
           return(MT_RET_ERR_PARAMS);
          }
    //--- create trade execution
       if(execution=m_api_gateway->DealerExecutionCreate())
          {
    //--- fill fields according to the trade execution type
           execution->Order(exchange_order.mt_ticket);
           execution->Symbol(exchange_order.symbol);
           execution->DealAction(exchange_order.type);
           execution->DealVolume(exchange_order.volume);
           execution->DealVolumeRemaind(0);              // 0 means the whole volume of the order is filled
           execution->DealPrice(exchange_order.price);   // price at which the order is filled
           execution->Action(IMTExecution::TE_ORDER_FILL);
           if(m_api_gateway->DealerExecuteAsync(execution)!=MT_RET_OK)
              {
               ExtLogger.Out(MTLogErr,L"failed to send new order execution");
               res=MT_RET_ERROR;
              }
          } 
       execution->Release();
    //--- return result
       return(res);
      }

In case of trade order modification on the side of the external trading system, you should form a confirmation object of type [IMTExecution::TE_ORDER_MODIFY (#entradeexecutions)](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions), with its [IMTExecution::Order*](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-OrderPrice.md) parameters filled (depending on what parameters of the order have been modified).

If the external trading system reports that the operation failed, form a trade execution with one of [IMTExecution::TE_*_REJECT (#entradeexecutions)](../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions) types. For example, if a new order has not been placed, use type IMTExecution::TE_ORDER_REJECT, for a failed order modification, use IMTExecution::TE_ORDER_MODIFY_REJECT, etc.

After that the processing of a trade operation is completed.

> In each case, the parameters that correspond to the type of operation executed in the external trading system, should be filled in the trade execution object. Example:

<a id="executions"></a>
## A Database of Trade Executions (#executions)

The gateway and the trade server store information about trade executions in order to maintain correct operation in case of failures or connection interruptions:

  * The executions.dat file on the server side. The number of the last trade execution processed by the server (A) is stored in this file. When the next execution is received, the number of the last processed execution is overwritten in this file.
  * Files executions-*.dat and executions-*.idx are stored on the gateway side. They store the number of the last execution sent to a trade server (B), as well as a database of executions, which are ready for sending.



When connection is established, the server sends to the gateway the number of the last processed execution (A). The gateway analyzes this information and sends to the server all executions from its executions-*.dat database, whose numbers are greater than the one sent by the server. Thus, trading executions will not be missed even in case of a failure, since after the restoration of connection the gateway will pass to the server all unsent executions, which are stored in its database on a disk. 

If the number (A) received by the gateway from the server is greater than the last sent execution (B), which is also greater than the numbers of all executions in the gateway database, then it is considered that the execution databases have been changed on the gateway side or on the server side. An appropriate message is written to the gateway log in this case:

2018.04.16 15:12:55.111 TradeExecutions last execution id 13226 on the Trade Server 1 is greater than last execution id 13208 in the gateway database   
2018.04.16 15:12:55.112 TradeExecutions probably, 'executions-1.dat' on the gateway side or 'executions.dat' on the server side was changed, numbering will be continued from 13209  
---  
  
No executions will be skipped in this case. The server will process all executions sent by the gateway. The numbering of executions in the server database will continue from the last execution number sent by the gateway (B+1).

> Do not delete or change the databases of executions manually. Also, do not move these databases between different servers. This can lead to serious errors in the operation of the trading platform and the gateway.
