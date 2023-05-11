# Team Process Mapping Take-Home Task: Shruti Agarwal.

Goal: In this pre-test, you will first read brief selections from two social science papers (Step 1). You will then go through an end-to-end implementation of a feature and apply it to a dataset of team conversations (Step 2). Finally, you will write a reflection on how well you think this feature extractor performed on the data, as well as how well it performs in operationalizing social science constructs (Step 3).

The idea behind this task is to give you a flavor of the scope of our work — to show how we take inspiration from social science, then apply these ideas in a computational way.

Please write your reflection in this README document.

## 1. High-Level Questions
1a. Which dataset did you choose?

> Both! Mainly focused on CSOP dataset. 

1b. What method(s) did you choose? In 1-2 sentences each, describe your sentiment analysis method(s).

> "Twitter-roBERTa-base for Sentiment Analysis" HuggingFace sentiment analysis method (provided in writeup): This sentiment analysis method classifies the levels of positive, neutral, and negative a particular string of text is, with frequencies ranging from 0-1. This helps rate the relative tone (on a scale of positivity) of each message sent between subjects. 

> "Emotion English DistilRoBERTa-base" HuggingFace sentiment analysis method: This sentiment analysis method calculates the frequency distribution of 7 emotions of a particular string of text, including anger, disgust, fear, joy, neutral, sadness, and surprise. Same as before, each emotion is given a rating between 0-1, which all add to 1. For every instance of the dataset, this method determines the emotion with the highest frequency (i.e. which emotion is "felt the strongest"), and labels the text with that emotion in the "emotion" column. 


1c. Does your method capture any of the ideas from Troth et al. and West et al.? If so, which ones?

>  Yes, they do! Troth et al. supports the idea that heightened emotional awareness and management serve to enhance team interactions, as it lends individuals with an increased air of rationale. These individuals hold back on immediate reactions, which helps resolve team conflict productively without emotional escalation. By implementing my second sentiment analysis method, I was able to go beyond the ternary pos/neu/neg analysis and classify messages with emotions themselves, which have more robust implications. This categorization can help pinpoint how often strong emotions (i.e. disgust, surprise, anger) were experienced in a given conversation, which in turn can help us evaluate the levels of emotional management within the teams, as stronger emotions suggest instability in the team's interactions. We can also study this in the context of different focal tasks, which is another important component of this research, which can help us understand if emotional awareness/management are employed to varying degrees depending on the situation at hand. 

> The first sentiment analysis method captures ideas from West et al. These authors assert that teams with higher levels of positive organizational behavior (POB) capacities tend to have greater team satisfaction, cooperation, cohesion, and performance. Out of the three critical variables of interest, self efficacy, optimism, and resilience, our sentiment analysis hones in on optimism. As we are rating how "positive" each message is in a given conversation, we can aggregate this analysis over entire conversations, which can lend us more insight to whether there exists a correlation between optimism and team performace. The more positive the teams are, the more optimistic they tend to be, which in turn implies more active team engagement, motivation, and excitement for the task at hand. An additional simple feature we could implement at the conversation level, pertaining to this optimism factor, would be to simply count how many messages were sent over the platform in any given conversation; this would lend us more insight as to whether or not there's a relationship between positivity/optimism, and active team engagement. This, in essence, would serve to directly test West et al.'s hypothesis. 

1d. Compared to how Troth et al. and West et al. measured positivity, what are some strengths and weaknesses of your approach?

> A definite strength in my approach is using two metrics for positivity, which include the ternary pos/neu/neg rating as well as an emotional classification. Because we have two different labels for each message, we can cross check these results with each other to ensure we're getting as accurate results as possible (i.e. comments with a high positive rating should not have an emotional label of anger). This can help us narrow down which messages are being rated correctly vs. incorrectly, and we can further use this information to fine tune the ML model and get more accurate results that frame the specific focal task we're working on. Additionally, both these sets of authors emphasize how either (A) managing your teammates' emotions or (B) having greater POB capacities are necessary for increased performance, as they improve teamwork and coordination. My methods do a good job in detecting how positive/optimistic team mambers are and how often strong emotions are experienced, which gives us a good handle on both (A) and (B).

