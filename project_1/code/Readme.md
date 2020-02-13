# Problem Statement:
Which state should money be best spent on, to improve SAT participation rates?

# Executive Summary:
The new format for the SAT was released in March 2016. As an employee of the College Board - the organization that administers the SAT - we are a part of a team that tracks statewide participation and recommends where money is best spent to improve SAT participation rates.

We're going to take a look at aggregate SAT and ACT scores and participation rates from each state in the United States. We'll seek to identify trends in the data and combine our data analysis with outside research to identify likely factors influencing participation rates and scores in various states. We will recommend 1 state (California) as the state where money should best be spent on to improve SAT participation rates.

# Contents:
2017 Data Import & Cleaning
2018 Data Import and Cleaning
Exploratory Data Analysis
Data Visualization
Descriptive and Inferential Statistics
Outside Research
Conclusions and Recommendations

# Data Dictionary:
| Feature                                      | Type     | Dataset                               | Description_eg.                  |
| -------------                                | ------------- |-------------                           | -------------
|state|O|ACT/SAT|US state. eg. Alabama
|sat-participation_%-2017|int64|SAT|SAT 2017 participation rate (%). eg. 100
|sat-evidence-based_reading_and_writing-2017|int64|SAT|SAT 2017 scores for evidence-based read&write....
|sat-math-2017|float64|SAT|SAT 2017 scores for math eg. 400
|sat-total-2017|float64|SAT|SAT 2017 sum of scores for evidence-based read...
|act-participation_%-2017|int64|ACT|ACT 2017 participation rate (%). eg. 100
|act-english-2017|float64|ACT|ACT 2017 scores for english. eg. 20
|act-math-2017|float64|ACT|ACT|2017 scores for math. eg. 20
|act-reading-2017|float64|ACT|ACT 2017 scores for reading. eg. 20
|act-science-2017|float64|ACT|ACT 2017 scores for science. eg. 20
|act-composite-2017|float64|ACT|ACT 2017 average scores for english+math+readi...
|sat-participation_%-2018|int64|SAT|SAT 2018 participation rate (%). eg. 100
|sat-evidence-based_reading_and_writing-2018|int64|SAT|SAT 2018 scores for evidence-based read&write....
|sat-math-2018|int64|SAT|SAT 2018 scores for math. eg. 400
|sat-total-2018|int64|SAT|SAT 2018 sum of scores for evidence-based read...
|act-participation_%-2018|int64|ACT|ACT 2018 participation rate (%). eg. 100
|act-composite-2018|float64|ACT|ACT 2018 average scores for english+math+readi..

# Conclusions and Recommendations
Answers:

[Focusing only on SAT]

## Key takeaways across 2017-2018

### Overall...
1. Highest SAT participation rates: Consistently Michigan, Deleware, Connecticut (all 100%)
2. Lowest SAT participation rates: Consistently North Dakota, Iowa, Mississippi, Nebraska, South Dakota, Wisconsin, Wyoming, Kansas (all 2-4%).
3. Largest rise in SAT participation rates: Illinois, Colorado.
4. Largest drop in SAT participation rates: Florida.
5. SAT Participation rates tend to be inversely correlated to SAT Total scores (from sns.heatmap, 2017: -0.86, 2018: -0.84).

### For the 3 states with largest number of students who didn't take SATs (=largest untapped potential)-1st California, 2nd Texas, 3rd Ohio...

6. Untapped potential (number of students who didn't take the SATs in both years) in 3 states, for 2017 & 2018: California (1773k, 199k), Texas (124k, 115k), then Ohio (108k, 101k). Note that the smallest untapped potential was in the hundreds, ~118
7. Good increase in SAT total, reading, math scores from 2017 to 2018, for California and then Texas (yay we can ride on this momentum!). But sizeable drops for Ohio (probably should give up on Ohio).
8. Slight increase in SAT participation rates for California and then Texas (again yay for us, ride on momentum!), but a drop for Ohio (sigh...should we give it up?)
9. Slight drop in ACT participation rates for California (yay for us!), no change for Texas, and sharp increase for Ohio (maybe we should just give Ohio up) 

## Recommendations...

1. From Key Takeaway 6-9, invest more marketing/training efforts on the states with the largest untapped potential, and with potential for higher SAT participation rates. California would be the best due to their rising SAT participation rates, and dropping ACT participation rates.
2. From Key Takeaways 1 & 3, these states did well for us, hence we could look at what we have been doing there, and replicate those efforts in California. eg. offer subsidised/free SAT tests, like in Colorado? (as verified here: https://magoosh.com/hs/sat/2017/states-provide-sat-free/)
3. We could support the students in California, to improve their math and verbal/reading abilities, so as to raise their scores, and hence confidence levels, and hence their SAT participation rates. But for impartiality, it might not be good to do so

## Additional data that would be desired...

1. Constituent scores for ACT 2018, to compare against other years better
2. Each State's popuation pyramids, and projected birth rates, to get a short and long term estimation of college-age ready students, so that we can focus our longer-term efforts on these states
3. More SAT, ACT scores across more years, to have a better view of the overall trend over the years
4. Test-takers' ages, since there has been a trend of non-college-ready-age students taking the tests, which skews the results (https://www.wsj.com/articles/sat-scores-fall-as-more-students-take-the-test-11569297660)
5. State funding in education across the years, to see how that has affected SAT & ACT scores, and perhaps participation rates (likely is true, as seen from "Both states have relatively large education budgets. Massachusetts (home state of PrepScholar) and Connecticut have some of the best colleges in the USA, and both have a strong emphasis on high school education and test prep". Link:https://blog.prepscholar.com/average-sat-and-act-scores-by-stated-adjusted-for-participation-rate)
6. Socio-economical/household income/crime rate data, to see how effective the newly introduced 'adversity score' (link: https://www.edsurge.com/news/2019-07-31-don-t-call-them-test-companies-how-the-college-board-and-act-have-shifted-focus. goal is to help college admissions officials put an applicant’s SAT score in perspective by showing whether the students come from a place of hardship or relative advantage), has helped to level the playing field for disadvantaged students in certain States, and to see whether this has been effective in incentivising SAT participation and raise participation rates in some of those states.