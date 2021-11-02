# Saanya Assignment 2 

## Project Overview

For this assignment, I used data from Wikipedia and Reddit, and attempted to use data from IMDB. Essentially, my goal was to write code that a user could then use to select some movie/tv show on Netflix of their liking. I scraped top streaming content on Netflix of all time from Reddit using the filter 'top' from the thread called *NetflixBestOf*. I eventually compounded a list of 20 items and filtered out some items which brought down the list to **12 items**. The associated Wikipedia pages for the 12 tv shows/movies were found and scanned for genre to create a dictionary with genre and movie/show that could be under that genre. Lastly, I attempted to derive the sentiment analysis using IMDB but I sadly was unable to :cry: . The techniques that I used were to strip down the submission text from the Reddit movie/show compilation, find the frequency of a certain genre in the Wikipedia page to match the movie/show with a genre(s), and I attempted to use sentiment analysis as well to derive the sentiment analysis of the first review on IMDB for the particular show/movie. Overall, I hoped to learn how to scrape information from Wikipedia, IMDB and Reddit, and analyze the information to make beneficial to a user. I did not have particular techniques I wanted to focus on, and rather what drove the techniques I used are what I thought may be useful to a user. 

## Implementation 

I started with creating a reddit instance and using **subreddit.top(limit=20)** to find the top 20 submissions to the particular netflix thread. Throughout my program, I use for loop to process different items and append them to new lists. I therefore appended all of the submissions to the subreddit to a list. I created new lists by using the for loop to iterate through items in an old list to append items to a new list only if they start with '[U] and by adjusting the item to strip it of the first 5 characters, by using the [:5] index. It was important to filter only for submissions that began with [U] so that only the movie/show reviews were included in the list, and I used the index function to remove the unwanted elements to strip for just the movie name for the user, but also so python could find the corresponding Wikipedia pages. I also added '(film)' to each item so that Wikipedia would recognize the type of media it was. 

I used a for loop to iterate through all the names, for **each** genre. This was tedious and I experimented with this by creating a function putting in 'genre' as a parameter. So that I could just output a bunch of def('horror); def('crime'), etc. This did not work however, so I had to make for loops for every genre. I was worried about the for loop however, because I remember we went through an example in class where because since the loop keeps iterating, it is important to add something that stops the loop from continuing and adding movie/show names over and over again. However, this was not a problem so I kept it as is. I intentionally wanted to create two lists so that I could use the zip function to create a dictionary. I was hoping to use the movie/show name list for sentiment analysis, and use the zip function again to create a dictionary with movie/show name as key and sentiment analysis for values but the code does not work there and I'm not sure why. 

## Results 

Below is essentially what the program can output. I was hoping to also include a dictionary with the sentiment analysis but I really struggled to make that work.  

```
The following list is a compliation of 11 of the "best of" streaming content on Netflix of all time as decided by Reddit users (limited to what is currently on Netflix, and is actually a movie or tv show):
['The Prestige',
'Trollhunter', 
'The Cube',    
'Rogue One',   
'Nightcrawler',
'Black Mirror',
'O Brother, Where Art Thou?',
'Kubo and the Two Strings',
'The Big Short',
 'Tucker and Dale vs. Evil',
    'Arrested Development']
Still unsure what to watch? Here are the genres that the movies can fall under:
{'Action': ['The Prestige (film)',
            'Trollhunter (film)',
            'Rogue One (film)',
            'Nightcrawler (film)',
            'Kubo and the Two Strings (film)',
            'The Big Short (film)',
            'Arrested Development (film)'],
 'Comedy': ['Nightcrawler (film)',
            'Black Mirror (film)',
            'O Brother, Where Art Thou? (film)',
            'The Big Short (film)',
            'Tucker and Dale vs. Evil (film)',
            'Arrested Development (film)'],
 'Crime': ['Rogue One (film)',
           'Nightcrawler (film)',
           'O Brother, Where Art Thou? (film)',
           'Arrested Development (film)'],
 'Drama': ['The Prestige (film)',
           'Trollhunter (film)',
           'The Cube (film)',
           'Nightcrawler (film)',
           'Black Mirror (film)',
           'O Brother, Where Art Thou? (film)',
           'The Big Short (film)'],
 'Fantasy': ['Trollhunter (film)', 'Kubo and the Two Strings (film)'],
 'Horror': ['Trollhunter (film)',
            'The Cube (film)',
            'Nightcrawler (film)',
            'Black Mirror (film)',
            'Tucker and Dale vs. Evil (film)'],
 'Mystery': ['The Prestige (film)', 'The Cube (film)'],
 'Science-fiction': ['The Cube (film)'],
 'Thriller': ['The Prestige (film)', 'Nightcrawler (film)']}

 ```

## Reflection

I think that my code is quite long for no reason. I would really like to learn how to be able to shorten it. I think I may have overused the .append method with lists, but I'm glad that I really got the hang of using this method throughout this project. Overall, accessing Reddit and Wikipedia went very smoothly and I was amazed to how that worked and how easy it was. It was very difficult for me to try to scrape data from IMDB because I initially wanted to include the rating instead of the review. When I exhausted external resources trying to find how to get the rating, and saw that it involved HTML and modules like 'BeautifulSoup' I decided to stick to Sentiment Analysis. It would have been great if the Sentiment Analysis worked out, but potentially there is something wrong with the import for nltk. 

What I am not sure about is if my assignment/project is challenging enough or worthwhile from a third point of view persepctive. To me, it was incredibly worthwhile and although the learning curve was **STEEP**, I feel more comfortable with Python than I ever have. For some people it may come quicker than others, and for me I know that it takes *time*, but as soon as I can put in the *hours* and really **focus** it becomes really interesting and I find myeslf absorbed in the code. 

What also helped me succeed was frequently using type() and print() to pinpoint where the code and me ceased to be on the same page, and check for possible errors due to data type. Going forward, I am very inclined to create more programs like this, it is particulary interesting to me to create programs that actually *help* users in decision making processes, which is why I was inclined toward a restaurant data base for my final project as well. Before I started, I wish I knew that this assignment would take me a *long, long* time. It is difficult to manage other coursework, along with recuriting, along with extracurricular activities with actually *learning* Python, but if I put in the hours, I end up being really absorbed and interested in what I'm making. 