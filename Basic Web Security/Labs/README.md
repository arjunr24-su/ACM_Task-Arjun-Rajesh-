# Cybersecurity Labs Progress

## Overview
This repository documents my journey through the cybersecurity labs, from apprentice to practitioner levels. It includes the challenges I faced, the solutions I implemented, and the knowledge I gained along the way.

## Experiences
(Only Apprentice level tasks)
### Cross-Site Scripting (XSS)
- **Description:** XSS is a type of injection attack where malicious scripts are injected into otherwise benign and trusted websites.
- **Experience:** I practiced identifying and exploiting XSS vulnerabilities in various web applications. One notable instance was discovering a stored XSS vulnerability in a test application, which allowed me to execute arbitrary JavaScript code in the context of another user's session.
- **Key Learnings:** The importance of input validation and output encoding to prevent XSS attacks.

### Cross-Site Request Forgery (CSRF)
- **Description:** CSRF is an attack that forces an end user to execute unwanted actions on a web application in which they are currently authenticated.
- **Experience:** I simulated CSRF attacks to understand how they exploit the trust a web application has in the user's browser. I successfully performed a CSRF attack that changed a user's email address without their consent.
- **Key Learnings:** Implementing anti-CSRF tokens and ensuring proper validation of user requests to mitigate CSRF risks.

### SQL Injection (SQLi)
- **Description:** SQLi is a code injection technique that exploits a vulnerability in an application's software by manipulating SQL queries.
- **Experience:** I identified and exploited SQL injection vulnerabilities in several test environments. One significant achievement was bypassing authentication by injecting SQL code into a login form, demonstrating the critical need for secure coding practices.
- **Key Learnings:** The necessity of using parameterized queries and prepared statements to prevent SQL injection attacks.

## Tools and Technologies
### Burp Suite
- **Description:** Burp Suite is a powerful web vulnerability scanner and penetration testing tool developed by PortSwigger.
- **Usage:** I used Burp Suite extensively for web application security testing, including tasks like intercepting HTTP requests, scanning for vulnerabilities, and performing automated and manual testing.
- **Experience:** During one of the labs, I discovered a critical SQL injection vulnerability in a test web application using Burp Suite. This experience taught me the importance of thorough testing and the effectiveness of Burp Suite in identifying security flaws.

### PortSwigger
- **Description:** PortSwigger is the company behind Burp Suite, known for its contributions to web security research and education.
- **Resources:** I utilized various resources from PortSwigger, including their Web Security Academy, which provided in-depth tutorials and hands-on labs to enhance my understanding of web security concepts.

## Conclusion
With consistent practice and dedication, I am confident in my ability to excel in the field of cybersecurity. This journey has been challenging yet rewarding, and I look forward to further enhancing my skills and knowledge.



