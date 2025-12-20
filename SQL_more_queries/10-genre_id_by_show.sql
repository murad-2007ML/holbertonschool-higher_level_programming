-- displaying genres
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows.id = tv_shows.genre_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;
