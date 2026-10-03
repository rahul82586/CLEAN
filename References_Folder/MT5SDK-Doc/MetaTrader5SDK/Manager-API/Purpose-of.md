[🏠 Document Start](../README.md) / [Manager API](README.md) / Purpose of

[Previous](README.md) | [Next](Recommendations-for-Developers.md)

# Purpose of Manager API

The MetaTrader 5 Manager API consists of two main interfaces — IMTManagerAPI and IMTAdminAPI, which provide access to the commands of the manager and administrator terminals respectively. Applications developed using the Manager API allow to extend the existing functionality, as well as to adapt it to suit your needs:

  * Calling the internal server data  
Reading various configurations, databases, information about the current state of clients, etc. This feature allows making all sorts of reports about the current state of the platform.
  * Management of internal data on a server  
Changing the settings, databases, creation of information in the databases (emails, news, etc.).
  * Receiving notifications of events  
Whenever you change a database or configurations, the application can receive the appropriate notifications and respond to them.
  * Performing dealing activities  
The application can connect to a server's queue of trade requests and process them in accordance with a specified algorithm.
  * Running custom commands  
MetaTrader 5 Manager API provides the possibility of extending the protocol for running custom commands on the server.


