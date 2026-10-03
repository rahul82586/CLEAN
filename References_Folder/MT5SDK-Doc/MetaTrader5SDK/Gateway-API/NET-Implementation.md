[🏠 Document Start](../README.md) / [Gateway API](README.md) / .NET Implementation

[Previous](Development-of-Data-Feeds.md) | [Next](Exported-Functions.md)

# Implementation of MetaTrader 5 Gateway API in .NET

The MetaTrader 5 Gateway API includes a ready implementation in .NET. The implementation is available in the form of ready to use DLLs. To be able to use their functions, you need to add them to a project.

The libraries are available in [SDK installation folder]\Libs:

  * MetaQuotes.MT5CommonAPI(64).dll — library of common API interfaces ([configuration bases](../Configuration-Interfaces/README.md) and [databases](../Database-Interfaces/README.md)).
  * MetaQuotes.MT5GatewayAPI(64).dll — Gateway API library.



Aside from DLLs, the package includes examples TextFeeder.NET and UniFeeder.NET. They are available in [Gateway API installation folder]\Examples.

  * .NET Framework 4.7.2 or newer and all [Visual C++ Redistributable for Visual Studio packages starting from 2015](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) are required to develop applications.


  * .NET implementation is a wrapper over the main Gateway API C++ library. Therefore, the MT5APIGateway(64).dll file is also required.

  
---  
  
## Basic Terms

