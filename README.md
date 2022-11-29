# Probability Games
## Question: given that we know the weights on a weighted coin, how good can we get at guessing the outcome? [UPDATE: the answer is solved! Read below to find out more.]

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

# The Answer
Alright, so it turns out we actually have an answer! And the answer is... f(p) = 1 is the best we can do. Here's an explanation/proof as to why by Luke Reynolds: 

* WLOG, assume the it’s more likely to return true than false. Ie p>=0.5 
* Then by definition, if you predict “true” then you’ll be right with probability p >= 0.5
* And if you guys “false” you’ll be right with probability p<= 0.5
* So always better (if not equal) to choose true

And here's my version/formalization of this proof:
* Let f(p) = 1 - x. This way, we can reframe the question so that we start by always guessing the more likely outcome, and we simply adjust this probability by x. 
* So, that means our new probability of being right is p * (1 - x) + (1 - p) * x. 
* This means we've reduced our total probability of being right by x * p, but we increase our probability of being right by x * (1 - p). This is compared to f(p) = 1, where our probability of being right is equal to p. Intuitively, this should make sense, but here is some algebra to prove it: our new probability of being right = p * (1 - x) + (1 - p) * x = p - p * x + (1 - p) * x. Subtracting p, we get - p * x + (1 - p) * x. 
* But, we also know that p > 0.5 and therefore (1 - p) < p. So, x * (1 - p) < x * p. 
* So, the tradeoff never works out for us because - p * x + (1 - p) * x < 0. I.e., it is never optimal to make x > 0
* Therefore, f(p) = 1 - 0 = 1 is always optimal. 
* QED

Here's some more commentary/proof from [Ananth Vivekanand](https://github.com/AnanthVivekanand):
* Where x is the weightage of some outcome on the coin, we choose a y to maximize “xy + (1-x)(1-y)” where y represents the probability we choose outcome x
* At x = 0.9, we maximize the expression when y = 1, so optimal strategy is to always choose the most probable outcome
* But something interesting happens when we slide x
* Since the line is “straight”, the value of y that maximizes the expression is either 0 or 1
* This corresponds to always choosing the most probable side
