# U.S. Senate Cammpaign Spending Analysis

## Topic

For our final group project, we are examining the relationship between how much money is spent by United States Senate campaigns, how the campaigns spend their money, and the success of these campaigns. How and to what extent does money affect elections?

Advertising is the major expense of political campaigns, with recent U.S. Senate campaigns spending roughly 40% of funds on ads. Within this realm of political advertising, political donations can be classified as either "hard money" or "soft money" contributions.

Hard money comes from political donations that are regulated by law by the Federal Election Commission, versus "soft money" that is donated in such a way that leaves the contribution unregulated. Soft money donations can be used for "party building" activities, but these funds cannot be used to tell voters which candidates to vote for. Hard money contributions, on the other hand, are spent on ads that either directly support or oppose a specific candidate.

For the purposes of this project, we are strictly concerned with "hard money" political donations.

When evaluating the success of a Senate campaign, we are primarily concerned with whether or not the Senate candidates win their campaigns, but also interested in how well the candidates do relative to expectations.

We also will look at the upcoming Senate elections in 2022, specifically the subset of elections that are expected to be competitive, and using our machine-learning model we will predict winners based on how much *and how* money is spent.

## Reason for Interest

In recent years, U.S. federal election campaign spending has exploded. In 2020, [nearly $14 billion](https://graphics.reuters.com/USA-ELECTION/SENATE-FUNDRAISING/yxmvjeyjkpr/) was spent across the House, Senate, and Presidential races. This is roughly double the amount spent on the previous presidential election cycle in 2016.

While this influx of cash gives campaigns the flexibility to spend in ways and amounts previously unavailable, it's also resulted in a campaign finance "arms race" where the opposing candidates often have the same flexibility. It remains critical for campaigns to allocate resources wisely.

So, we want to examine not only to what degree campaign spending influences election outcomes, but also what types of spending are most effective. In particular we are looking closely at support ads versus opposition ads.


## Data Sources

We rely primarily on four general data sources for the project.

The first source is titled [U.S. Senate 1976-2020](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PEJ5QU), from MIT Election Data and Science Lab. This dataset shows state-level returns for U.S. Senate elections from 1976-2020.

Our second dataset is Federal Election Commission (FEC) data via [Kaggle](https://www.kaggle.com/fec/independent-political-ad-spending). This dataset shows campaign spending for U.S. Senate, House of Representatives, and Presidential elections between 2002-2016.

Our third dataset is state-level demographic data. We use this information to identify and compare states with similar electorate profiles.

Our final dataset is from the Elections Performance Index. The Elections Performance Index provides a "non-partisan, objective measure of how well each state is faring in managing national elections." The EPI uses seventeen indicators to evaluate election administration at the state level. While every indicator sheds light on a different aspect of each state's unique profile, voter turnout is a measure of "civic participation that many people believe best gauges the health of the electoral process."

We hypothesize that focused campaign spending on competitive races in states with turnout levels that, relative to other states, show room for significant improvement, is money well spent.


## Questions to Answer

How much does each additional dollar spent by campaigns relative to other campaigns impact the candidate's win probability?

What is the optimal asset allocation of campaign dollars in terms of spending categories?

Does this asset allocation prescription vary by subgroups of U.S. states with similar demographic profiles?

Given a baseline expectation of candidate performance, how well can we predict candidate performance using our independent variables?


## Team Communication

Outside of the Tuesday and Thursday night classes, we will meet over video conference at least once per week to coordinate and plan.

Additionally, we will be communicating regularly via our group Slack channel, and group text as well.

## Outline

▾ □ Elections Analysis
    ▾ □ Questions to Answer
        ▾ □ How much does a vote "cost”?
            ▾ □ Build a curve?
                - □ Dollars spent (x-axis) vs win probability (y-axis)
                - □ “That matches up with other research suggesting that advertising can have a serious effect on how people vote if the candidate buying the ads is not already well-known and if the election at hand is less predetermined along partisan lines.
Basically, said Darrell West, vice president and director of governance studies at the Brookings Institution, advertising is useful for making voters aware that a candidate or an issue exists at all. Once you’ve established that you’re real and that enough people are paying attention to you to give you a decent chunk of money, you reach a point of diminishing returns”
            - □ Only look at competitive states
            - □ Varies depending on incumbency
            - □ 
        ▾ □ Support or opposition ads?
            - □ Top-line ratio of all campaigns (60/40? 80/20? etc), maybe subgroup ratios too
            - □ Support ads = more turnout? Maybe limit to that?
            - □ When are opposition ads most effective?
        ▾ □ How do we integrate demographics?
            - □ Possible hypothesis: younger and more demographically diverse states have lower turnout and are ripe for increased turnout
            - □ 
    ▾ □ Datasets
        - □ Senate race results 1976-2020
        - □ State-level demographics
        - □ County-level demographics (maybe for one or a few states?)
        ▾ □ Elections Performance Index
            ▾ □ Can use for turnout data at least (2008-2018)
                - □ Three presidential elections (08, 12, 16) and three midterms (10, 14, 18)
    ▾ □ Predict winners based on ad money spent
        - □ Machine-learning model
    ▾ □ Dashboard
        - □ Maybe input spending and predict turnout and results

