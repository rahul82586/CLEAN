[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Security](../Security.md) / Certificates

[Previous](../Security.md) | [Next](Firewall.md)

<a id="certificates"></a>
# Certificates (#certificates)

Security certificates are used for advanced authentication in the trading platform. This authentication type allows improving the system operation security. For more details please read a [separate section](../Groups/Extended-Authentication-Setup.md).

Here you can configure certificates.

![Certificates](images/certificates.png)

Specify how certificates will be generated:

  * on the basis of license — by default, client certificates are generated on the basis of a license issued by MetaQuotes Software Corp. when you purchase the platform. The license file contains a unique certificate created for the brokerage company, based on which all client certificates are generated.
  * on the basis of certificate — a brokerage company can use its own certificate to generated client certificates. Upon the selection of this option a window for selecting of a pfx certificate opens. The certificate file must contain a private key. The certification issuer must be added to the [trusted (#trusted)](Certificates.md#trusted) list.
  * disabled — this option disables the generation of certificates. However, this does not mean that the [extended authentication (#authorization)](../Groups/Group-Settings.md#authorization) will become unavailable. In this case, the client will not be able to receive a certificate automatically when connecting to the account. The brokerage company will need to issue a certificate to the user specifically (for example, on an e-token), and then link the certificate to an account in the trading platform. To link a certificate, import it via the [Security (#security)](../Accounts/Editing-Account.md#security) tab of this account.



<a id="certificate-requirements"></a>
## Certificate Requirements (#certificate-requirements)

The following requirements must be fulfilled when using the company's own certificates:

  * The certification authority that issued the certificate must be added to the [trusted (#trusted)](Certificates.md#trusted) list.
  * A certificate issued to a client must contain a private key.
  * The client must add the issued certificate to the /certificates folder of the terminal, install it to the operating system storage or upload it to an e-token.



<a id="trusted"></a>
## Trusted Authorities (#trusted)

When authorizing on the server with a certificate, the certification authority is checked. Authorization is allowed only using certificates issued by trusted authorities. By default, such an authority is a certificate from the trading platform license that is used to generate client certificates.

To add a certification authority, click the appropriate button and specify the *.cer or *.crt file. If necessary, any of the previously added centers can be disconnected at any time.