A short glossary of the terms used:

  * Managed — code, method, class running in the .NET CLI environment with the so called garbage collection management via the [GC class](https://msdn.microsoft.com/ru-ru/library/system.gc%28v=vs.110%29.aspx). The class controls the system garbage collector — the service that automatically releases unused memory.
  * Native — the native code, method, class running directly in the operating system environment.
  * Native code or API — classes and interfaces of API.
  * Managed wrapper — a .NET class providing an interface of the native API without inheritance.
  * Unsafe code — code in C# or any other managed language that can access pointers, low-level memory management, etc.



## Use the reference of the native Gateway API for the .NET wrapper — almost all functions and methods are identical

All managed wrappers are identical to their native interfaces except for the methods that use arrays. For example:
    
    
    // Native API
    MTAPIRES  ChartUpdate(LPCWSTR symbol,const MTChartBar *bars,const UINT bars_total)=0;
    // Managed API C#
    MTAPIRES  ChartUpdate(string symbol,MetaQuotes.MT5CommonAPI.MTChartBar[] bars)...
    // Managed API C++
    MTAPIRES  ChartUpdate(String^ symbol,array<MetaQuotes.MT5CommonAPI.MTChartBar>^ bars)...

## No Exceptions

Managed wrappers do not generate exceptions. If any library calls generate exceptions, the wrapped code will not let them out.

## Always Use Factory

All managed wrappers of API interfaces should only be created using factories, special methods (for example, [UserCreate](Main-Interface/Users/UserCreate.md), [UserCreateAccount](Main-Interface/Users/UserCreateAccount.md), etc.). This will prevent from passing incorrect pointers to the native code and from using unsafe client code. A separate factory is implemented for each API library.

## Register Event Handler Classes, Do Not Allow Exceptions

For sink classes, you must call the RegisterSink method in the child class constructor and check the return value. This is connected with the possibility to process errors binding a native sink interface to its managed wrapper.

It is important to not let exceptions out of the sink classes handler methods. Otherwise, logging exceptions will be impossible. It is especially important not to let the exceptions out of the hook methods, which may cause unpredictable behavior of the trading platform.

## Use the "using" Operator

All API managed wrappers inherit the [IDisposable](https://msdn.microsoft.com/ru-ru/library/system.idisposable%28v=vs.110%29.aspx) interface, which provides a mechanism for releasing unmanaged resources. Use the ["using"](https://msdn.microsoft.com/ru-ru/library/yh598w02.aspx) operator for easy and correct use of IDispose objects.
    
    
    void UserFunction()
      {
    ...
       using(CIMTConSymbol symbol=m_gateway.SymbolCreate())
         {
          symbol.Symbol("<SymbolName>");
    ...
          symbol.Path("<SymnolPath>");
    ...
          m_gateway.SymbolAddPreliminary(symbol);
         }
         //--- Will surely destroy the 'symbol' object and its native resources
      }

In the above example, the 'user' object and its native resources will be released once code execution exits the 'using' block. Without using the "using" operator, it is unknown when and under what circumstances the object will be deleted.

> To explicitly release resources, you can also use the 'Release' and 'Dispose' methods of managed wrappers. These methods are similar.

## ToArray Methods in Managed Wrappers for Working with Arrays

ToARray methods are implemented in all managed wrappers for working with array objects, such as [CIMTUserArray](../Database-Interfaces/Users/IMTUserArray.md), [CIMTOrderArray](../Database-Interfaces/Trade/Orders/IMTOrderArray.md) and others. These methods create an array and fill it with the elements of the array source object.

  * No element copying is performed during ToArray call. Elements in the new array refer to the elements of the original array. Therefore, when an element is destroyed by calling Dispose or Release in one array, the appropriate element becomes invalid (destroyed) on the other array. Do not call Dispose/Release methods for the []ToArray array elements.
  * Use the Detach method to detach an element from the array object (CIMT*Array).
  * If the source array does not have elements, ToArray returns an empty array, not nullptr.



## Memory Management

Memory in .NET implementation is managed by the programmer. The programmer must explicitly call the Dispose or Release methods for the created objects in the required places of the application. In .NET finalizers memory is not released automatically: if a .NET wrapper object is not released through Dispose, it will lead to memory and native API object leaks.

When working with the .NET implementation, a situation may occur where two or more wrappers refer to the same native object. For example, this may occur when using the aforementioned ToArray methods. In this case, the programmer must control the lifetime of the objects and avoid access to already released objects.

> Dispose and Release perform the same function, i.e. they release the previously created object. Dispose is designed to match the .NET style and enable the use of the 'using' construct.

## Operation Speed

The speed of calling wrapped methods is much slower than calling its native analogue. This is connected with the check of the native pointer, managed arguments, etc.

Speed ​​of calls of some wrapped methods that return arrays, particularly arrays of structures, can slow down performance significantly. Example — creating a copy of the array:
    
    
    array<INT64>^ CIMTGatewayAPI::UserLogins(MTRetCode% res)
            {
             res=MTRetCode::MT_RET_ERR_MEM;
             array<INT64>^ result=nullptr;
             if(m_this)
               {
                INT64* narray=NULL;
                UINT   total =0;
                //--- Call implementation
                if((res=(MTRetCode)m_this->UserLogins(res))==MTRetCode::MT_RET_OK)
                  {
                   res=(MTRetCode)NativeToManagedArrayCopy(result,narray,total);
                   //--- release the native array
                   if(narray) m_this->Free(narray);
                  }
               }
             return(result);
            }

Example of using the .NET wrapper of Gateway API
    
    
    namespace SomeClientNamespace
      {
       using MetaQuotes.MT5CommonAPI;
       using MetaQuotes.MT5GatewayAPI;
       using System;
    ...
       class CSomeClientClass
         {
          //--- Gateway API
          public CIMTGatewayAPI m_gateway=null;
              public CDataSource    m_source=null;
    ...
          public MTRetCode Initialize()
            {
             MTRetCode res=MTRetCode.MT_RET_ERROR;
             //--- Initialize the factory
             if((res=SMTGatewayAPIFactory.Initialize())!=MTRetCode.MT_RET_OK)
               {
                LogOutFormat("SMTGatewayAPIFactory.Initialize failed - {0}",res);
                return(res);
               }
             //--- Receive the API version
             uint version=0;
             if((res=SMTGatewayAPIFactory.GetVersion(out version))!=MTRetCode.MT_RET_OK)
               {
                LogOut("SMTGatewayAPIFactory.GetVersion failed - {0}",res);
                return(res);
               }
             //--- Compare the obtained version with the library one
             if(version!=SMTGatewayAPIFactory.GatewayAPIVersion)
               {
                LogOutFormat("Gateway API version mismatch - {0}!={1}",version,SMTGatewayAPIFactory.GatewayAPIVersion);
                return(MTRetCode.MT_RET_ERROR);
               }
             //--- Create an instance
             m_gateway=SMTGatewayAPIFactory.CreateGateway(SMTGatewayAPIFactory.GatewayAPIVersion,out res);
             if(res!=MTRetCode.MT_RET_OK)
               {
                LogOut("SMTGatewayAPIFactory.CreateGateway failed - {0}",res);
                return(res);
               }
             //--- For some reasons, the creation method returned OK and the null pointer
             if(m_gateway==null)
               {
                LogOut("SMTGatewayAPIFactory.CreateGateway was ok, but GatewayAPI is null");
                return(MTRetCode.MT_RET_ERR_MEM);
               }
             //--- All is well
             LogOutFormat("Using GatewayAPI v. {0}", version);
                     //--- create the data feed
             m_source=new CDataSource();            
             return (res);
            }
    ...
          //+------------------------------------------------------------------+
          //| Data feed operation                                              |
          //+------------------------------------------------------------------+
          public bool Run(string address=null)
            {
             bool started=false;
             //--- Check
             if(m_gateway==null || m_source==null)
                return(false);
             //--- start processing external connections
             if(started=m_source.Start(m_gateway))
               {
                //--- start receiving incoming connections
                started=m_gateway.Start(this,address)==MTRetCode.MT_RET_OK;
               }
             //--- set the flag if the launch is successful
             if(started)
                Interlocked.Exchange(ref m_workflag,1);
             //--- main cycle of external connections management
             while(Interlocked.Add(ref m_workflag,0)!=0)
               {
                //--- check the external connection
                if(!m_source.Check())
                   break;
                //--- waiting
                Thread.Sleep((int)constants.SLEEP_TIMEOUT);
               }
             //--- end operation
             m_gateway.Stop();
             m_source.Shutdown();
             //--- All is well
             return(true);
            }
    ...
          //+------------------------------------------------------------------+
          //| Receive the data feed description                                |
          //+------------------------------------------------------------------+
          public override void OnGatewayConfig(UInt64 login,CIMTConFeeder config)
            {
             //--- performing operation
             if(m_source!=null)
                m_source.Init(config);
            }
    ...
         }
      }
