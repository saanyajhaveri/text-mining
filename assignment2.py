""" My Assignment 2 uses Reddit to find the best Netflix content of all time, and then Wikipedia to create a dictionary based on genre of these movies"""
import praw
import config
import pprint

""" The below reddit import was derived from https://github.com/praw-dev/praw"""
reddit = praw.Reddit(
    client_id = 'fHg_QCRdsGZGnmhNcjkKQw',
    client_secret = 'y0jRFeG560aevJFKiLBP40xGOUWLhg',
    user_agent = 'visualstudio:myexampleapp:v1.2.4 (by u/sjhaveri1)',
    username = 'sjhaveri1',
    password = 'Purvihitesh1!!',
)
""" creating a Reddit instance and specifying the thread: NetflixBestOf"""
subreddit = reddit.subreddit('NetflixBestOf')
#print('The following list is a compliation of 11 of', subreddit.title[10:],'of all time as decided by Reddit users (limited to what is currently on Netflix, and is actually a movie or tv show):')
submission_list=[]
for submission in subreddit.top(limit=20):
    submission_list.append(submission.title)
"""Limiting the list to 20 items"""

"""Below I filter for items that begin with [U because I noticed that all of the content references start with [US] where as there are other posts talking about
various things like bringing back content on netflix and those start with other characters such as [D for [Discussion]"""

updated_submissionlist=[]
for element in submission_list:
    if element.startswith('[U'):
        updated_submissionlist.append(element)

movie_show_list=[]
for i in updated_submissionlist:
    movie_show_list.append(i[5:])
del movie_show_list[1]
del movie_show_list[5]
del movie_show_list[7]
""" I deleted items that are no longer on netflix or are not a movie/tv show, such as the 4K Fireplace """

newlist=[movie_show_list[0][:12], movie_show_list[1][:11], movie_show_list[2][:8], movie_show_list[3][:9], movie_show_list[4][:12], movie_show_list[5][:12], movie_show_list[6][:26],
movie_show_list[7][:24], movie_show_list[8][:13], movie_show_list[9][:24], movie_show_list[10][:20]]

""" In order to look up the names on Wikipedia, I had to strip the movie/show names to just their names without the year and description. This was also a preferable
format for the output list for the user. I also realized that it waas necessary to specify '(film)' so that Wikipedia knew that it was a movie/show and not a book etc"""
#pprint.pprint(newlist)
stradd = ' (film)'
newlistfor_wikipedia = []
for item in newlist:
    newlistfor_wikipedia.append(item + stradd)

""" The below wikipedia import was derived from https://github.com/barrust/mediawiki"""

from mediawiki import MediaWiki
wikipedia= MediaWiki()
""" Next I look up the count of each of the genre names on the Wikipedia page for each movie to create a list for each genre with the movie titles"""
horror = []
thriller =[]
mystery = []
science_fiction = []
action = []
crime = []
comedy = []
fantasy = []
drama = []

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('horror') >= 1:
        horror.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('thriller') >= 1:
        thriller.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('mystery') >= 1:
        mystery.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('sci-fi') >= 1:
        science_fiction.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('action') >= 1:
        action.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('crime') >= 1:
        crime.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('comedy') >= 1:
        comedy.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('fantasy') >= 1:
        fantasy.append(name)
    else:
        continue

for name in newlistfor_wikipedia:
    page_finder = wikipedia.page(name)
    page_finder.content.split()
    if page_finder.content.count('drama') >= 1:
        drama.append(name)
    else:
        continue

genres = ['Horror', 'Thriller', 'Mystery', 'Science-fiction', 'Action', 'Crime', 'Comedy', 'Fantasy', 'Drama']
movies = [horror, thriller, mystery, science_fiction, action, crime, comedy, fantasy, drama]

"""I then used the zip function to make a dictionary with the genres as keys and movies that fall under the genres as values"""

movie_genre_dictionary = dict(zip(genres,movies))

#print('Still unsure what to watch? Here are the genres that the movies can fall under:')
#pprint.pprint(movie_genre_dictionary)

"""I proceeded to derive the sentiment analysis for the first review for each of the movies on Imdb"""

