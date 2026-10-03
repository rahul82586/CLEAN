[🏠 Document Start](../README.md) / [Server API](README.md) / Recommendations for Developers

[Previous](Request-Processing-on-the-Server.md) | [Next](Debugging.md)

<a id="recommendations-for-developers"></a>
# Recommendations for Developers (#recommendations-for-developers)

This section contains general recommendations and solutions of typical issues programmers face when developing plugins.

<a id="multithread"></a>
## Multithreading (#multithread)

When writing a multithreaded application, a programmer must take into account some specific features of MetaTrader 5 Server API:

  * Calling Server API methods (methods of interface IMTServerAPI, e.g. the functions [IMTServerAPI::Group*](Main-API-Interface/Configuration-Databases/Groups.md), [IMTServerAPI::Symbol*](Main-API-Interface/Configuration-Databases/Symbols.md), etc.) is thread safe. In using them, the does not need to ensure synchronization of access for simultaneous access to the same object of the server API from different threads. In other words, methods of the IMTServerAPI interface can be simultaneously called from different threads without additional synchronization.
  * Calling of interface methods (e.g. interfaces of configuration bases: [IMTConGroup](../Configuration-Interfaces/Groups/IMTConGroup.md), [IMTConSymbol](../Configuration-Interfaces/Symbols/IMTConSymbol.md), [IMTConGateway](../Configuration-Interfaces/Gateways/IMTConGateway.md), etc.) is not thread safe. When accessing the same object from two threads, the programmer must ensure synchronization of access.
  * It is not guaranteed that hooks and events are called sequentially. Several hooks or events (even of the same type) can be called simultaneously, and each of them will be called in a separate thread. Accordingly, the handlers of (hooks) must be thread safe.
  * Synchronous calling from events/hooks of a client base (for example, [IMTUserSink](../Database-Interfaces/Users/IMTUserSink.md)) to a trade base is forbidden in plugins. Violation of this rule may cause deadlocks and trade server crash.
  * Calling from trading events and hooks to the client base is allowed. All [IMTServerAPI::User*](Main-API-Interface/Users.md) methods can be used except for those related to trading activity: [IMTServerAPI::UserAccountGet](Main-API-Interface/Users/UserAccountGet.md), [IMTServerAPI::UserDepositChange](Main-API-Interface/Users/UserDepositChange.md) and [IMTServerAPI::UserDepositChangeRaw](Main-API-Interface/Users/UserDepositChangeRaw.md).



> All the plugin components must be implemented thread-safe, except for calls of IMTServerAPI methods.

<a id="multithread-interaction"></a>
## Multithreaded interaction with the trade server (#multithread-interaction)

We strongly advise you against interfering with the server threads operation and interaction logic. In particular, we urge you not to implement your own synchronization primitives affecting the server threads operation (i.e. not to use them in the [hooks](Hooks.md)).

When developing an application, keep in mind the following:

  * The unit of grouping data on client's open orders and positions is a client group. It manages client's open orders and positions, as well as margin status. Each group has its own synchronization primitive.
  * Trading bases (open orders, history orders, deals, positions) also feature their own synchronization primitives.
  * In general, requests are handled sequentially by a group of threads: initial control, routing and execution ones. When executing tasks, these threads access the corresponding client groups using synchronization primitives (securing exclusive access — lock) among other things.
  * Incoming quotes as well as trade symbol and group changes are handled by a separate thread pool. When executing tasks, these threads also access the corresponding client groups using synchronization primitives among other things.
  * All incoming trading executions ([IMTExecution](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md)) of gateways are put in a separate queue and processed by a separate thread. When handling execution, this thread accesses the corresponding client groups using synchronization primitives. Trading executions are handled by the thread sequentially in the order of their receipt.
  * A significant number of events and hooks are called under the lock, including the lock of the group synchronization primitive and the lock of a certain database (orders, positions, deals).
  * The entire interaction of trading and client databases is unidirectional - the trading base always refers to the client base, but not vice versa.



In order to avoid deadlocks when working from trading events and hooks, do the following:

  * Minimize direct (receiving data) and indirect (calculating a margin for a certain request, etc.) access to the data located in other groups: client's open orders, positions and trading account data.
  * Minimize the use of your custom synchronization primitives.
  * Do not try to directly control the interaction of server internal threads by explicitly stopping them or applying synchronization primitives.
  * The hooks and client base events (for example, [IMTUserSink::OnUser*](../Database-Interfaces/Users/IMTUserSink/OnUserAdd.md), [IMTUserSink::HookUser*](../Database-Interfaces/Users/IMTUserSink/HookUserAdd.md)) should not contain calls of the API methods associated with the trading databases (for example, [IMTServerAPI::PositionGet](Main-API-Interface/Trade/Positions/PositionGet.md)).
  * In [IMTDealSink](../Database-Interfaces/Trade/Deals/IMTDealSink.md) events, it is only allowed to use synchronous calls of methods changing, creating and deleting only those deals which are in the same groups as the deal for which the event was received. In all other cases, you should use asynchronous calls — API methods should be called in a separate thread, and not in the thread that triggers the events of the deal database.



<a id="memory-manage"></a>
## Memory Management (#memory-manage)

The correct approach to the use of memory is one of the key points in the development of plugins. There are the following requirements for working with memory:

  * Since the DLL modules of plugins work in the address space of the server, the plugin must be memory efficient. In addition, the plugin should have limited memory re-allocation to prevent it from too much fragmentation.
  * All interface objects are allocated using the Create methods and removed using the Release methods.
  * In cases where the API itself allocates memory (e.g., the function [IMTServerAPI::UserLogins](Main-API-Interface/Users/UserLogins.md), which returns a dynamic array of clients from the specified group), it is necessary to free the memory using the method [IMTServerAPI::Free](Main-API-Interface/Common-Functions/Free.md).  
Pair to the method IMTServerAPI::Free is the method [IMTServerAPI::Allocate](Main-API-Interface/Common-Functions/Allocate.md), which allows to allocate memory.



<a id="base"></a>
## Working with the configuration base and database interfaces (#base)

When working with [configuration base](../Configuration-Interfaces/README.md) and [database](../Database-Interfaces/README.md) interfaces, please consider the following features:

  * Any *Add, *Update, *Delete and *Clear methods of these interfaces only affect the appropriate local object. To send changes to a server, you should call the corresponding *Add or *Update method of the Server API. For example, the [IMTConGroup::SymbolUpdate](../Configuration-Interfaces/Groups/IMTConGroup/SymbolUpdate.md) method only updates a symbol configuration in the group object. To send these changes to a server, you should call the [IMTServerAPI::GroupAdd](Main-API-Interface/Configuration-Databases/Groups/GroupAdd.md) method.



<a id="escape"></a>
# Escaping special characters (#escape)

When using special characters = (equal sign), | (vertical bar), \ (slash) and line feed as method parameter values, you must escape them with the \ (slash) character.

> If the \ (slash) character is not followed by special characters listed above, then it is processed as is.

The table below shows examples of processing escaped characters on a trading server.

Character sent to the server | character recognized by the server  
---|---  
\= | =  
\| | |  
\(line feed) | (line feed)  
\\\ | \
