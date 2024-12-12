Select ratings.rating,movies.title from ratings join movies ON movies.id = ratings.movie_id where movies.year = 2010 Order By ratings.rating DESC, movies.title ASC;
