1) What is the IP of the Indian Institute of Technology in Bombay
	- 103.21.124.10
2) What is the IP of the DNS server:
	- 208.67.222.222
3) Did the response come from an authoritative or non authoritative server:
	- Non authoritative
4) What is the name of the authoritative name server: 
	- dns1.iitb.ac.in
5) How would you find the IP of the authoritative name server
	- nslookup dns1.iitb.ac.in

5) Locate the DNS query for gaia.cs.umass.edu:
a) What is the packet number: 15
b) Was this query sent over UDP or TCP? UDP

6) Locate the repsonse
a) What is the packet number: 17
b) What the response sent over UDP or TCP? UDP

7) Port number
a) DNS query destination port: 53
b) DNS response source port: 53

8) To what IP was the query sent?
a) 75.75.75.75

9) How many questions in the query? 1 How many answers 0

10) How many question does the reponse contain? 1 How many answers? 1
11) 
a) What is the packet number in the trace for the initial HTTP GET request for the base file http://gaia.cs.umass.edu/kurose_ross/? 22

b) What is the packet number in the trace of the DNS query made to resolve gaia.cs.umass.edu so that this initial HTTP request can be sent to the gaia.cs.umass.edu IP address? 15

c) What is the packet number in the trace of the received DNS response? 17

d) What is the packet number in the trace for the HTTP GET request for the image object http:// gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E2.jpg? 205

e) What is the packet number in the DNS query made to resolve gaia.cs.umass.edu so that this second HTTP request can be sent to the gaia.cs.umass.edu IP address? There is not one made


## Packet 2

12) What is the destination port for the DNS query message? What is the source port of the DNS response message?

53, 53

13) To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?

75.75.75.75, yes

15) Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?

A, no answers

17) Examine the DNS response message to the query message. How many “questions” does this DNS response message contain? How many “answers”? 1, 1

18) To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server? 208.67.222.222, no

19) Examine the DNS query message. How many questions does the query have? Does the query message contain any “answers”?
1, no

21) Examine the DNS response message. How many answers does the response have? What information is contained in the answers? How many additional resource records are returned? What additional information is included in these additional resource records?
3, ![[Pasted image 20230307142134.png]]