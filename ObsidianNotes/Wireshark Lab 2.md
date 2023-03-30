1. Is your browser running HTTP version 1.0, 1.1, or 2? What version of HTTP is the server running?

- Local machine: HTTP 1.1
- Server: HTTP 1.1

2. What languages (if any) does your browser indicate that it can accept to the server?

- en-US
- en

3. What is the IP address of your computer? What is the IP address of the gaia.cs.umass.edu server

Your Computer: 10.0.0.44
Server: 128.119.245.12

4. What is the status code returned from the server to your browser?

- 200 OK

5. When was the HTML file that you are retrieving last modified at the server?

- Sat, 30 Jan 2021 06:59:02 GMT

6. How many bytes of content are being returned to your browser?

- 128 bytes

7. By inspecting the raw data in the packet content window, do you see any headers within the data that are not displayed in the packet-listing window? If so, name one.

- No

8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?

- No

9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?

- Line based text data tag

10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET ? If 6 so, what information follows the “IF-MODIFIED-SINCE:” header?

- Sat, 30 Jan 2021 06:59:02 GMT (Last access time)

11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.

- 304 Not Modified
- No, the contents were not sent

12. How many HTTP GET request messages did your browser send? Which packet number in the trace contains the GET message for the Bill or Rights?

- 1, 26

13. Which packet number in the trace contains the status code and phrase associated with the response to the HTTP GET request?

- 32

14. What is the status code and phrase in the response?

- 200 OK

15. How many data-containing TCP segments were needed to carry the single HTTP response and the text of the Bill of Rights?

- 4

TCP Segment Numbers:
- 28
- 29
- 31
- 32

16. How many HTTP GET request messages did your browser send? To which Internet addresses were these GET requests sent?

- 4
- 128.119.245.12 
- 128.119.245.12
- 178.79.137.164
- 104.98.115.146

17. Can you tell whether your browser downloaded the two images serially, or whether they were downloaded from the two web sites in parallel? Explain.

- Serial

18. . What is the server’s response (status code and phrase) in response to the initial HTTP GET message from your browser?

- 401

20. When your browser’s sends the HTTP GET message for the second time, what new field is included in the HTTP GET message?

- Authorization


