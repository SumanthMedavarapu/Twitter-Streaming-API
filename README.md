# Twitter-Streaming-API

I am going to keep punctuation,emoji,hashtags and anything else that comes with raw text and this is my defination of Machine Learning dataset because emoji and hashtags provide valuable info on any Downstream ML task 

### Steps:
* Connected to the Twitter streaming API by creating project and accessed API using Bearer Token and done with keyword search on "Justin Bieber"

![twitter_acct](https://user-images.githubusercontent.com/60243899/150699871-112c764b-b143-44b4-b684-ed85a9c781dd.JPG)

* In order to filter out(remove) music from all tweets, I have done keyword match by passing all acroynms related to music in the query "-music" etc.some of the combination of keywords could be (sound, music, singing, rock, tune, melody,etc). granted that there could be more keywords that's related to music being omitted at this current analysis further defination on music as a keyword needs to be optimized. 

![filter_out_music](https://user-images.githubusercontent.com/60243899/150699890-39bf69a1-7f05-4150-9f82-fbe87f886b7e.JPG)

* Dropped the duplicates like retweets using -is:retweet in the query

* Stored the tweets into a MongoDB(NoSQL) database 

![store_mongodb](https://user-images.githubusercontent.com/60243899/150699898-9939ed9c-7962-4bc1-bbec-b59895058825.JPG)



![mongodb](https://user-images.githubusercontent.com/60243899/150699908-01331fe7-704f-4d83-8915-fd6d3e84c6cf.JPG)

* Produced the count for all and unique(removed duplicates) tweets consumed per day by calling "get_recent_tweets_count()" as shown below

![unique_all_tweet_count](https://user-images.githubusercontent.com/60243899/150699920-0666056d-0fcc-4591-bd6d-7783bd977d50.JPG)



### What are the risks involved in building such a pipeline?

*  the way that this ETL pipeline is developed will continuously gather or collect 100 tweets every few seconds and will not consider disk space for its execution.
* The current ETL pipeline don't have mechanism to remove and update tweets(might consider tweets removing tweets older than 90 days or archive tweets older than a set period of time).
* The current ETL pipeline gather only id, text and created timestamp if more features are requested the current pipeline needs to be modified.
* The current pipeline don't have unit tests and the code are not fully optimized for production.
* The current ETL pipeline uses MongoDB as Datastore option. Could consider other storage option based on business requirement(Eg. graphDB to explore social media connection) 
* Consider Docker, containers for independent execution environment

### How would you roll out the pipeline going from proof-of-concept to a production-ready solution?

* Migration to cloud, testing and validating various test cases
* Performing Stress tests and benchmarking to make sure pipeline can sustain peak hour traffic.
* Refactoring the code to be Modular and reusable, executing the code or containerizing in Docker
* Optimize the Dataflow and develop CRUD mechanism.
* Deploy using CI/CD so that it is continuous pipeline Development  


### What would a production-ready solution entail that a POC wouldn't? 

* Production ready solution would have extensive error logging mechanism and pipeline health monitoring whereas POC doesn't.
* Production ready solution would need to have disaster recovery mechanism.
* Production ready solution needs to be scaled automatically to meet traffic demand.
* Production ready solution is also cost optimized.


### What is the level of effort required to deliver each phase of the solution?
* In order to move the solution from Proof of Concept to Production.we need to perform code optimization,unit testing,Data Validation and pipeline benchmarking etc.For each one of this phase it would take roughly 2 to 3 days to complete.

### What is your estimated timeline for delivery for a production-ready solution?

* It would take something around 2 - 4 weeks because we need to migrate to cloud first and perform code optimization, unit testing, data validation, pipeline benchmarking etc to make sure pipeline is ready for Production.
