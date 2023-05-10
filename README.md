# Team Process Mapping Take-Home Task: Shruti Agarwal.

Goal: In this pre-test, you will first read brief selections from two social science papers (Step 1). You will then go through an end-to-end implementation of a feature and apply it to a dataset of team conversations (Step 2). Finally, you will write a reflection on how well you think this feature extractor performed on the data, as well as how well it performs in operationalizing social science constructs (Step 3).

The idea behind this task is to give you a flavor of the scope of our work — to show how we take inspiration from social science, then apply these ideas in a computational way.

Please write your reflection in this README document.

## 1. High-Level Questions
1a. Which dataset did you choose?

> Both! Mainly focused on CSOP dataset. 

1b. What method(s) did you choose? In 1-2 sentences each, describe your sentiment analysis method(s).

> 
"Twitter-roBERTa-base for Sentiment Analysis" HuggingFace sentiment analysis method (provided in writeup): This sentiment analysis method classifies the levels of positive, neutral, and negative a particular string of text is, with frequencies ranging from 0-1. This helps rate the relative tone (on a scale of positivity) of each message sent between subjects. 

"Emotion English DistilRoBERTa-base" HuggingFace sentiment analysis method: This sentiment analysis method calculates the frequency distribution of 7 emotions of a particular string of text, including anger, disgust, fear, joy, neutral, sadness, and surprise. Same as before, each emotion is given a rating between 0-1, which all add to 1. For every instance of the dataset, this method determines the emotion with the highest frequency (i.e. which emotion is "felt the strongest"), and labels the text with that emotion in the "emotion" column. 


1c. Does your method capture any of the ideas from Troth et al. and West et al.? If so, which ones?

>  Yes, they do! Troth et al. supports the idea that heightened emotional awareness and management serve to enhance team interactions, as it lends individuals with an increased air of rationale. These individuals hold back on immediate reactions, which helps resolve team conflict productively without emotional escalation. By implementing my second sentiment analysis method, I was able to go beyond the ternary pos/neu/neg analysis and classify messages with emotions themselves, which have more robust implications. This categorization can help pinpoint how often strong emotions (i.e. disgust, surprise, anger) were experienced in a given conversation, which in turn can help us evaluate the levels of emotional management within the teams, as stronger emotions suggest instability in the team's interactions. We can also study this in the context of different focal tasks, which is another important component of this research, which can help us understand if emotional awareness/management are employed to varying degrees depending on the situation at hand. 

The first sentiment analysis method captures ideas from West et al. These authors assert that teams with higher levels of positive organizational behavior (POB) capacities tend to have greater team satisfaction, cooperation, cohesion, and performance. Out of the three critical variables of interest, self efficacy, optimism, and resilience, our sentiment analysis hones in on optimism. As we are rating how "positive" each message is in a given conversation, we can aggregate this analysis over entire conversations, which can lend us more insight to whether there exists a correlation between optimism and team performace. The more positive the teams are, the more optimistic they tend to be, which in turn implies more active team engagement, motivation, and excitement for the task at hand. An additional simple feature we could implement at the conversation level, pertaining to this optimism factor, would be to simply count how many messages were sent over the platform in any given conversation; this would lend us more insight as to whether or not there's a relationship between positivity/optimism, and active team engagement. This, in essence, would serve to directly test West et al.'s hypothesis. 

1d. Compared to how Troth et al. and West et al. measured positivity, what are some strengths and weaknesses of your approach?

> quite binary, because we are using pretrained models, we aren't getting the highest levels of personalization in our analysis, but ML models take months to curate, so given our resources this is as good as it gets essentially
strengths - using two metrics (pos/neg/neu) (emotions) both of which we can cross check with each other (positive comments should not have an emotional label of anger) which can help us narrow down how we are generating results and pinpoint our accuracy. 


## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up your output CSV and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

> [YOUR ANSWER]

2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

> [YOUR ANSWER]

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

> [YOUR ANSWER]

2d. Given the nature of these datasets, what challenges do you anticipate that you may encounter during evaluation? How would you go about resolving them?

> [YOUR ANSWER]

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

> 12-13 hours. 

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

> [YOUR ANSWER]
Great experience, learned a lot about machine learning algorithms, parallellization, as well as the social science concepts encompassing the project. I was impressed by how quickly I was able to absorb the material, and it makes me excited for future projects I may encounter. 
Began the project doing the readings, which help frame the scope of the task. As I got my project started, however, I ran into various bugs upon just importing the code into my VSCode environment and running it.I interfaced with Emily during the process, and was able to understand a bit more about how the mechanics of the code work, which helped me debug the error and get a much better handle on how the program worked. 
Implementing the sentiment analysis methods were relatively straightforward, as it really was a research/practical skills task as opposed to a programming task. Trying to figure out what was already out there, and incorporate it fittingly into this task was interesting to think about. Figuring out how to utilize multiple cores on my system definitely was a more programming-oriented task

- talk about how both datasets operate differently, even though using same sentiment analysis methods for both, acknowledging that they will come into better use for the CSOP dataset than the Juries dataset, simply because of the empirical study done before and in the original writeup