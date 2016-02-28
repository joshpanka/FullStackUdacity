-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
    name	TEXT,
    id 		SERIAL PRIMARY KEY
);

CREATE TABLE matches (
	winner	INTEGER REFERENCES players(id),
	loser	INTEGER REFERENCES players(id)
);

CREATE VIEW winning_record AS SELECT players.id, count(matches.winner) as wins
FROM players LEFT JOIN matches ON players.id=matches.winner
GROUP BY players.id ORDER BY wins DESC;

CREATE VIEW losing_record AS SELECT players.id, count(matches.loser) as losses
FROM players LEFT JOIN matches ON players.id=matches.loser
GROUP BY players.id ORDER BY losses DESC;

CREATE VIEW total_games AS SELECT winning_record.id,
(winning_record.wins+losing_record.losses) AS total
FROM losing_record, winning_record WHERE winning_record.id=losing_record.id;

CREATE VIEW player_standings AS SELECT players.id, players.name,
winning_record.wins AS wins, total_games.total AS matches FROM
players, winning_record, total_games WHERE players.id=winning_record.id
AND players.id=total_games.id ORDER BY wins DESC;

CREATE VIEW player_rank AS SELECT ROW_NUMBER() OVER
(ORDER BY wins) AS rank, id, name FROM player_standings ORDER BY wins;

CREATE VIEW swiss_pairs AS SELECT s1.id AS id1, s1.name AS name1, s2.id AS id2,
s2.name AS name2 FROM player_rank s1, player_rank s2 WHERE s1.rank = s2.rank-1 AND s1.rank%2=1;

