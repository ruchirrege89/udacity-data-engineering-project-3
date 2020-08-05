_This project is a part of [Udacity's Data Engineer Nano Degree](https://eu.udacity.com/course/data-engineer-nanodegree--nd027)._

# Purpose of this database for, Sparkify, a startup and their analytical goals.
The popularity of the Sparkify music app has led the management to strategize their move to cloud. In doing so there is a need to move theor logs already stored on AWS S3 to AWS data warehouse offering Redshift. This is an ideal move for Sparify as it will be able to focus on their growing business and database design rather then worring about the infrastructure and it's needs. Since this is in continuation of their first phase of data warehouse building and have continued to eye the long term goal of gaining insights like most played songs, user engagaement, subscriptions etc and generating new features to grow their business. The data collected in these databases can also be used to run machine learning models in the long run.

# Justifying the database schema design and the ETL pipeline.

Database Schema Design:

The database design is in continuation of the initial/on-prem database schema which consists of Fact: songsplay (user song play data) and Dimensions: users (user info), songs (song info), artists (artist info), time (time info). This will reduce the learning curve of the Analytics teams to analyze WHERE, WHEN and WHAT questions against a metric. The 4 dimension tables mentioned above are related to fact table in the Star Schema format which allows for easy readability of data, query centric design and reduced duplication of records in fact table.

ETL Pipeline

The ETL pipeline allows for data loading from AWS S3 in the batch mode. After pointing the ETL scripts with the correct S3 paths for songs and logs, it reads-transforms-loads the data in AWS Redshift tables. Time dimension is an important dimension for analysis and and the ETL efficiently handles the time in milliseconds reported in log file and transforms in hour, day, month and year. This seemed a complex task at first but with pandas dt attribute it allowed for an easy transformation of date-time data.

To run the ETL trigger the below python modules from command line:

`python3 create_tables.py`
`python3 etl.py`

# Example queries and results for song play analysis.

Question - Which artists's songs were played often by the users

Query -

`select
    a.name, count(*) SongFrequency
from songplays s
    left join artists a
        on s.artist_id = a.artist_id
group by s.user_id, u.first_name, u.last_name, s.artist_id, a.name, t.year`
