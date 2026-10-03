[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Integrations](../Integrations.md) / Web Services

[Previous](Event-Streaming/Kafka-Streaming-Setup.md) | [Next](../Security.md)

<a id="web-service"></a>
# Web Services (#web-service)

The trading platform offers extensive opportunities for integration with brokerage websites and web services, as well as for integration with additional service providers. This functionality is implemented via the [MetaTrader 5 Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi). By using integrations, you can create trader rooms on your website, to which data on trading operations will be sent from the platform, as well as implement registration, account top-up and other options.

> The [App Store](https://support.metaquotes.net/en/market/mt5/integration) features a plethora of ready-made web integration solutions from professional developers.

<a id="ssl"></a>
## SSL Certificates (#ssl)

Support for connection over HTTPS is implemented on access servers (HTTP is not connected). Therefore, they can act as a web server. This allows sending to a server [Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi_https) commands as usual GET and POST requests.

To enable connection to the access server via HTTPS, at least one of its [public addresses (#public)](../Network-cluster/Configuring-Servers.md#public) must be associated with a certain domain, i.e. the host to which POST and GET requests will be implemented. For this purpose, the appropriate entry must be specified on the DNS server. For example, if you want to implement operation via the host abc.broker.com, the following entry should be added to DNS

abc.broker.com 3600 IN A XXX.XXX.XXX.XXX   
abc.broker.com 3600 IN AAAA XXXX:XXXX:X:XX:XX  
---  
  
Here XXX is the public IPv4 or IPv6 address of the Access server.

Since only protected TLS connections (HTTPS) are supported, an SSL certificate must be installed on the access server for the appropriate domain. Use the "Integration \ Web Services \ SSL Certificates" section to upload and manage certificates:

![Configuring SSL certificates for connecting to an access server via HTTPS](images/network_add_ssl.png)

There are three ways to upload a certificate to the platform:

  * Using a pre-made pfx file
  * By generating a self-signed certificate (can only be used for testing)
  * By generating a certificate via the [Let's Encrypt](https://letsencrypt.org/) service



The type of the certificate used is shown in a tooltip when you hover over its line.

SSL settings apply to all access servers. Changes in the list of certificates are applied instantly, so you do not need to restart the servers.

Connections from multiple domains can be supported on one server ([the SNI mode](https://en.wikipedia.org/wiki/Server_Name_Indication)). In this case, the corresponding SSL certificate must be installed for each of them. When connecting, the client specifies the address to connect to. The access server checks all installed certificates and automatically provides the necessary one to the client:

  * First, the server tries to find a certificate for an exact match domain.
  * If not, it tries to find the most suitable one using mask "*".
  * If the certificate could not be found, the server returns the first certificate from the list.



After making changes to the list of certificates, click "Apply" on the toolbar.

One month before the certificate expiration date, its line is highlighted in red. The appropriate warning is displayed on the platform [start page](../Start-Page.md) as well.

<a id="pfx"></a>
### Adding a certificate from a PFX file (#pfx)

Click PFX and specify the path to the file. The certificate can be password protected. In this case, you will be prompted to enter the password.

<a id="selfsigned"></a>
### Adding a self-signed certificate (#selfsigned)

The trading platform allows the issuing of self-signed SSL certificates. Such certificates can be used to test applications written using the [MetaTrader 5 Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi). Unlike a certificate issued by a trusted authority, a self-signed certificate can be obtained instantly and free of charge. However, it cannot be used for operations in a real environment since the connection will not be trusted — for this reason, browsers and apps will return warnings.

Click "Add \ Self-signed" and specify the domain, your company name, certificate expiration date, and encryption algorithm:

  * Elliptic Curve Cryptography (ECC) with a 256 or 384 bit key.
  * RSA with a 2048 or 4096 bit key



![Issuing a self-signed certificate](images/self_signed_certificate.png)

The generated certificate will be added to the platform. A self-signed certificate must be associated with at least one public address of any of your Access servers using a DNS record. For further details please read the [SSL certificates (#ssl)](Web-Services.md#ssl) section.

Self-signed certificates are not automatically renewed. Upon expiration, you need to generate and upload a new certificate.

<a id="letsencrypt"></a>
### Adding a Let's Encrypt certificate (#letsencrypt)

[Let's Encrypt](https://letsencrypt.org/) is a certificate authority which enables free automatic issuing of SSL certificates. You can obtain a ready-made certificate from this service right in the platform. Let's Encrypt certificates are trusted by most browsers and operating systems. Accordingly, a non-trusted domain warning will not be displayed for your clients upon connection.

How the certificate is issued

  1. The platform makes the first request to Let's Encrypt and receives the initial data for issuing a certificate.
  2. The platform (its main trading server) generates keys for the new certificate. The private key is not transfered to Let's Encrypt, to Access servers or to anywhere else.
  3. For security purposes, Let's Encrypt verifies that the certificate is issued by the real domain owner. The service uses several confirmation methods to verify that: <https://letsencrypt.org/docs/challenge-types/>. MetaTrader 5 uses the TLS-ALPN-01 option:
     1. A domain validation certificate is generated on the platform side and is distributed to all Access servers.
     2. Using a separate SSL protocol, Let's Encrypt connects to port 443 on all IP addresses specified in the DNS for the domain name. Having connected, the service receives and checks the certificate which contains the verifiable data. It is very important that all IP addresses associated with the domain, point to the Access servers in your cluster. All Access servers must be operational and available for verification. They must be configured to listen and accept connections to port 443.
  4. The platform waits for Let's Encrypt to complete the verification. After successful verification, the platform receives the issued certificate. The certificate is installed in the platform



Preparing to receive the certificate

To issue a certificate, Let's Encrypt checks the IP addresses specified for your domain. Therefore, before proceeding with the certificate issuing, correctly configure the DNS server as described in the [SSL Certificates (#ssl)](Web-Services.md#ssl) section. All addresses must point exactly to the Access servers of your cluster.

Also please note that after you add a DNS record, it takes some time for them to propagate across the Internet. You can check which IP address a domain is pointing to using the "nslookup" command. For example:

nslookup abc.broker.com  
---  
  
Make sure that the domain is associated with the correct address and proceed to add the certificate in the platform. Click "Add \ Let's Encrypt" and specify the domain, your company name, and the encryption algorithm:

  * Elliptic Curve Cryptography (ECC) with a 256 or 384 bit key.
  * RSA with a 2048 or 4096 bit key



Also make sure that the option "Issue a free and automatically renewable Let's Encrypt certificate" is enabled.

Domain name requirements:

  * The name must contain only ANSI letters and numbers, dots and dashes
  * Dots and dashes are allowed everywhere except at the line beginning and end
  * The name must not be an IP address



![Issuing a certificate via Let's Encrypt](images/lets_encrypt_certificate.png)

The generated certificate will be added to the platform.

The Let's Encrypt certificate is valid for 90 days, but the platform will automatically renew it. A week before the certificate expires, the platform will send a request to the server and then will receive and install a new certificate.

  * Let's Encrypt has limits on the frequency and number of issued certificates. If the certificate generation fails, find out and fix the cause rather than trying again and again. Otherwise, the service may restrict your access.


  * Let's Encrypt does not support the [Cloudflare service](../Security/Anti-DDoS-Protection.md). If you are using cloud protection for your access servers, Let's Encrypt will not be able to connect to them for domain verification.

  
---  
  
<a id="web-service"></a>
## Web Services (#web-service)

The platform allows the receiving and sending of [callback requests](https://en.wikipedia.org/wiki/Callback_(computer_programming)) from external services. They are used to notify the system about various external events.

For example, SMS providers CM.com and Vonage which are available for [integration](SMS-Gateways.md), can send notifications about message delivery statuses. The services need to know the address to which the messages should be sent. Such addresses are referred to as endpoints. Endpoints can be configured via the Web Services section.

Callback requests are received and processed by access servers. The access servers actually act as a web server. First, you should set a domain name for them. External services will access the platform at this address. Also, endpoint addresses for callback requests will be formed relative to this address. You should create a DNS record for the specified domain (bind the domain with a public IP address of the access server), as well as load the certificate to the platform, as described in the [SSL Certificates (#ssl)](Web-Services.md#ssl) section.

![Configuring endpoints for callback requests from web services](images/web_services.png)

<a id="request-urls"></a>
### Request URLs (#request-urls)

To maintain a transparent structure and to ensure further extensibility, all callback endpoints are named as follows: [domain name]/api/callback/[integration section]/[unique part for a specific service]. For example:

  * Endpoints for [messenger](Messengers.md) and [SMS gateway](SMS-Gateways.md) integrations will start with [domain name]/api/callback/messenger/.


  * All endpoints for [payment system](../Payments.md) integrations will start with the path [domain name]/api/callback/payments/.


  * To run [automation (#webcallback)](../Automations/Triggers.md#webcallback) tasks through external services, all endpoints will start from the path [domain name]/api/callback/automation/.



The platform only accepts requests with the specified URLs. The platform will nor process any other requests out of this list. This is necessary to ensure safety.

<a id="authorization-for-requests"></a>
### Authorization for requests (#authorization-for-requests)

As an additional security measure, authorization through [a manager account](../Managers.md) can be enabled for each request. To do this, specify the relevant account login in the Manager field. Requests with additional authentication should have the following information in their header:

Authorization: BASIC BASE64_LOGIN_PASSWORD  
---  
  
where BASE64_LOGIN_PASSWORD is a sting in the BASE64 format with the login and password of the manager account specified as <login>:<password>. For example:

1000:Password  
---  
  
This string in the BASE64 format is shown below:

MTAwMDpQYXNzd29yZA==  
---  
  
Accordingly, in the request header should be as follows

Authorization: BASIC MTAwMDpQYXNzd29yZA==  
---  
  
If you leave the Manager field empty, the request will operate as before, without the additional authorization. The server will only check the list of allowed URLs and IP addresses.

<a id="list-of-allowed-ip-addresses-for-requests"></a>
### List of allowed IP addresses for requests (#list-of-allowed-ip-addresses-for-requests)

Set the IP addresses from which access servers will receive callback requests to specific endpoints. This is needed for added security. The default list contains only one entry "* — 127.0.0.1". It allows requests to be received on any endpoints from the local machine.

Addresses can be specified in the following forms:

  * A comma separated list: 10.12.192.1, 10.12.192.6
  * A range: 10.12.192.1-10.12.192.110
  * Using a netmask: 192.168.0.0/16 or 2a00::0/16



The formats can be combined. For example: 10.12.192.1-10.12.192.110, 192.168.0.1

> The list of allowed addresses is valid for all access servers.
