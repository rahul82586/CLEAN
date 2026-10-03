[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderDelete

[Previous](OrderUpdateBatchArray.md) | [Next](OrderDeleteBatch.md)

# IMTServerAPI::OrderDelete

Delete an open trade order from the server data base.
    
    
    MTAPIRES  IMTServerAPI::OrderDelete(
       const UINT64  ticket      // The ticket of an order
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An order can be deleted only from the plugins that run on the same trade server where the order was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

### Example: deleting a pending order in case of a partial execution
    
    
    //+------------------------------------------------------------------+
    //| Pending order deletion example in case of a partial execution    |
    //| remaining part is canceled, order is substituted in history      |
    //+------------------------------------------------------------------+
    void CPluginInstance::OnDealPerform(const IMTDeal *deal,IMTAccount *account,IMTPosition *position)
    {
       IMTOrder     *order,*order_new =NULL;
       IMTDeal      *record=NULL;
       MTAPIRES      retcode;
       //--- checks
       if(!deal || !m_api) return;
       //--- Creating an order object
       if((order = m_api->OrderCreate()) == NULL)
         {
          m_api->LoggerOut(MTLogOK, L"Failed to create order object");
          return;
         }      
       //--- Getting the order, as a result of which the deal was executed
       if(m_api->OrderGet(deal->Order(), order)!=MT_RET_OK)
         {
          m_api->LoggerOut(MTLogOK, L"Failed to get order: [%d]", retcode);
          order->Release();
           return;
         }
       //--- Only operate with partially filled orders
       if(order->State()==IMTOrder::ORDER_STATE_PARTIAL)
         {
          //--- Creating a new order object
          if((order_new= m_api->OrderCreate())==NULL)
            {
             m_api->LoggerOut(MTLogOK, L"Failed to create new order object");
             order->Release();
             return;
          }
          //--- deleting an old order and preparing a new one
          if(m_api->OrderDelete(order->Order())==MT_RET_OK)
            {
             m_api->LoggerOut(MTLogOK, L"Order %I64u deleted", order->Order());
             //--- Forming a new order based on the old one, but with the remaining volume
             order_new->Symbol(order->Symbol());
             order_new->Login(order->Login());
             order_new->Type(order->Type());
             order_new->Digits(order->Digits());
             order_new->DigitsCurrency(order->DigitsCurrency());
             order_new->ContractSize(order->ContractSize());
             order_new->OrderSet(order->Order());
             order_new->StateSet(IMTOrder::ORDER_STATE_FILLED);
             order_new->PriceOrder(order->PriceOrder());
             order_new->TimeSetup(order->TimeSetup());
             order_new->TimeDone(m_api->TimeCurrent());
             order_new->VolumeInitial(order->VolumeCurrent()); //--- The initial volume is set to the actual filled volume
             order_new->VolumeCurrent(0);                      //--- Unfilled volume is set to zero, because the order is considered to be fully executed
             if(m_api->HistoryAdd(order_new)==MT_RET_OK)
              {
               m_api->LoggerOut(MTLogOK, L"Order %I64u added to history", order_new->Order());
              }
             else
               {
                m_api->LoggerOut(MTLogOK, L"Failed to add order to history: [%d]", retcode);
               }
            }
          else
            {
             m_api->LoggerOut(MTLogOK, L"Failed to delete order: [%d]", retcode);
            }
          //--- Release resources
          order_new->Release();
         }
       //--- Release resources
       order->Release();
       return;
    }
    //+------------------------------------------------------------------+
