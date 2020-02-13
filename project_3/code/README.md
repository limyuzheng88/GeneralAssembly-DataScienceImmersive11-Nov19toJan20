## Business Problem
How can we auto-filter out troll posts that don’t belong to the askscience sub-reddit, to save the moderators’ time?

(assesment metric will be by: accuracy, supported by specificity & sensitivity)

## Conclusion

I. Our model (tvec with gridsearch >> selectkbest(chi2) >> best of logreg/multinomialNB/bernoulliNB depending on data of the day), on the whole, works well in classifying posts (using their titles) according to whether it belongs to the r/askscience or the r/jokes subreddit. The accuracy is high (90+%), and the specificity (90+%) and sensitivity (90+%) are both high as well. The r/askscience moderators would be pleased, since this would provide a good first cut filter, to remove troll posts that masquerade as science-related posts.

II. Additionally, given that our 'positive' class is class2 (=r/askscience), we actually want to have both a high sensitivity and a high sensitivity (achieved as mentioned above) - we want to maximise sensitivity via minimizing the wrongful deletion of legitimate science posts (false negatives), AND also maximise specificity via minimizing the wrongful retention of actual troll/joke posts (false positives).

III. Also, each time this series of models is re-trained (which is likely necessary, periodically, so as to keep up with in-trend scientific developments) with refreshed training data, it dynamically updates itself with the best tvec hyperparameters, and the best option from amongst logreg/multinomialNB/bernoulliNB. This makes it a current & dynamic solution for the moderators, because sometimes a different tvec's max_df may work better, or perhaps logreg may work better (vs multinomialNB/bernoulliNB), whenever the training data changes (which happens frequently enough).

IV. For now, the most common words for r/jokes would be 'call', 'whi(ch)', 'man', 'ask', 'say' etc. And the most common words for r/askscience would be 'whi(ch)', 'differ(ent)', 'doe(s)', 'water' etc.

## Limitations, Future work

I. Puns are not well classified. We would expect more misclassifications when there are double-entendres, sarcasm etc, hence perhaps better models like Bert may be required to boost its performance. N-grams may help too.

II. As mentioned earlier, since topics in trend change with time (Higgs Boson was popular earlier, but in future maybe new Tesla car models would be more in-trend), these models would need to be trained often enough, to "keep up with the trends", for accurate classification.