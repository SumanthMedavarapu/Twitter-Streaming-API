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



### What are the risks involved in building such a pipeline?

* Scalability like 100 tweets every few sec and when would it stop working due to space disk issue
* How long are we storing, some Mechanism to remove tweets older than 90 days
* Way to write code to run faster and better way to store the data than current one we are using.
* Consider Docker, containers

### How would you roll out the pipeline going from proof-of-concept to a production-ready solution?

* Migration to cloud, testing, Validating the Test cases
* Sustain the stress in the peak hours like when high amount of data(tweets) comes at a time
* Refactoring the code to be Modular and reusable, executing the code or containerizing in Docker
* Optimize the Dataflow and the best way to write CRUD to move into other Database
* Deploy using CI/CD so that it is continuous pipeline Development  



### What would a production-ready solution entail that a POC wouldn't? 

* There is Error logging for Prod ready solution and unit solution whereas POC wouldn't.other. 
* If it fails in Production we can Backup, scalability, maintainability, cost etc


### What is the level of effort required to deliver each phase of the solution?
* Inorder to move the solution from Proof of Concept to Production. we need to consider multiple phases like Data Extraction, Transformation, Validation, testing.
* It takes a week for one phase like Unit testing, Error logging for Production ready solution and for Unit solution as well whereas POC wouldn't

### What is your estimated timeline for delivery for a production-ready solution?

* It would take something around 2 week because we need to migrate to cloud which is easy and we are using few outputs and it takes time for testing, vallidation and logging errors for Prod ready solution
