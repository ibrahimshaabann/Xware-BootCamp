## parameters and queryparameters
Both the way of passing data in get request and the deference is something below

Params:

https://localhost:3000/user/5896544

access from backend:

request.params.userId = 5896544

Query String:

https://localhost:3000/user?userId=5896544

access from backend:

request.query.userId = 5896544




# HTTP Methods and Status Codes

HTTP methods and status codes are fundamental concepts in web development and the HTTP protocol. They define how clients (e.g., web browsers) and servers communicate with each other. Here's a list of common HTTP methods and their associated status codes:

## HTTP Methods

1. **GET**: Retrieve data from the server. It should not have any side effects on the server's data.

2. **POST**: Submit data to the server for processing. It may create new resources on the server or modify existing ones.
 > it returns status code 201 **created**

3. **PUT**: Update data on the server. It typically replaces the entire resource with the new data provided in the request.

4. **PATCH**: Partially update data on the server. It applies modifications to the resource, rather than replacing it entirely.
> the mumber appears next to patch suppose : 200 162 ---> the 162 refers to the content length

5. **DELETE**: Remove a resource from the server.
> returns status code 204 no content

6. **HEAD**: Similar to GET but only retrieves the headers, not the actual data. Used for checking resource headers without downloading the resource itself.

7. **OPTIONS**: Retrieve information about the communication options for the target resource.

8. **CONNECT**: Establish a network connection to the target resource, typically for use with a proxy.

9. **TRACE**: Perform a diagnostic test to check the route and intermediary servers between the client and server.

## HTTP Status Codes

HTTP status codes are three-digit numbers returned by the server to indicate the outcome of a request. They are divided into different classes:

1. **1xx (Informational)**: The request was received, and further action is needed.
   - 100: Continue
   - 101: Switching Protocols

2. **2xx (Successful)**: The request was successfully received, understood, and accepted.
   - 200: OK
   - 201: Created
   - 204: No Content (successful response with no body)
   - 206: Partial Content (for partial GET requests)

3. **3xx (Redirection)**: The request needs further action to be fulfilled.
   - 301: Moved Permanently (resource has permanently moved)
   - 302: Found (resource has temporarily moved)
   - 304: Not Modified (cached response can be used)

4. **4xx (Client Error)**: The request contains bad syntax or cannot be fulfilled by the server due to client-related issues.
   - 400: Bad Request
   - 401: Unauthorized
   - 403: Forbidden
   - 404: Not Found
   - 422: Unprocessable Entity (often used in REST APIs)

5. **5xx (Server Error)**: The server failed to fulfill a valid request.
   - 500: Internal Server Error
   - 502: Bad Gateway
   - 503: Service Unavailable
   - 504: Gateway Timeout


