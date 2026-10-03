[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealPerform

[Previous](DealSelectByLogins.md) | [Next](DealPerformCloseBy.md)

# IMTServerAPI::DealPerform

Perform a deal on the client's account. This method performs a market buy or sell operation on an account, as if it is performed by the client through the terminal. The only difference is that no trade request and no order is created to perform the deal, and thus routing rules are not applied to the operation. In all other respects, the behavior is the same: the deal execution result is applied to the position and the account trading state; commission is calculated and charged for the deal in accordance with the relevant account group settings.
    
    
    MTAPIRES  IMTServerAPI::DealPerform(
       IMTDeal*  deal      // An object of a deal
       )

### Parameters

**deal**  
[in/out] An object of the deal. The deal object must be first created using theIMTServerAPI::DealCreatemethod.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code means that the deal has been successfully created. The object of the executed deal from the server base is added to 'deal'. If a deal could not be executed, the method returns a corresponding error code.

### Note

A deal can only be performed on the account existing on the same server, on which the plugin is running.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md) (only values IMTDeal::DEAL_BUY and IMTDeal::DEAL_SELL are allowed)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::PositionID](../../../../Database-Interfaces/Trade/Deals/IMTDeal/PositionID.md) (when closing a position on a hedging account)



You can additionally specify in a deal an individual margin recalculation rate ([IMTDeal::RateMargin](../../../../Database-Interfaces/Trade/Deals/IMTDeal/RateMargin.md)) and profit recalculation rate([IMTDeal::RateProfit](../../../../Database-Interfaces/Trade/Deals/IMTDeal/RateProfit.md)). If you do not specify them calculated rates will be used.

If commission ([IMTDeal::Commission](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Commission.md)) is specified in a deal, this commission will be applied to the trading account. However, it does not replace the commission charged in accordance with the trader's group settings ([IMTConGroup::Commission*](../../../../Configuration-Interfaces/Groups/IMTConGroup/CommissionAdd.md)). Therefore, the commission specified in the deal is summed up with the calculated commission. 

The profit of a deal is always calculated by the server, even if you specify profit in the [IMTDeal::Profit](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Profit.md) field. The server automatically charges commission on a deal if necessary (in accordance with [commission settings](../../../../Configuration-Interfaces/Groups/IMTConCommission.md)).

It is not recommended to call IMTServerAPI::DealPerform from the following handlers: [IMTDealSink::OnDealAdd](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealAdd.md), [IMTDealSink::OnDealUpdate](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealUpdate.md) and [IMTDealSink::OnDealPerform](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealPerform.md).

### An example of closing positions (even if trading is disabled for an instrument)
    
    
    //+------------------------------------------------------------------+
    //| Closing client's all positions at the current price              |
    //+------------------------------------------------------------------+
    MTAPIRES CPluginInstance::CloseAll(UINT64 login)
      {
       IMTPositionArray* positions={0};
       IMTDeal*          deal_tmp ={0};
       IMTPosition*      pos_tmp={0};
       MTAPIRES          res;
       //--- Check
       if(m_api)
         {
          positions=m_api->PositionCreateArray();
          deal_tmp=m_api->DealCreate();
          pos_tmp=m_api->PositionCreate();
         }
       else return(MT_RET_ERR_PARAMS);
       //--- Get positions
       if(res=m_api->PositionGet(login, positions)!=MT_RET_OK)
         {
          m_api->LoggerOut(MTLogOK, L"PositionGet failed [%d]", res);
          return(MT_RET_ERR_PARAMS);
         }
       else
         {
          m_api->LoggerOut(MTLogOK, L"client '%I64u' has %d positions, try to close them", login, positions->Total());
          //---
          for(UINT index=0;index<positions->Total();index++)
            {
             pos_tmp=positions->Next(index);
             if(pos_tmp)
               {
                //--- Fill the deal object
                deal_tmp->Login(pos_tmp->Login());
                deal_tmp->Symbol(pos_tmp->Symbol());
                //--- Set the direction of the closing deal depending on the position direction
                if(pos_tmp->Action() == IMTPosition::POSITION_BUY)
                   deal_tmp->Action(IMTDeal::DEAL_SELL);
                else
                   deal_tmp->Action(IMTDeal::DEAL_BUY);
                //--- Fill other deal parameters
                deal_tmp->Volume(pos_tmp->Volume());
                deal_tmp->Price(pos_tmp->PriceCurrent());
                deal_tmp->PositionID(pos_tmp->Position()); // Only filled for hedging accounts
                //--- Close position            
                if(res=m_api->DealPerform(deal_tmp)!=MT_RET_OK)
                   m_api->LoggerOut(MTLogOK, L"DealPerform failed [%d]", res);
               }
            }
         }
       //--- Clear objects
       if(positions)
          positions->Release();
       //--- Clear objects
       if(pos_tmp)
          pos_tmp->Release();
        //--- Clear objects
        if(deal_tmp)
           deal_tmp->Release();
    }
    //+------------------------------------------------------------------+
