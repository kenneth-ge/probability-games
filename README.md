# Probability Games
## Question: given that we know the weights on a weighted coin, how good can we get at guessing the outcome?

# Inspiration
I was reading an article today that talked about how people were really bad at guessing a certain binary thing (won't go into the details of what that thing is lol). In fact, the article specifically said that people did no better than a coin flip. 

This was interesting to me, because the distribution was actually 9-1 -- meaning 90% of the data points fit one category, and 10% fit the other. 

This got me thinking, and I had two questions in mind:
* This seems counterintuitive; why would a coin flip be correct 50% of the time when the distribution itself was 90-10?
* Can we do better by guessing along the distribution? If so, what is the best we can do given that the only thing we know is the probability of getting either outcome?

The first question was answered pretty easily: yes, indeed a coin flip is still correct 50% of the itme no matter what the distirbution looks like. We can prove this by noticing that our probability of being correct = 0.5 * p + (1 - 0.5) * (1 - p) = 0.5. 

The second question was more interesting. If we guess along the distribution (i.e. guessing the 90% outcome 90% of the time, and the 10% outcome 10% of the time), the total probability that our guess matches the data is p * p + (1 - p) * (1 - p), assuming p is the chance that we get heads from the distribution. 

But, we can do even better by simply guessing the more likely outcome. In other words, assuming p is the more likely probability out of the two, we can be right with a probability of p if we simply always guess the more likely outcome. This is because p * 1 + (1 - p) * 0 = p. We can prove that this is better than our guess above -- this is left as an exercise to the reader. 

But, is this the best we can do? If so, why?

# The Game!
In this repository, you will see a file called ``user_defined.py``. This is where you get to define your own function, f(p), to try to see if you can beat the approach described above! Basically, given that p is the probability of the more likely outcome, you create a function to return the chance that you choose this outcome. I.e., the probability that your answer agrees with the weighted coin is p * f(p) + (1 - p) * (1 - f(p)). And, given this, you want to see if you can somehow maximize this function to beat f(p) = 1 at *any* probability p -- even if it doesn't beat f(p) = 1 for all p ∈ [0.5, 1]. 

If you find a function ``f(p)`` that can beat our current best approach (just choosing the more likely outcome, i.e. f(p) = 1), pull requests are certainly welcome! My mind will be blown, and you will forever have the honor of having rocked my world. 
