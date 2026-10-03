[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureSink](../IMTExposureSink.md) / OnExposureUpdate

[Previous](../IMTExposureSink.md) | [Next](../../Daily-Reports.md)

# IMTExposureSink::OnExposureUpdate

A handler of the exposure modification event.

C++
    
    
    virtual void  IMTExposureSink::OnExposureUpdate(
       const IMTExposure*  exposure      // A pointer to the asset record object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTExposureSink.OnExposureUpdate(
       CIMTExposure        exposure      // The asset record object
       )

### Parameters

**exposure**  
[in] A pointer to the object of the updated asset record.

### Note

This method is called by the API to notify that an asset record has been modified.
