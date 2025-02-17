### Comparison: HTTP vs HTTPS

| **Criteria**         | **HTTP (HyperText Transfer Protocol)** | **HTTPS (HyperText Transfer Protocol Secure)** |
|----------------------|---------------------------------------|----------------------------------------------|
| **Security**         | ❌ Not secure, data in plain text     | ✅ Secure with SSL/TLS encryption            |
| **Encryption**       | ❌ None, vulnerable to attacks       | ✅ Data encryption during transit            |
| **Authentication**   | ❌ No server identity verification   | ✅ Server verification via SSL/TLS certificate |
| **Data Integrity**   | ❌ Data can be modified in transit   | ✅ Protection against data tampering        |
| **Vulnerabilities**  | Exposed to MITM (Man-In-The-Middle) attacks, network eavesdropping, spoofing | Protected against MITM and malicious interference |
| **Browser Indicator**| 🚨 Displayed as "Not Secure"         | 🔒 Padlock icon, displayed as "Secure"      |
| **SEO Impact**       | Lower Google ranking                 | 🔥 Improves SEO ranking                     |
| **Usage**            | Non-critical sites (blogs, static content) | Sites requiring security (e-commerce, APIs, user logins) |
| **Port Used**        | 80                                    | 443                                          |
| **Cost**             | Free (no certificate needed)         | May require the purchase of an SSL/TLS certificate |
| **Example URL**      | `http://www.example.com`              | `https://www.example.com`                    |

✅ **Conclusion**: HTTPS is essential for ensuring **confidentiality**, **integrity**, and **authenticity** of data, especially for sites handling sensitive information. 🚀

### Structure of an HTTP Request

1. **Client Request**
   - **Method**: GET / POST / PUT
   - **URI**: /page.html
   - **Version**: HTTP/1.1
   - **Headers**:
     - Host: www.example.com
     - User-Agent: Mozilla/5.0
     - Accept: text/html
   - **Body**: (present for POST/PUT)

2. **Server Response**
   - **Version**: HTTP/1.1
   - **Status**: 200 OK
   - **Headers**:
     - Content-Type: text/html
     - Server: Apache
     - Date: Mon, 17 Feb 2025
   - **Body**: HTML content returned

3. **Client Action**
   - Displaying the response in the browser


# HTTP Methods and Status Codes

## **HTTP Methods**

1. **GET**
   - **Description**: Retrieves data.
   - **Use case**: Accessing a web page, fetching data from an API (e.g., viewing a blog post).

2. **POST**
   - **Description**: Sends data to the server, usually to create a new resource.
   - **Use case**: Submitting a registration form, posting a comment on a blog.

3. **PUT**
   - **Description**: Replaces an existing resource or creates a new one if it doesn’t exist.
   - **Use case**: Updating user profile information, modifying an entry in a database.

4. **DELETE**
   - **Description**: Deletes a resource.
   - **Use case**: Deleting a blog post, removing a user from a database.

---

## **HTTP Status Codes**

### **2xx - Success Status**
- **200 OK**
  - **Description**: The request was successfully processed.
  - **Scenario**: Successful access to a web page, retrieving data from an API.
  
- **201 Created**
  - **Description**: The resource was successfully created.
  - **Scenario**: Submitting a form that creates a new resource (e.g., a new user or post).
  
- **204 No Content**
  - **Description**: The request was successfully processed, but there is no content to return.
  - **Scenario**: Deleting an item successfully without a response to display.

---

### **4xx - Client-Side Errors**
- **400 Bad Request**
  - **Description**: The request is malformed or invalid.
  - **Scenario**: Missing or incorrect query parameters in a form.
  
- **401 Unauthorized**
  - **Description**: The request requires authentication.
  - **Scenario**: Attempting to access a protected resource without being logged in.
  
- **403 Forbidden**
  - **Description**: The request is forbidden, even if authentication was successful.
  - **Scenario**: Attempting to access a resource the user doesn't have permission to access.
  
- **404 Not Found**
  - **Description**: The requested resource doesn't exist.
  - **Scenario**: The requested URL is incorrect or the page no longer exists.
  
- **405 Method Not Allowed**
  - **Description**: The HTTP method used is not allowed for this resource.
  - **Scenario**: Trying to use POST when the resource only accepts GET.

---

### **5xx - Server-Side Errors**
- **500 Internal Server Error**
  - **Description**: The server encountered an unexpected error.
  - **Scenario**: A bug in the server or configuration error prevents processing the request.
  
- **502 Bad Gateway**
  - **Description**: The server received an invalid response from an upstream server.
  - **Scenario**: A proxy server or gateway receives an incorrect response from another server.
  
- **503 Service Unavailable**
  - **Description**: The server is temporarily unavailable.
  - **Scenario**: The server is down for maintenance or overloaded with too many requests.
  
- **504 Gateway Timeout**
  - **Description**: The upstream server took too long to respond.
  - **Scenario**: A resource upstream is taking too long to respond (e.g., a remote API).
