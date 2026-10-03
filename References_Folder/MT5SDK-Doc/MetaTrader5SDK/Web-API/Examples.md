[🏠 Document Start](../README.md) / [Web API](README.md) / Examples

[Previous](Protocol-Extension.md) | [Next](Manager-Interface-(Rest-API).md)

# Examples

To help you in understanding the operation of Web API via HTTPS, let use view some examples. The following operation scheme is implemented in these examples:

  * An MT5Request object is created, in which the Keep-Alive connection mechanism is implemented.
  * The Auth command for authentication on the server is called.
  * Then GET/POST request sending commands to a server are implemented.
  * The examples contain verification of SSL certificates used to connect to the platform. When using [untrusted certificates (#https)](Getting-Started.md#https), authorization error is activated. You can disable the verification by uncommenting out the corresponding code line (see the comments).



## JavaScript

For the example to work, install [Node JS](https://nodejs.org/).
    
    
    const https = require("https");
    const crypto = require('crypto');
    const buffer = require('buffer');
     
    function MT5Request(server, port) {
      this.server = server;
      this.port = port;
      this.https = new https.Agent();
      this.https.maxSockets = 1; // only one connection is used
    }
     
    MT5Request.prototype.Get = function (path, callback) {
      var options = {
        hostname: this.server,
        port: this.port,
        path: path,
        agent: this.https,
        headers: { "Connection": "keep-alive" },    
     // rejectUnauthorized: false, // uncomment this line if you use self-signed certificates
      };
      var req = https.get(options, function (res) {
        res.setEncoding('utf8');
        var body = "";
        res.on('data', function (chunk) {
          body += chunk;
        });
        res.on('end', function () {
          callback(null, res, body);
        });
      });
      req.on('error', function (e) {
        console.log(e);
        return callback(e);
      });
    };
     
    MT5Request.prototype.Post = function (path, body, callback) {
      var options = {
        hostname: this.server,
        port: this.port,
        path: path,
        agent: this.https,
        method: "POST",
        headers: {
          "Connection": "keep-alive",
          "Content-Type": "application/x-www-form-urlencoded",
          "Content-Length": Buffer.byteLength(body),
        },
        rejectUnauthorized: false, // comment out this line if you use self-signed certificates
      };
      var req = https.request(options, function (res) {
        res.setEncoding('utf8');
        var body = "";
        res.on('data', function (chunk) {
          body += chunk;
        });
        res.on('end', function () {
          callback(null, res, body);
        });
      });
      req.on('error', function (e) {
        console.log(e);
        return callback(e);
      });
      req.write(body);
      req.end();
    };
     
     
    MT5Request.prototype.ParseBodyJSON = function (error, res, body, callback) {
      if (error) {
        callback && callback(error);
        return (null);
      }
      if (res.statusCode != 200) {
        callback && callback(res.statusCode);
        return (null);
      }
      var answer = null;
      try {
        answer = JSON.parse(body);
      }
      catch {
        console.log("Parse JSON error");
      }
      if (!answer) {
        callback && callback("invalid body answer");
        return (null);
      }
      var retcode = parseInt(answer.retcode);
      if (retcode != 0) {
        callback && callback(answer.retcode);
        return (null);
      }
      return (answer);
    }
     
    MT5Request.prototype.ProcessAuth = function (answer, password) {
      //---
      var pass_md5 = crypto.createHash('md5');
      var buf = buffer.transcode(Buffer.from(password, 'utf8'), 'utf8', 'utf16le');
      pass_md5.update(buf, 'binary');
      var pass_md5_digest = pass_md5.digest('binary');
      //---
      var md5 = crypto.createHash('md5');
      md5.update(pass_md5_digest, 'binary');
      md5.update('WebAPI', 'ascii');
      var md5_digest = md5.digest('binary');
      //---
      var answer_md5 = crypto.createHash('md5');
      answer_md5.update(md5_digest, 'binary');
      var buf = Buffer.from(answer.srv_rand, 'hex');
      answer_md5.update(buf, 'binary');
      //---
      return (answer_md5.digest('hex'));
    }
     
    MT5Request.prototype.ProcessAuthFinal = function (answer, password, cli_random) {
      //---
      var pass_md5 = crypto.createHash('md5');
      var buf = buffer.transcode(Buffer.from(password, 'utf8'), 'utf8', 'utf16le');
      pass_md5.update(buf, 'binary');
      var pass_md5_digest = pass_md5.digest('binary');
      //---
      var md5 = crypto.createHash('md5');
      md5.update(pass_md5_digest, 'binary');
      md5.update('WebAPI', 'ascii');
      var md5_digest = md5.digest('binary');
      //---
      var answer_md5 = crypto.createHash('md5');
      answer_md5.update(md5_digest, 'binary');
      answer_md5.update(cli_random, 'binary');
      return (answer.cli_rand_answer == answer_md5.digest('hex'));
    }
     
    MT5Request.prototype.Auth = function (login, password, build, agent, callback) {
      if (!login || !password || !build || !agent)
        return;
      var self = this;
      self.Get("/api/auth/start?version=" + build + "&agent=" + agent + "&login=" + login + "&type=manager", function (error, res, body) {
        var answer = self.ParseBodyJSON(error, res, body, callback);
        if (answer) {
          var srv_rand_answer = self.ProcessAuth(answer, password);
          var cli_random_buf = crypto.randomBytes(16);
          cli_random_buf_hex = cli_random_buf.toString('hex');
          self.Get("/api/auth/answer?srv_rand_answer=" + srv_rand_answer + "&cli_rand=" + cli_random_buf_hex, function (error, res, body) {
            var answer = self.ParseBodyJSON(error, res, body, callback);
            if (answer) {
              if (self.ProcessAuthFinal(answer, password, cli_random_buf))
                callback && callback(null);
              else
                callback && callback("invalid final auth answer");
            }
          });
        }
      });
      return (true);
    };
     
    // Example of use
    var req = new MT5Request("my.broker.com", 443);
    // Authenticate on the server using the Auth command
    req.Auth(1000, "Password", 1985, "WebManager", function (error) {
      if (error) {
        console.log(error);
        return;
      }
      // Let us request the symbol named TEST using the symbol_get command
      req.Get("/api/symbol/get?symbol=TEST", function (error, res, body) {
        if (error) {
          console.log(error);
          return;
        }
        var answer = req.ParseBodyJSON(error, res, body, null);
        var symbol = answer.answer;
        console.log(symbol);
        // Changing the description
        symbol.Description = 'My Description';
        // Sending changes to the server using the symbol_add command
        req.Post('/api/symbol/add', JSON.stringify(symbol), function (error, res, body) {
          if (error) {
            console.log(error);
            return;
          }
          var answer = req.ParseBodyJSON(error, res, body, null);
          var symbol = answer.answer;
          console.log(symbol);
        });
      });
    });

## PHP

The "Curl" extension is used for this example. Enable it for the example to work.
    
    
    <?php
     
    class CMT5Request
    {
      private $m_curl=null;
      private $m_server="";
     
      public function Init($server)
      {
        $this->Shutdown();
        if($server==null)
          return(false);
        $this->m_curl=curl_init();
        if($this->m_curl==null)
          return(false);
        //---
        curl_setopt($this->m_curl,CURLOPT_SSL_VERIFYPEER,0); // comment out this line if you use self-signed certificates
        curl_setopt($this->m_curl,CURLOPT_MAXCONNECTS,1); // one connection is used
        curl_setopt($this->m_curl, CURLOPT_HTTPHEADER,array('Connection: Keep-Alive'));
        //---
        $this->m_server=$server;
        //---
        return(true);
      }
     
      public function Shutdown()
      {
        if($this->m_curl!=null)
            curl_close($this->m_curl);
        $this->m_curl=null;
      }
     
      public function Get($path)
      {
        if($this->m_curl==null)
          return(false);
        curl_setopt($this->m_curl,CURLOPT_POST,false);
        curl_setopt($this->m_curl,CURLOPT_URL,'https://'.$this->m_server.$path);
        curl_setopt($this->m_curl,CURLOPT_RETURNTRANSFER,true);
        $result=curl_exec($this->m_curl);
        if($result==false)
        {
          echo 'Curl GET error: '.curl_error($this->m_curl);
          return(false);
        }
        $code=curl_getinfo($this->m_curl,CURLINFO_HTTP_CODE);
        if($code!=200)
        {
          echo 'Curl GET code: '.$code;
          return(false);
        }
        return($result);
      }
     
      public function Post($path, $body)
      {
        if($this->m_curl==null)
          return(false);
        curl_setopt($this->m_curl,CURLOPT_POST,true);
        curl_setopt($this->m_curl,CURLOPT_URL, 'https://'.$this->m_server.$path);
        curl_setopt($this->m_curl,CURLOPT_POSTFIELDS,$body);
        curl_setopt($this->m_curl,CURLOPT_RETURNTRANSFER,true);
        $result=curl_exec($this->m_curl);
        if($result==false)
        {
          echo 'Curl POST error: '.curl_error($this->m_curl);
          return(false);
        }
        $code=curl_getinfo($this->m_curl,CURLINFO_HTTP_CODE);
        if($code!=200)
        {
          echo 'Curl POST code: '.$code;
          return(false);
        }
        return($result);
      }  
     
      public function Auth($login, $password, $build, $agent)
      {
        if($this->m_curl==null)
          return(false);    
        //--- send start
        $path='/api/auth/start?version='.$build.'&agent='.$agent.'&login='.$login.'&type=manager';
        $result=$this->Get($path);
        if($result==false)
          return(false);
        $auth_start_answer=json_decode($result);
        if((int)$auth_start_answer->retcode!=0)
        {
          echo 'Auth start error : '.$auth_start_answer.retcode;
          return(false);
        }
        //--- Getting code from the hex string
        $srv_rand=hex2bin($auth_start_answer->srv_rand);
        //--- Hash for the response
        $password_hash=md5(mb_convert_encoding($password,'utf-16le','utf-8'),true).'WebAPI';
        $srv_rand_answer=md5(md5($password_hash,true).$srv_rand);
        //--- Random string for the MetaTrader 5 server
        $cli_rand_buf=random_bytes(16);
        $cli_rand=bin2hex($cli_rand_buf);
        //--- Sending the response
        $path='/api/auth/answer?srv_rand_answer='.$srv_rand_answer.'&cli_rand='.$cli_rand;
        $result=$this->Get($path);
        if($result==false)
          return(false);
        $auth_answer_answer=json_decode($result);
        if((int)$auth_answer_answer->retcode!=0)
        {
          echo 'Auth answer error : '.$auth_answer_answer.retcode;
          return(false);
        }
        //--- Calculating a correct server response for the random client sequence
        $cli_rand_answer=md5(md5($password_hash,true).$cli_rand_buf);
        if($cli_rand_answer!=$auth_answer_answer->cli_rand_answer)
        {
          echo 'Auth answer error : invalid client answer';
          return(false);
        }
        //--- Everything is done
        return(true);
      }
    }
     
    // Example of use
    $request = new CMT5Request();
    // Authenticate on the server using the Auth command
    if($request->Init('my.broker.com:443') && $request->Auth(1000,"Password",1985,"WebManager"))
    {
      // Let us request the symbol named TEST using the symbol_get command
      $result=$request->Get('/api/symbol/get?symbol=TEST');
      if($result!=false)
      {
        echo $result;
        $json=json_decode($result);
        if((int)$json->retcode==0)
        {
          $symbol=$json->answer;
          //--- Changing the description
          $symbol->Description='My Description';
          // Sending changes to the server using the symbol_add command
          $result=$request->Post('/api/symbol/add',json_encode($symbol));
          if($result!=false)
            echo $result;
        }
      }
    }
    $request->Shutdown();
    ?>

## Java

Note that in Java the byte type is signed
    
    
    public class Connector {
       private final String USER__AGENT = "Mozilla/5.0";
       private final String HTTPS       = "https://";
       private       String m_server;
       //+--------------------------------------------------------------+
       //| Disable SSL when using untrusted certificates                |
       //+--------------------------------------------------------------+
       private static void disableSslVerification() {
          try {
             //---
             TrustManager[] trustAllCerts = new TrustManager[] {
                new X509TrustManager() {
                   public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                      return null;
                   }
                   //---
                   public void checkClientTrusted(X509Certificate[] certs, String authType) {
                   }
                   //---
                   public void checkServerTrusted(X509Certificate[] certs, String authType) {
                   }
                }
             };
             //---
             SSLContext sc = SSLContext.getInstance("SSL");
             sc.init(null, trustAllCerts, new java.security.SecureRandom());
             HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());
             //---
             HostnameVerifier allHostsValid = new HostnameVerifier() {
                public boolean verify(String hostname, SSLSession session) {
                   return true;
                }
             };
             //---
             HttpsURLConnection.setDefaultHostnameVerifier(allHostsValid);
          } catch(NoSuchAlgorithmException e) {
             e.printStackTrace();
          } catch(KeyManagementException e) {
             e.printStackTrace();
          }
       }
       //+--------------------------------------------------------------+
       //| Initialize connection                                        |
       //+--------------------------------------------------------------+
       public boolean initConnection(String server) {
          disableSslVerification();
          m_server = HTTPS + server;
          return(true);
       }
       //+--------------------------------------------------------------+
       //| Authentication                                               |
       //+--------------------------------------------------------------+
       public boolean sendAuth(String login, String password, String build, String agent) {
          String response="";
          if(m_server.isEmpty()) {
             System.out.println("call initConnection with correct server first");
             return(false);
          }
          //---
          String path = "/api/auth/start?version=" + build + "&agent=" + agent + "&login=" + login + "&type=manager";
          //---
          try {
             System.out.println("sendAuth - send Http GET request");
             response=sendGet(path);
          } catch(Exception ex) {
             System.out.println(ex.toString());
          }
          //---
          if(!response.isEmpty()) {
             JSONObject json_obj = new JSONObject(response);
             String retcode = json_obj.getString("retcode");
             System.out.println(retcode);
             if(retcode.equals("0 Done")) {
                String srv_rand = json_obj.getString("srv_rand");
                byte[] byte_array = DatatypeConverter.parseHexBinary(srv_rand);
                printByteResult(byte_array);
                //---
                byte[] cli_rand_buf = GetRandomHex();
                printByteResult(cli_rand_buf);
                //---
                String cli_rand_string = DatatypeConverter.printHexBinary(cli_rand_buf);
                //---
                String srv_rand_answer = GetHashFromPassword(password, byte_array);
                //---
                String auth_response="/api/auth/answer?srv_rand_answer=" + srv_rand_answer + "&cli_rand=" + cli_rand_string;
                try {
                   System.out.println("sendAuth - send Http GET request");
                   sendGet(auth_response);
                } catch(Exception ex) {
                   System.out.println(ex.toString());
                }
             }
             return(true);
          } else {
             return(false);
          }
       }
       //+--------------------------------------------------------------+
       //| Send GET request                                             |
       //+--------------------------------------------------------------+
       public String sendGet(String path) throws Exception {
          String url = m_server + path;
          //---
          URL obj = new URL(url);
          HttpURLConnection con = (HttpURLConnection) obj.openConnection();
          //---
          con.setRequestMethod("GET");
          //---
          con.setRequestProperty("User-Agent", USER__AGENT);
          //---
          int responseCode = con.getResponseCode();
          //---
          System.out.println("\nSending 'GET' request to URL : " + url);
          System.out.println("Response Code : " + responseCode);
          //---
          BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
          String inputLine;
          StringBuffer response = new StringBuffer();
          //---
          while((inputLine = in.readLine()) != null) {
             response.append(inputLine);
          }
          in.close();
          //---
          System.out.println(response.toString());
          return(response.toString());
       }
       //+------------------------------------------------------------------+
       //| Get a random sequence                                            |
       //+------------------------------------------------------------------+
       private byte[] GetRandomHex() {
          byte[] base_byte = new byte[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
          //---
          SecureRandom random = new SecureRandom();
          random.nextBytes(base_byte);
          //---
          return base_byte;
       }
       //+------------------------------------------------------------------+
       //| Output the result                                                |
       //+------------------------------------------------------------------+
       private void printByteResult(byte[] array_to_print) {
          if(array_to_print!=null) {
             StringBuilder sb_unsigned_bytes = new StringBuilder();
             for(byte b : array_to_print)
                sb_unsigned_bytes.append((b & 0xff));
             System.out.println("result array =" + sb_unsigned_bytes.toString());
          } else {
             System.out.println("array_to_print is null");
          }
       }
       //+------------------------------------------------------------------+
       //| Get the result in HEX format                                     |
       //+------------------------------------------------------------------+
       private String getHEXResult(byte[] array_to_print) {
          if(array_to_print!=null) {
             StringBuilder sb = new StringBuilder();
             for(byte b : array_to_print)
                sb.append(String.format("%02X", b));
             return(sb.toString());
          } else {
             System.out.println("array_to_print is null");
             return null;
          }
       }
       //+------------------------------------------------------------------+
       //| Get a password hash                                              |
       //+------------------------------------------------------------------+
       private String GetHashFromPassword(String password, byte[] randCode) {
          if(password.isEmpty()||randCode==null)
             return null;
          //---
          try {
             MessageDigest md = MessageDigest.getInstance("MD5");
             byte[] password_bytes_unicode = md.digest(password.getBytes(StandardCharsets.UTF_16LE));
             //---
             printByteResult(password_bytes_unicode);
             //---
             String api_word_str = "WebAPI";
             byte[] apiWord = api_word_str.getBytes(StandardCharsets.UTF_8);
             System.out.println("WebAPI byte array =" + Arrays.toString(apiWord));
             //---
             byte[] hashContains = CopyBuffer(password_bytes_unicode, apiWord);
             //---
             printByteResult(hashContains);
             //---
             byte[] final_hash = md.digest(hashContains);
             printByteResult(final_hash);
             //---
             byte[] final_hash_plus_rand = CopyBuffer(final_hash, randCode);
             byte[] final_hash_plus_rand_md5 = md.digest(final_hash_plus_rand);
             //---
             return getHEXResult(final_hash_plus_rand_md5);
          } catch(Exception ex) {
             System.out.println(ex.toString());
             return null;
          }
       }
       //+------------------------------------------------------------------+
       //| Copy the buffer                                                  |
       //+------------------------------------------------------------------+
       public static byte[] CopyBuffer(byte[] ar1, byte[] ar2) {
          byte[] result = new byte[ar1.length + ar2.length];
          //---
          try {
             System.arraycopy(ar1, 0, result, 0, ar1.length);
             System.arraycopy(ar2, 0, result, ar1.length, ar2.length);
          } catch(Exception ex) {
             System.out.println(ex.toString());
             return null;
          }
          //---
          return result;
       }
    }
    //+------------------------------------------------------------------+

Usage:
    
    
    //+------------------------------------------------------------------+
    //| Call authentication function                                     |
    //+------------------------------------------------------------------+
    public static void main(String[] args) {
       Connector rest_client = new Connector();
       rest_client.initConnection("192.168.1.104:1990");
       if(rest_client.sendAuth("1002","Password1","2190","WebManager"))
          System.out.println("auth success");
       else
          System.out.println("auth failed");
    }
