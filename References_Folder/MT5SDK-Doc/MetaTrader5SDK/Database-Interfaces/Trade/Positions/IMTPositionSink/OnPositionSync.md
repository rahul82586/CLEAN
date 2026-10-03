[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionSink](../IMTPositionSink.md) / OnPositionSync

[Previous](OnPositionClean.md) | [Next](../../Accounts.md)

# IMTPositionSink::OnPositionSync

A handler of the event of synchronization of a database of trade positions.

C++
    
    
    virtual void  IMTPositionSink::OnPositionSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTPositionSink.OnPositionSync()

### Note

This method is called by the API to notify that synchronization of a database of trading positions is completed.

  * Server API — between the trade server and its backup server.
  * Manager API — between the trade server and the local data cache of the application.


