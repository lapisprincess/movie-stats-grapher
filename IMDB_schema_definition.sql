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
	FOREIGN KEY(tconst) REFERENCES Akas(titleId)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- OMITTED: TABLE Crew. 3 attributes, one is tconst, other two are arrays.

CREATE TABLE Episode (
	tconst TEXT PRIMARY KEY -- alphanumeric identifier of episode
	parentTconst TEXT -- alphanumeric identifier of the parent TV Series
	seasonNumber INTEGER -- season number the episode belongs to
	episodeNumber INTEGER -- episode number of the tconst in the TV series
	FOREIGN KEY(tconst) REFERENCES Akas(titleId)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	
)

CREATE TABLE Principals (
	tconst TEXT PRIMARY KEY -- alphanumeric unique identifier of the title
	ordering INTEGER -- a number to uniquely identify rows for a given titleId
	nconst TEXT -- alphanumeric unique identifier of the name/person
	category TEXT -- the category of job that person was in
	job TEXT -- the specific job title if applicable, else '\N'
	characters TEXT -- the name of the character played if applicable, else '\N'
)

CREATE TABLE Ratings (
	tconst TEXT PRIMARY KEY -- alphanumeric unique identifier of the title
	averageRating REAL -- weighted average of all the individual user ratings
	numVotes INTEGER -- number of votes the title has received
)

CREATE TABLE Basics (
	nconst TEXT PRIMARY KEY -- alphanumeric unique identifier of the name/person
	primaryName TEXT -- name by which the person is most often credited
	birthYear INTEGER -- in YYYY format
	deathYear INTEGER -- in YYYY format if applicable, else '\N'
	-- OMITTED: primaryProfession (array of strings)
	-- OMITTED: knownForTitles (array of tconsts)