# Twitter-Streaming-API

I am going to keep punctuation,emoji,hashtags and anything else that comes with raw text and this is my def of ML dataset.this is because emoji and hashtags provide valuable info
on any downstream ML task 

-get raw text 


Connect to the Twitter streaming API and do a keyword search on "Justin Bieber"


keyword match to filter out music. post process go with API
-> keyword match on music with tweets. Its going to be a comb of keyword could be melody, album names, digital release( acroynm using python and use them as filter)

-> emoji,hashtag, album release, drums emoji (eg), drop duplicates, retweets,  

 ************** emoji,hashtag
Filter out all tweets having to do with music(remove music)

Store the tweets into a database of your choosing
                                                          sparksql DB,sql,nosql(tweets)
      Avoid duplicates  -> retweets,
      Produce a count of all tweets consumed ->print(data) 
      Produce a count of unique tweets -> print(data) after removing duplicates


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
