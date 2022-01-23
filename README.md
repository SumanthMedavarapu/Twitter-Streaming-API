# Twitter-Streaming-API

I am going to keep punctuation,emoji,hashtags and anything else that comes with raw text and this is my def of ML dataset.this is because emoji and hashtags provide valuable info on any downstream ML task 

### Steps:
* Connected to the Twitter streaming API by creating project and accessed API using Bearer Token and done with keyword search on "Justin Bieber"

![twitter_acct](https://user-images.githubusercontent.com/60243899/150699871-112c764b-b143-44b4-b684-ed85a9c781dd.JPG)

* In order to filter out(remove) music from all tweets, I have done keyword match by passing all acroynms related to music in the query "-music" etc.some of the combination of keywords could be (sound, music, singing, rock, tune, melody) and used them as filter 

![filter_out_music](https://user-images.githubusercontent.com/60243899/150699890-39bf69a1-7f05-4150-9f82-fbe87f886b7e.JPG)

* Dropped the duplicates like retweets using -is:retweet in the query

* Stored the tweets into a MongoDB(NoSQL) database 

![store_mongodb](https://user-images.githubusercontent.com/60243899/150699898-9939ed9c-7962-4bc1-bbec-b59895058825.JPG)



![mongodb](https://user-images.githubusercontent.com/60243899/150699908-01331fe7-704f-4d83-8915-fd6d3e84c6cf.JPG)

* Produced the count for all and unique(removed duplicates) tweets consumed per day by calling "get_recent_tweets_count()" as shown below

![unique_all_tweet_count](https://user-images.githubusercontent.com/60243899/150699920-0666056d-0fcc-4591-bd6d-7783bd977d50.JPG)



#### What are the risks involved in building such a pipeline?
* scalability, 100 tweets every 5 sec, when would it stop working -> space disk issue, how long are we storing, mechansim to remove tweets older than 90 days, 
-> way to write code to run faster->better way to store the data than current Iam using-> consider docker, containers

#### How would you roll out the pipeline going from proof-of-concept to a production-ready solution?
* migration to cloud, testing, validation the test cases, sustain the stress in the peak hours(1000 tweets high amt of data if it comes at a time)
-> refactoring the code to be moduler and reusable, executing the code or containerizing in docker -> optimize the dataflow -> best way to write CRUD for move to other DB
-> deploy using CI/CD so that continuous pipeline dev



#### What would a production-ready solution entail that a POC wouldn't?
* if it fails in prod we can backup, scalability, maintainability, cost, 
error logging Prod ready sol will do and unit sol as well that POC wouldn't


#### What is the level of effort required to deliver each phase of the solution?
* POC->prod   valid,testing(how long it takes in each phase it takes a week for one phase, unit testing, error logging Prod ready sol will do and unit sol as well that POC wouldn't
->

#### What is your estimated timeline for delivery for a production-ready solution?

* something around 2 week (migration easy and only few o/p using,
