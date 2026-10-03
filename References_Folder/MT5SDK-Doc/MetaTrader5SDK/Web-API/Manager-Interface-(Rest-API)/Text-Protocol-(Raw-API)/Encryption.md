[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Text Protocol (Raw API)](../Text-Protocol-(Raw-API).md) / Encryption

[Previous](Authentication.md) | [Next](../Outdated-version-of-Rest-API.md)

<a id="encryption"></a>
# Encryption (#encryption)

When connected to the platform using the Web API, a client can choose whether to encrypt the transmitted data stream or not.

  * It is strongly recommended to [enable encryption (#client-start)](Authentication.md#client-start) in order to prevent unauthorized access to information. The option of disabling encryption is provided only for the purpose of simplifying the process of application debugging.
  * The encryption of transmitted data can be started only after completing the [authentication](Authentication.md) procedure, since the Web client obtains a required encryption sequence as soon as it is completed.

  
---  
  
The Web API uses AES encryption with the 256-bit key in the OFB (Output Feedback) mode. The main stages of encryption:

  * [Receiving an Encryption Sequence (#sequence)](Encryption.md#sequence)
  * [AES256 Initialization (#initialization)](Encryption.md#initialization)
  * [Encryption of Outgoing Packets (#encryption-out)](Encryption.md#encryption-out)
  * [Decryption of Incoming Packets (#encryption-in)](Encryption.md#encryption-in)



<a id="sequence"></a>
## Receiving an Encryption Sequence (#sequence)

At the end of [authentication (#server-answer)](Authentication.md#server-answer) a trade server sends a random sequence, which should be used to form a final encryption sequence:
    
    
    OUT=MD5(MD5('Password')+'WebAPI')
    for(i=0;i<16;i++)
      {
       OUT=MD5(CRYPT_RAND[i]+OUT);
       CRYPT_IV[i]=OUT;
      }

where:

  * OUT — the value of the previous calculated CRYPT_IV block; initially equal to the [password hash (#hash)](Authentication.md#hash) (16-byte block).
  * CRYPT_RAND — [a random sequence of the server (#server-answer)](Authentication.md#server-answer), consisting of 16 blocks 16 bytes each.
  * CRYPT_IV — an encryption sequence, sized 16 16-byte blocks.



An Example of Receiving an Encryption Sequence
    
    
    //--- Password hash (used for the first iteration, when the first 16 bytes of CRYPT_IV are formed):
    MD5(MD5('Password')+'WebAPI')=904ba8ecb16273d2f0ae9c3b8a023752
    //--- A random sequence received from the server (16 16-byte blocks):
    CRYPT_RAND=
    000102030405060708090a0b0c0d0e0f
    101112131415161718191a1b1c1d1e1f
    202122232425262728292a2b2c2d2e2f
    303132333435363738393a3b3c3d3e3f
    ...
    f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff
    //--- An encryption sequence (16 16-byte blocks), based on which AES initialization will be performed:
    CRYPT_IV:
    MD5(000102030405060708090a0b0c0d0e0f+904ba8ecb16273d2f0ae9c3b8a023752)=b0ed3aa00c46c12260202166f8484536
    MD5(101112131415161718191a1b1c1d1e1f+b0ed3aa00c46c12260202166f8484536)=8f57767e6a2ca7a54c85776325f7677e
    MD5(202122232425262728292a2b2c2d2e2f+8f57767e6a2ca7a54c85776325f7677e)=1b6493c551ce24e2746982f0a15dc916
    MD5(303132333435363738393a3b3c3d3e3f+1b6493c551ce24e2746982f0a15dc916)=57c68578ca6d4196107f83e6a8f4b48f
    ...
    MD5(f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff+ef863280e56de9f5898de0496d3db4bb)=70c65d37748166f082270af669327005

<a id="initialization"></a>
## AES256 Initialization (#initialization)

A formed encryption sequence is divided into three parts:

  * A key for the AES256 encryption — first 32 bytes of CRYPT_IV.
  * The initial encryption vector (IV_Out) for outgoing data — 16 bytes after the encryption key in CRYPT_IV.
  * The initial decryption vector (IV_In) for incoming data — 16 bytes after the initial vector for outgoing data in CRYPT_IV.



The remaining part of CRYPT_IV is not used in this implementation of the encryption algorithm.

An example of how a key and encryption vectors are formed from the encryption sequence received above:
    
    
    //---AES key:
    b0ed3aa00c46c12260202166f84845368f57767e6a2ca7a54c85776325f7677e
    //---Initial encryption vector:
    1b6493c551ce24e2746982f0a15dc916
    //---Initial decryption vector
    57c68578ca6d4196107f83e6a8f4b48f

<a id="encryption-out"></a>
## Encryption of Outgoing Packets (#encryption-out)

> Each packet is encrypted separately. Only the [body (#body)](Format-of-Packages.md#body) is encrypted in a packet.

The initial encryption vector IV_Out is used as an infinite encryption key generated based on the AES encryption.
    
    
    for(i=0,key=16;i<packet_body_size;i++)
        {
         //--- If there is no key
         if(key>=16)
           {
            //--- Form a new part of the stream key for incoming data
            aes_out=AESEncrypt(encryption_key,aes_out);
            //--- Reset the stream counter
            key=0;
           }
         //--- If there is a key, then encrypt
         packet_body[i]=packet_body[i]^aes_out[key++];
        }

Each byte of the packet is encrypted inside the "for" loop using the 16-byte aes_out key by the XOR method. Each byte of the packet has its separate byte of the aes_out key. After encrypting a byte, the "key" counter increases by one, and the beginning of the loop start again.

Initially, aes_out is equal to IV_Out (the initial encryption vector of outgoing data). As soon as a key's 16 bytes are completed, the generation of the key continuation using the "AESEncrypt" function starts. This is a standard function for encrypting one block in the AES. The key continuation is obtained using the 32-byte key for AES encryption received from the [encryption sequence (#initialization)](Encryption.md#initialization).

> The part of the key that was not used for encryption/decryption of the packet is discarded. For each packet a new key is generated.

<a id="encryption-in"></a>
## Decryption of Incoming Packets (#encryption-in)

Decryption of incoming packets is similar to encryption. But the IV_In value (the initial decryption vector of incoming data) is used as the initial value for the decryption key aes_in.
    
    
    for(i=0,key=16;i<packet_body_size;i++)
        {
         //--- If there is no key
         if(key>=16)
           {
            //--- Form a new part of the stream key for outgoing data
            aes_in=AESEncrypt(encryption_key,aes_in);
            //--- Reset the stream counter
            key=0;
           }
         //--- If there is a key, then encrypt
         packet_body[i]=packet_body[i]^aes_in[key++];
        }
