
###LIVE URL 

- http://139.59.24.38:8010/

###GITHUB URL 
 
 - https://github.com/sreejasn7/book_lend_store.git

###FOR PYTHON TESTS - 

- Used Selenium. 
>> python manage.py tests.

Note: 
1. Dockerized the solution which is up and running
2. Any CI tool has not been used.
3. Handle Large Requests
- DB connections
    - Restrict the max connections to DB 
    - Set proper buffer pool based on system RAM 
- Dispensing client requests across multiple servers.
- Setting Timeout , Max client requests  in webserver config.
- Enabling multiprocessing / cron jobs. 
   
