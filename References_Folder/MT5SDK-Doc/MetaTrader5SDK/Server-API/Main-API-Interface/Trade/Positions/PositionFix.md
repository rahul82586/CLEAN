[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionFix

[Previous](PositionCheck.md) | [Next](PositionSplit.md)

# IMTServerAPI::PositionFix

Correcting a client's positions based on the history of his deals.
    
    
    MTAPIRES  IMTServerAPI::PositionFix(
       const UINT64       login,        // The user's login
       IMTPositionArray*  current       // Client's positions after correction
       )

### Parameters

**login**  
[in] The login of a user.

**current**  
[out] The array of the client's positions after correction based on the history. The 'current' object must be first created using theIMTServerAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Disclaimer

Upon the call of the method, the platform calculates a client's positions based on the history of his deals, and corrects current positions if necessary.
