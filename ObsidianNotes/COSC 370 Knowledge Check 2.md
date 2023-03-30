1) In the client server appoach we observe the following: There is a server that remainings constantly running, the HTTP (protocol) uses this structure, and the server's IP address is widely known.
2) In the peer-to-peer (or P2P) there exists no server thus we can say that there is not a server that is always on, we also know that the application (or process) may request information from others and will provide information when requested by others.
3) The UDP service is known as a best effort service. The service will try its best to deliver the data to the destiniation but can make no guarantees for any particular subset of the data.
4) On the otherhand, the TCP service  ensures that the sender does not send too much data as to overflow the buffers on the recieving end (flow control). TCP also controls senders so that they do not collectively send more data than the recieving links can support. Finally, TCP supports loss-free data transfer, ensuring all packets reach their destination.
5) When we say that HTTP is stateless we are refering to the fact that an HTTP server does not remember anything about previous interactions with this client.
6) Cookies are used by a server on an HTTP client's request. They store information about an earlier interaction between the server and a web browser.
7) An HTTP GET request is a message sent by a client to request an object from a web server to be sent to said client.
8) A conditional HTTP GET request will only send the requested object if said object has changed since the server last sent the object to the client.
9) Given GET /kurose_ross_sandbox/interactive/quotation2.htm `HTTP/1.1` we know the client is using HTTP version 1.1
10) Given Accept-Language: `en-us, en-gb`;q=0.1, en;q=0.7, fr, fr-ch, da, de, fi we know that the client would least prefer to get a reply in United Kingdom English as it follows US English in the list of accepted languages.
11) Given If-Modified-Since: Wed, 09 Sep 2020 16:06:01 -0700 we know the client has a cached version of the requested object as this is a conditional GET request.
12) Given HTTP/1.0 200 OK we can expect the server to close the connection following this message as HTTP version 1.0 is non persistent.
13) We use web caching as it uses less bandwidth entering at network if the client and cache are located on the same network. If the cache is on the same network as the client, then the response is generally faster.
14) HTTP 2.0 vs 1.1: 2 allows for the objects in a persistent connection to be send in a client specified order. 2 also supports breaking larger objects into smaller pieces and can be sent using priority scheduling, generally increasing performance by allowing smaller objects to not be blocked by larger ones.
15) An HTTP reply is composed of a reponse code and a reponse phrase associated with the code.
16) The if modified since field inciates to the server that the client has a cached version of the requested object along with the time it was last cached.
17) The purpose of a cookie value in an HTTP GET request doesn't mean anything in particular, it is simply a value that was returned during an earlier interaction between the client and the server.
18) ![[Pasted image 20230307111222.png]]
In the scenario depicted above there is a total of 3 RRTs from the client contacting the server to the client sending the email.
19) When comparing HTTP and SMTP we notice that HTTP uses a blank line (CRLF) to end a request header, it is mostly a pull protocol, and uses port 80 to communicate.
20) SMTP instead is a push protocol, uses CRLF.CRLF to indicate the end of the message, and uses port 25.
21) STMP also uses ASCII commands and status codes. It is able to use a persistent TCP connection to transfer multiple objects.
22) SMTP pushes email from a mail client to the a mail server. IMAP pulls email from a mail server to a mail client. Neither SMTP or IMAP pull from one mail server to another mail server.
23) The highest level of the DNS hierarchy is the DNS root servers and knows how to contact the TLD servers. Top Level Domain (TLD) server is responsible for a domain (example, *.com*, *.edu*) and knows how to contact authoritative name servers. Authoritative name servers are responsible for mapping an IP to a hostname. Local DNS servers reply to DNS queries by a localhost, contacting other DNS servers to repsond to the query.
24) DNS performs caching to reduce load elsewhere in the DNS, additionally, the caching results in faster replies.
25) DNS type A is a hostname and an IP address
26) Requests for time units t=30, t=0, t=1 all take 8 time units (Not cached anywhere).
27) Requests t=12 and t=5 take 6 time units (Cached in TLD DNS server).
28) Request t=10 takes 2 time units (Cached in local DNS server)
29) The local DNS server record for a remote host may be different that the record of the authoritative server for the same host.
30) A local DNS server can decrease the name-to-IP-address resolution time experienced by a querying localhost over the time needed to resolve the query via the DNS hierarchy.
31) What is the role of the authoritative name server? Provides the definitve answer to the query with repsect to a name in the authoritative name server's domain.

## Possible Questions:

1) In a streaming multimedia setting, a manifest file lets the client know where it can retrieve different video segments from, encoded at different rates.
2) CDNs (Content Delivery Networks) store and server multiple copies of videos across geographically distributed sites.
3) Definitions in video steaming: 
	- A chunk is a unit of video that may be encoded at different rates.
	- A manifest is a file containing the location and encoding rates of files that match video segments.
	- DASH is an approach that allows clients to adapt the encoding rate of a video to match congestion conditions.
	- A CDN uses a enter deep approach meaning content is stored close to the clients.
4) DASH or Dynamic Adaptive Streaming over HTTP approach divides video files into chunks that are encoded at various different rates. The client will play the video chunk-by-chunk, each chunk that is requested will have an encoding rate corresponding to the available bandwidth at the time of the request.
5) Characteristics of a UDP socket:
	- Can be created in Pyhton using socket(AF_INET, SOCK_DGRAM)
	- An application must explicitly specify the IP destination address and port number for each group of bytes written in a socket.
	- Allows for unreliable transfer of a datagram (group of bytes) from client to server.
6) Characteristics of a TCP socket:
	- Can be created in Python using the code socket(AF_INET, SOCK_STREAM)
	- When contacted a server will create a new server-side socket to communicate with each client
	- Server may accept connections on this socket
	- Provides reliable transfer of an in-order byte stream (also known as a pipe) from client to server.
7) How does a UDP server know where to send a reply to a datagram? The server application determines the client's IP and port number from the initial data sent by the client. These values must be specified in the response.
8) If a webserver have five ongoing TCP connections using port 80. Assuming the server has no other on going TCP connections, how many TCP sockets are in use on this server. $6$
9) What happens when the socket.connect() procedure is called? Creates a new client socket and connects to the server using that socket.