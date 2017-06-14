from media import Movie
from fresh_tomatos import open_movies_page

list_of_movies = []
eternal_sunshine = Movie("Eternal Sunshine","1h 48m","https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg","https://www.youtube.com/watch?v=yE-f1alkq9I")
list_of_movies.append(eternal_sunshine)
empire_strikes_back = Movie("Empire Strikes Back","2h 7m","https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg","https://www.youtube.com/watch?v=96v4XraJEPI")
list_of_movies.append(empire_strikes_back)
back_to_the_future = Movie("Back To The Future","1h 56m","https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg","https://www.youtube.com/watch?v=qvsgGtivCgs")
list_of_movies.append(back_to_the_future)
pirates_of_silicon_valley = Movie("Pirates Of Silicon Valley","1h 35m","https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Movieposterposv.jpg/250px-Movieposterposv.jpg","https://www.youtube.com/watch?v=lEyrivrjAuU")
list_of_movies.append(pirates_of_silicon_valley)
die_hard = Movie("Die Hard","2h 12m","https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Die_hard.jpg/220px-Die_hard.jpg","https://www.youtube.com/watch?v=2TQ-pOvI6Xo")
list_of_movies.append(die_hard)
gremlins = Movie("Gremlins","1h 46m","https://upload.wikimedia.org/wikipedia/en/3/3d/Gremlins1.jpg","https://www.youtube.com/watch?v=z9DNOuEv7iI")
list_of_movies.append(gremlins)
et = Movie("E.T.","1h 56m","https://upload.wikimedia.org/wikipedia/en/thumb/6/66/E_t_the_extra_terrestrial_ver3.jpg/220px-E_t_the_extra_terrestrial_ver3.jpg","https://www.youtube.com/watch?v=qYAETtIIClk")
list_of_movies.append(et)
goonies = Movie("Goonies","1h 54m","https://upload.wikimedia.org/wikipedia/en/thumb/c/c6/The_Goonies.jpg/220px-The_Goonies.jpg","https://www.youtube.com/watch?v=hJ2j4oWdQtU")
list_of_movies.append(goonies)
lord_of_the_rings = Movie("Fellowship Of The Ring","2h 58m","https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=V75dMMIW2B4")
list_of_movies.append(lord_of_the_rings)

open_movies_page(list_of_movies)

