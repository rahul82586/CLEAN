[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUpdateBatch

[Previous](SymbolUpdate.md) | [Next](SymbolDelete.md)

# IMTAdminAPI::SymbolUpdateBatch

Add or edit multiple symbol configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolUpdateBatch(
       IMTConSymbol**    configs,      // An array of configurations
       const UINT        config_total, // The number of configurations in the array
       MTAPIRES*         results       // An array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolUpdateBatch(
       CIMTConSymbol[]   configs,      // An array of configurations
       MTRetCode[]       results       // An array of results
       )

Python
    
    
    AdminAPI.SymbolUpdateBatch(
       configs           # An array of configurations
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to add/update.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of applying of each configuration change on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful sending of changes to a server; results of applying the changes are passed in the 'results' parameter.

### Further Note

A configuration can only be added or updated from the applications that run on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.

### C++ Example
    
    
    //+------------------------------------------------------------------+
    //| Update multiple symbols                                          |
    //+------------------------------------------------------------------+
    MTAPIRES MarginLimitUpdateBatch(double new_rate, IMTAdminAPI* manager)
      {
      UINT           symbols_prepared=0,total;
      IMTConSymbol  *symbol;
      MTAPIRES       res=MT_RET_OK;
    //--- checks
      if(!manager || (total=manager->SymbolTotal())<1)
        return(MT_RET_ERR_PARAMS);
    //--- allocate arrays
      IMTConSymbol **symbols=new IMTConSymbol*[total];  
      MTAPIRES      *results=new MTAPIRES[total];
    //--- go through all symbols and save them in an array
      for(UINT i=0;i<total; i++)
        {
         symbol=manager->SymbolCreate();
         //--- get a symbol
         if(res=manager->SymbolNext(i,symbol)==MT_RET_OK)
           {
            //--- if successful, write to the array
            symbols[i]=symbol;
            wprintf_s(L"Symbol %s loaded\n",symbol->Symbol());        
            //--- change margin rate in own array
            if(res=symbols[i]->MarginRateInitial(IMTConSymbol::MARGIN_RATE_BUY_LIMIT,new_rate)==MT_RET_OK)
              {       
               wprintf_s(L"Symbol %s updated\n",symbols[i]->Symbol());
               symbols_prepared++;
              }
            }
         else
           symbol->Release();
        }
    //--- send changes
       if(res=manager->SymbolUpdateBatch(symbols,symbols_prepared,results)==MT_RET_OK)
         {
          for(UINT i=0;i<symbols_prepared;i++)
            wprintf_s(L"%s update result - %u\n",symbols[i]->Symbol(),results[i]);
         }
    //--- release objects
      for(UINT i=0;i<symbols_prepared;i++)
        symbols[i]->Release();
      delete[] symbols;
      delete[] results;
    //--- return result
      return(res);
     }

### .NET Example
    
    
    //+------------------------------------------------------------------+
    //| Batch update of tick value in symbol configuration       |
    //+------------------------------------------------------------------+
    static MTRetCode TickValueUpdateBatch(double new_tick_value, CIMTAdminAPI admin)
      {
       uint          symbols_prepared=0;
       uint          symbols_total   =0;
       CIMTConSymbol symbol          =null;
       MTRetCode     res             =MTRetCode.MT_RET_OK;
       //--- Checking
       if(admin==null)
         return(MTRetCode.MT_RET_ERR_PARAMS);
       //--- Get the number of symbols
       symbols_total=admin.SymbolTotal();
       if(symbols_total<1)
         return(MTRetCode.MT_RET_ERR_PARAMS);
       //--- Output the number of symbols to journal
       Console.WriteLine("Total symbols to update = {0}", symbols_total);
       //--- Create arrays
    .   CIMTConSymbol[] symbols=new CIMTConSymbol[symbols_total];  
       MTRetCode[]     results=new MTRetCode[symbols_total];
       //--- Check all symbols and save them to array
       for(uint i=0;i<symbols_total;i++)
         {
          symbol=admin.SymbolCreate();
          //--- Get the symbol
          res=admin.SymbolNext(i,symbol);
          if(res==MTRetCode.MT_RET_OK)
            {
             //--- If successful, write to array
             symbols[i]=symbol;
             Console.WriteLine("Symbol {0} loaded", symbol.Symbol());
             //--- Update tick value in our array
             res=symbols[i].TickValue(new_tick_value);
             if(res==MTRetCode.MT_RET_OK)
               { 
                Console.WriteLine("Updated \a symbol \a {0}", symbols[i].Symbol());      
                symbols_prepared++;
               }
            }
          else
            {
             symbol.Release();
            }
          }
          //--- Send changes
          res=admin.SymbolUpdateBatch(symbols,results);
          if(res==MTRetCode.MT_RET_OK)
            {
             for(uint i=0; i<results.Length; i++)
             Console.WriteLine("{0} update result - {1}", symbols[i].Symbol(),results[i]); 
            }
          //--- Free memory
          for(uint i=0; i<symbols_prepared; i++)
            symbols[i].Release();
          //--- Return the result
          return(res);
      }