A potential weakness of my approach is using pretrained ML models from HuggingFace, as it discounts personalization in the analysis. Because ML models take many weeks to build and make accurate, the best course of action is to observe how the messages behave in this pretrained environment, and fine tune the model based off of the inaccuracies to deplete any lack of precision. Another weakness is not considering the other POB variables (self efficacy and resilience) as directly as optimism, but those are fairly subjective capacities that would require higher level analysis to quantify. 


## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up your output CSV and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

> Yes, most of the values make sense intuitively, especially the pos/neu/neg ratings. All the messages I would perceive as positive are given a higher positive score, and similarly with the neutral/negative scores. The RoBERTa model was pretrained on tweets, which are similar to our messages, as they are also delivered casually over a virtual network, so the accurate tone mapping checks out. The emotion sentiment analysis method also does a good job, but I do notice some inaccuracies, which suggest there may need to be more fine-tuning done on this front. For example, one message says "purple is messing it up on purpose", which is given a high negative rating of 0.85 (as expected), but is given an emotion label of "neutral", which is inaccurate. 

2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

> 

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

> [YOUR ANSWER]

2d. Given the nature of these datasets, what challenges do you anticipate that you may encounter during evaluation? How would you go about resolving them?

> [YOUR ANSWER]

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

> ~17 hours. 

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

> 
Overall, this task was a great experience! It exposed me to several novel ideas/concepts, including machine learning implementation techniques, parallelization, and social science literature. The bare skeleton of the task itself is minimally complex, but going one step further and connecting the work to the psychological chassis of the research requires far greater depth that I'm grateful I pushed myself to explore. 

I originally approached this task sequentially, starting with the readings, which helped contextualize the project. However, once I imported the stub code into my environment, I found that I was encountering a KeyError when running my project; I decided to comment out this code, as it pertained to conversation level features, and revisited it later after having interfaced with Emily, who educated me a bit on the mechanics of the code. This propelled me into a deep dive analysis of how the code operated and (through some syntax lookup) helped me debug the error. In retrospect, this challenge gave me a much better handle on how the program worked/transfered dataframes and made future parallelization implementation much smoother.  

Implementing the sentiment analysis methods were relatively straightforward, as it really was a research/practical skills task as opposed to a programming task. Searching for methods that would generate useful information about the datasets was an interesting activity that required me to revisit the readings and fully understand the needs/goals of this research. 

The last big component of this work was figuring out how to parallelize the code. Even on the CSOP dataset, my code was taking 6 minutes to fully process without parallelization, so I eventually made it a priority to incorporate this feature into my program. Researching online gave me several different avenues I could take, a lot of which I tried (swifter, Parallel Pandas, pandarallel) because they seemed simpler to implement, but ended up not working because our parallelization ran on string text. This led me to research more complex implementations using maps and Pool, which in turn forced me to understand how the sentiment analysis methods were actually being applied to the dataframe. Because I have two sentiment analysis methods, I had to accomodate this additional complexity in my parallelization. Once I found the right resources and correctly implemented it, it cut my runtime for CSOP down to 2.5 minutes, allowing me to also run this code on the Juries dataset!

If I had more time with this data, there is a lot more I'd hope to implement. The previous research done on the CSOP dataset suggested the average word count and number of words spoken by the most active participant were telling factors of the team's performance. When evaluating this data at the conversation level, we could quantify how much each person talked in a given conversation, and compare this data to that of the Juries data, for which a different (greater) level of even collaboration is optimal. Another method we could implement is evaluating the cohesion of the teams by implementing a simple, VADER-esque "bag of words" approach. We can determine how "team-oriented" vs individualistic a group is based on the frequency of "team" words spoken, (i.e. we, us) vs individual words spoken (i.e. I, me, my, you). This can be analyzed in the context of both CSOP and Juries datasets to see which focal tasks requires higher displays of team morale and pride. Another potential improvement could be analyzing the length of conversation (if it is not fixed by the experiment), as well as the density of messages across the length of the conversation. We can evaluate how time affects productivity depends on the task; for example, do teams lose productivity/motivation with time, or does the length of time allow people to get more comfortable which each other and then produce more fruitful results? This answer could vary depending on the task, so it would be interesting to analyze/think about. Overall, because this take home task worked with only chat-level features, there wasn't much bandwidth in terms of analyzing holistic conversations and relationships between speakers; accounting for this additional factor opens up endless avenues for analysis. 