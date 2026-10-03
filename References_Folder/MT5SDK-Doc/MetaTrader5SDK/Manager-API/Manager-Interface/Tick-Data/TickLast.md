[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickLast

[Previous](TickAddStat.md) | [Next](TickLastRaw.md)

# IMTManagerAPI::TickLast

Get the last quote of a symbol taking into account spread difference settings ([IMTConGroupSymbol::SpreadDiff](../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiff.md)) for the group of the manager account, which is used for Manager API [connection](../Connection-to-the-Server/Connect.md).

C++
    
    
    MTAPIRES  IMTManagerAPI::TickLast(
       LPCWSTR       symbol,     // Symbol
       MTTickShort&  tick        // Reference to the quote structure
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickLast(
       string        symbol,     // Symbol
       MTTickShort   tick        // Quotes structure
       )

Python
    
    
    ManagerAPI.TickLast(
       symbol        # Symbol
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get a quote.

**tick**  
[out] A reference to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The symbol for which data are requested must be included into the [list of selected symbols](../Selected-Symbols.md).

# IMTManagerAPI::TickLast

Get the last quote of a symbol taking into account spread widening settings ([IMTConGroupSymbol::SpreadDiff](../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiff.md)) of the specified group.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickLast(
       LPCWSTR       symbol,  // Symbol
       LPCWSTR       group,   // Group
       MTTickShort&  tick     // Reference to the quote structure
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickLast(
       string           symbol, // Symbol
       string           group,  // Group
       out MTTickShort  tick    // Quote structure
       )

Python
    
    
    ManagerAPI.TickLast(
       symbol,          # Symbol
       group            # Group
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get a quote.

**group**  
[in] A group, whosespread difference settingsare applied to the quote.

**tick**  
[out] A reference to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The symbol for which data are requested must be included into the [list of selected symbols](../Selected-Symbols.md).

### Example
    
    
    //--- connect manager in the full pumping mode
    res=manager->Connect(server,login,password,L"",IMTManagerAPI::PUMP_MODE_FULL,MT5_TIMEOUT_CONNECT);
    if(res!=MT_RET_OK)
       wprintf_s(L"Manager connection failed (%u)\n",res);
     else 
       wprintf_s(L"manager connected\n");
    //---
    if(manager)
      {
       BOOL        stop_flag=FALSE;
       LPCWSTR     symbol=L"EURUSD";
       LPCWSTR     group=L"demo\\demoforex";
       SYSTEMTIME  current_tick_time={0};
       MTTickShort ticks;
       //--- add the symbol to the list of selected symbols
       manager->SelectedAdd(symbol);
       //--- get last ticks in a loop
       while(!stop_flag)
         {
          //--- get the last tick considering the group settings
          res=manager->TickLast(symbol,group,ticks);
          //--- if the ticks has been requested successfully, print its details to the journal
          if(res==MT_RET_OK)
            {
             SMTTime::TimeToST(ticks.datetime, current_tick_time);
             wprintf_s(L"current tick time: %04d.%02d.%02d %02d:%02d:%02d :: %02d\n",current_tick_time.wYear,current_tick_time.wMonth,current_tick_time.wDay,current_tick_time.wHour,current_tick_time.wMinute,current_tick_time.wSecond,current_tick_time.wMilliseconds);
             wprintf_s(L"symbol %s TickLast: current bid = %.5lf current ask = %.5lf\n",symbol,ticks.bid,ticks.ask);
            }
          else
            {
             wprintf_s(L"symbol %s TickLast failed (%u)\n",symbol,res);
            }
          //--- wait
          Sleep(1000);
         }
      }
