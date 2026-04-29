DESCRIPTION

I chose the web-scraper project for my final project of this CMPSC 132 course. 

This project uses the Beautiful Soup 4 module to scrape an indexed website which contains a list of laptops with their brand names, price and ratings inside ‘cards’. 

-	First, I started with fetching the websites index.html using the requests module and creating a soup from it. Then I loaded all cards from the soup using the find_all function into a variable ‘cards’.
-	Second, I iterated through that variable to get the title, price and ratings from each ‘card’ using the find function. I chose to yield these instead of return since that stops it from returning them every time.
-	Third, I created a function for each of these functionalities: search, filter by rating, filter by price and main.
-	Last, I started an infinite loop which runs till the user wants. Which takes all the inputs and calls the required functions.

INSTRUCTIONS TO RUN THE PROGRAM

Upon running the code, it will print the entire directory it's fetching and will ask for an input choice: "P", "R", "S", or "E" to filter by price, filter by rating, search, and end respectivelly.

Thank you.
