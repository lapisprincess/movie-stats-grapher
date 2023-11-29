-- turn on foreign keys
PRAGMA foreign_keys = ON;

-- delete tables if they already exist
-- if relation not specified, refers to title
drop table if exists Akas;
drop table if exists Title_basics;
-- OMITTED - Crew (its basically all string arrays)
drop table if exists Episode;
drop table if exists Principals;
drop table if exists Ratings;
drop table if exists Name_basics;

CREATE TABLE Akas (
	titleId TEXT PRIMARY KEY -- a tconst, an alphanumeric unique identifier of the title
	ordering INTEGER -- a number to uniquely identify rows for a given titleId
	title TEXT -- the localized title
	region TEXT -- the region for this version of the title
	language TEXT -- the language of the title
	-- OMITTED: types (array)
	-- OMITTED: attributes (array)
	isOriginalTitle INTEGER -- 0: not original title; 1: original title
);

CREATE TABLE Title_Basics (
	tconst TEXT PRIMARY KEY -- alphanumeric unique identifier of the title
	titleType TEXT -- the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
	primaryTitle TEXT -- the more popular title / the title used by the filmmakers on promotional materials at the point of release
	originalTitle TEXT -- original title, in the original language
	isAdult INTEGER -- 0: non-adult title; 1: adult title
	startYear INTEGER -- (YYYY) represents the release year of a title. In the case of TV Series, it is the series start year
	endYear INTEGER -- (YYYY) TV Series end year. ‘\N’ for all other title types
	runtimeMinutes INTEGER -- primary runtime of the title, in minutes
	-- OMITTED: genres (string array)
);

