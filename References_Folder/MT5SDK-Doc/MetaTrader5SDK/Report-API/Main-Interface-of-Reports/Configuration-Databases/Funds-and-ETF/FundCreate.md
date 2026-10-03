[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Funds and ETF](../Funds-and-ETF.md) / FundCreate

[Previous](../Funds-and-ETF.md) | [Next](FundAccountCreate.md)

# IMTReportAPI::FundCreate

Create a fund configuration object.
    
    
    IMTConFund*  IMTReportAPI::FundCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConFund](../../../../Configuration-Interfaces/Funds-and-ETF/IMTConFund.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConFund::Release](../../../../Configuration-Interfaces/Funds-and-ETF/IMTConFund/Release.md) method of this object.
