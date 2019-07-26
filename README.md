
###LIVE URL 

- http://139.59.24.38:8010/

###GITHUB URL 
 
 - https://github.com/sreejasn7/book_lend_store.git

### Work Flow to login above
1. Register as a customer through the right top person icon. 
It will take you to register / login page. 
2. Register as a customer . 
3. Login as the same customer. 
4. Hover Books menu.
5. Select menu other than Old-stock (Old-stock was story one)
6. Click on any images down .
7. You can see "ADD TO CART"
8. After clicking , html will display rented above the ADD to CART button.
9. Add any number of products like above as you wish . 
10. Login as admin by  `admin` / `admin@123`
11. You will see admin page new tab near to BOOKS.
12. Click and you will see select customer. 
13. On change customer , it will load the added to cart books.
14. Option to provide days is given.
15. After entering days , click calculate 
16. The amount is calculated in the text box on down right end.
The calculation is now based on story 3.


###FOR PYTHON TESTS - 
- Used Selenium and unit test >>  python manage.py tests.

####RUN THE APPLICATION AT LOCAL:
   
- Prior Installation
    - Docker
    - Docker Compose 
 
- git clone https://github.com/sreejasn7/book_lend_store.git
- cd book_lend_store
-  docker-compose up
- Will run at 0.0.0.0:8010 

- Note:
This will also create dummy book data with all three types 
 and create user `admin` / `admin@123`
 

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


