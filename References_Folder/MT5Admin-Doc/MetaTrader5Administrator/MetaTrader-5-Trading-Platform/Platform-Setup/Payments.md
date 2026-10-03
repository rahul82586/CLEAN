[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../Platform-Setup.md) / Payments

[Previous](Accounts/Links-to-Depositing-and-Withdrawing.md) | [Next](Payments/Payment-Gateways.md)

# Integrated Payment Processing System

MetaTrader 5 features a built-in payment receiving and sending system. Your clients do not have to leave the platform in order to deposit or withdraw funds. The relevant operations can be performed straight through the trading terminal. The platform is integrated with various payment providers and thus your traders can access all the necessary deposit/withdrawal methods, including bank cards, popular wallets, and bank transfers. All transactions are securely encrypted and are completely safe.

Payment system integration with the platform ensures that you always work with a single database. All transactions are linked to accounts and client records. For example, by opening client data, you can easily see all payments along with transaction amounts, dates, cards, etc. You won't need complex and expensive integrations with payment systems and third-party CRMs.

![Integrated Payment Processing System](images/payments.png)

The benefits of built-in services for your company:

  * Streamlined onboarding. Since the need for additional registration on your website is eliminated, users can download the trading platform, open an account, make a deposit, and start trading. This accelerates the account opening process for potential customers and enables a seamless transition to real trading for demo users.
  * Cost reduction. You don't need to invest in the development, configuration, and maintenance of infrastructure for customer registration, payment processing and transaction management. This might be especially relevant for start-up companies which possess limited resources.
  * Increased deposit volumes. The natively integrated payment option simplifies the deposit process. Thus, users can faster respond to market situations by adding funds to their accounts. This contributes to overall growth in user deposits.
  * Higher deposit frequency. With all the required features available within the trading environment, your traders can maintain trading focus and engagement for longer periods. By eliminating distractions and the need for additional authentications in third-party resources, you can increase decision-making speed and achieve higher deposit frequencies.



Configure integrated payments for your traders to eliminate extra costs, increase demo to real conversion rates, implement seamless onboarding procedures and boost deposits from existing clients.

## How it works

  * You set up integration with the payment system on the server side.
  * A [special section](Payments/in-Client-Terminals.md) for deposits and withdrawals will become available in client terminals.
  * Your client makes a payment via the terminal and the transaction is forwarded to your payment provider for processing. Depending on the rules configured on the server, the transaction may be additionally [confirmed by the manager](Payments/Processing.md).
  * If the transaction is successfully processed in the payment system, the corresponding balance operation is performed on the client's account in MetaTrader 5.
  * All deposit and withdrawal operations are stored in the platform database and are available in the [Active](Payments/Controlling.md) and [History](Payments/Controlling.md) sections. Transactions are linked to client records and trading accounts, so you can easily access all the necessary information whenever you need it.



## How to start the service

  * Select a payment provider. The platform currently supports Unlimit, ECOMMPAY, APS, AstroPay, EU Paymentz and Kora. If your preferred payment provider is not currently available in the service, please [reach out to us](../Technical-Support.md) for possible integration options. Contact the selected provider and sign their service agreement.
  * [Configure a wallet](Payments/Payment-Gateways.md) in the platform. After you sign the agreement with the payment provider, they will send you all the necessary data to set up service integration. Usually, the data includes a login, a password and a special access key. Connecting the provider in the platform will take 10-15 minutes.
  * [Set payment processing rules](Payments/Payment-Processing-Rules.md). The system enables flexible configuration of deposit and withdrawal processing rules depending on transaction parameters. For example, you may set all bank transfers to be processed manually and card payments up to 1000 USD to be confirmed automatically.


