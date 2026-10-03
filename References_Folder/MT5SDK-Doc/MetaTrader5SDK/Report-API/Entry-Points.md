[🏠 Document Start](../README.md) / [Report API](README.md) / Entry Points

[Previous](Ready-made-Examples/Fast-Profit-Deals.md) | [Next](Entry-Points/MTReportAbout.md)

# Entry Points

Any DLL of a server reports module must implement two entry points (exported functions):

Entry point | Purpose  
---|---  
[MTReportAbout](Entry-Points/MTReportAbout.md) | The method that provides the initial information about the reports module.  
[MTReportCreate](Entry-Points/MTReportCreate.md) | The method called by the server to create an instance of an object of the reports module.
