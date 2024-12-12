Select name from people where id IN (Select person_id from stars where movie_id IN
(Select id from movies where title like '%Toy Story%'));
