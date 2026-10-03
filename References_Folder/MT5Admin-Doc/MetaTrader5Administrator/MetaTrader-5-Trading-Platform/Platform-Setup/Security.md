[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../Platform-Setup.md) / Security

[Previous](Integrations/Web-Services.md) | [Next](Security/Certificates.md)

# Security

The trading platform provides a variety of features to ensure system security. This includes protection for server and client components.

  * The platform support certificate-based [extended authentication](Groups/Extended-Authentication-Setup.md). Usage of certificates provides a higher level of client and manager account security. [Set up certificates](Security/Certificates.md) to start using extended authentication.
  * By configuring [firewall](Security/Firewall.md), you can restrict access to the platform from specific IP addresses. For example, you can block addresses from which attacks were registered, or add your office address to the white list so that they are not blocked by anti-flood control.
  * Furthermore, the platform provides a specialized component [Anti DDoS Proxy Server](Security/Anti-DDoS-Protection.md). It protects from DDoS attack by using external protection providers. Unwanted connections are blocked on the distributed network of an external provider's servers rather than on your access servers.
  * Components interact through secure protocols, databases are securely encrypted, while user actions are registered in logs. This information, along with other operation security details, is available under the "[Authentication Protocols](Security/Authentication-Protocols.md)" section.



Please treat settings in this section carefully, as they affect the continuity of your business processes.