""" The below imdb import was derived from https://github.com/saanyajhaveri/text-mining/blob/master/instructions.md, I used the example in the 
instructions provided by you! """
from imdbpie import Imdb

imdb = Imdb()
imdb.search_for_name("The Prestige" [0])
reviews1 = imdb.get_title_user_reviews("tt0482571")
theprestige = [(reviews1['reviews'][0]['reviewText'])]

imdb.search_for_name("Trollhunter" [0])
reviews2 = imdb.get_title_user_reviews("tt1740707")
trollhunter = [(reviews2['reviews'][0]['reviewText'])]

imdb.search_for_name("The Cube" [0])
reviews3 = imdb.get_title_user_reviews("tt0123755")
thecube = [(reviews3['reviews'][0]['reviewText'])]

imdb.search_for_name("Rogue One" [0])
reviews4 = imdb.get_title_user_reviews("tt3748528")
rogueone = [(reviews4['reviews'][0]['reviewText'])]

imdb.search_for_name("Nightcrawler" [0])
reviews5 = imdb.get_title_user_reviews("tt2872718")
nightcrawler = [(reviews5['reviews'][0]['reviewText'])]

imdb.search_for_name("Black Mirror" [0])
reviews6 = imdb.get_title_user_reviews("tt0482571")
blackmirror = [(reviews6['reviews'][0]['reviewText'])]

imdb.search_for_name("O Brother, Where Art Thou?" [0])
reviews7 = imdb.get_title_user_reviews("tt0190590")
obrotherwhereartthou = [(reviews7['reviews'][0]['reviewText'])]

imdb.search_for_name("Kubo and the Two Strings" [0])
reviews8 = imdb.get_title_user_reviews("tt4302938")
kuboandthetwostrings = [(reviews8['reviews'][0]['reviewText'])]

imdb.search_for_name("The Big Short" [0])
reviews9 = imdb.get_title_user_reviews("tt1596363")
thebigshort = [(reviews9['reviews'][0]['reviewText'])]

imdb.search_for_name("Tucker and Dale vs. Evil" [0])
reviews10 = imdb.get_title_user_reviews("tt1465522")
tuckeranddale = [(reviews10['reviews'][0]['reviewText'])]

imdb.search_for_name("Arrested Development" [0])
reviews11 = imdb.get_title_user_reviews("tt0367279")
arresteddevelopment = [(reviews11['reviews'][0]['reviewText'])]


"""When I printed the lists I made above storing the first review for each movie, they correctly stored the reviews as I'd hoped. 
That being said, I played around with the code below a lot but was unable to produce the sentiment analysis for each of the reviews """

"""The below nltk import was derived from https://www.nltk.org/howto/sentiment.html"""

#forsentimentanalysis=[theprestige, trollhunter, thecube, rogueone, nightcrawler, blackmirror, obrotherwhereartthou, kuboandthetwostrings, thebigshort, tuckeranddale, arresteddevelopment]
#import nltk
#nltk.download('vader_lexicon')
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#sentimentscore = []
#for item in forsentimentanalysis:
    #sentimentscore.append(SentimentIntensityAnalyzer().polarity_scores(item))

#""" I used the zip function to make a dictionary with movies and their corresponding sentiment scores"""

#sentimentscore_dictionary = dict(zip(newlistfor_wikipedia,sentimentscore))

#print("Here are the sentiment scores for the movies as per the first review for each movie on IMDB")

#print(sentimentscore_dictionary)


"""I know that the first 4 lines of the code below works, since I tested them above where there are # comments. But because of the sentiment analysis errors, it is not
possible to test the code below"""

def main():
    print('The following list is a compliation of 11 of', subreddit.title[10:],'of all time as decided by Reddit users (limited to what is currently on Netflix, and is actually a movie or tv show):')
    pprint.pprint(newlist)

    print('Still unsure what to watch? Here are the genres that the movies can fall under:')
    pprint.pprint(movie_genre_dictionary)

    #print("Here are the sentiment scores for the movies as per the first review for each movie on IMDB")
    #print(sentimentscore_dictionary)


if __name__ == "__main__":
    main()















   





    










