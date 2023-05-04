movie_cast(act_id) -> actors(act_id): one-to-many

movie_cast(mov_id) -> movie(mov_id): one-to-many

oscar_awarded(mov_id) -> movie(mov_id): one-to-many

movie_direction(mov_id) -> movie(mov_id): many-to-many

movie_direction(dir_id) -> director(dir_id): many-to-many