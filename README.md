# U.S. Senate Campaign Spending Analysis

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

For competitive campaigns, how much does each additional dollar spent by campaigns relative to other campaigns impact the candidate's win probability?

Does this asset allocation prescription vary by subgroups of U.S. states with similar demographic profiles?


## Team Communication

Outside of the Tuesday and Thursday night classes, we will meet over video conference at least once per week to coordinate and plan.

Additionally, we will be communicating regularly via our group Slack channel, and group text as well.

## Outline

![Outline](https://github.com/flowersmichael/elections/blob/mike/Resources/Initial%20Outline.png)

# elections

Link to presentation: https://docs.google.com/presentation/d/1E93kYEQFJNGIZQmk9z00w1K3CHVzehhQ3yrYlhuCUcg/edit#slide=id.gd85dd7db60_0_6

--1. combine demographics, population and voter turnout
-- `All_State_Demographics` table is not working!
WITH demo AS(
SELECT All_State_Demographics.Year,
	   State,
	   Race
FROM postgres.public.All_State_Demographics)

SELECT year,
	   state_fips AS State,
	   vep_turnout
FROM epi AS e
INNER JOIN demo AS d ON d.Year = e.year 
AND d.LOWER(state) = e.LOWER(state) 

--2. opposition or support spending on advertising and victory (i think this would be EPI and FEC data)
WITH electresults AS (
SELECT state_po AS state,
	   _year AS year,
	   senate_model.Results
FROM senate_model
)

SELECT cand_office_state AS State,
	   report_year AS Year,
	   support_oppose_indicator AS S_or_O,
	   SUM(expenditure_amount) AS expenditure_amount,
	   CASE WHEN results = 1 THEN 'Win' ELSE 'Lose' END
FROM fec_independent_expenditures_original AS f
INNER JOIN electresults AS r on _state = cand_office_state AND _year = report_year 
GROUP BY cand_office_state, S_or_O, year
ORDER BY Cand_office_state, year

## Second Segment Project Deliverable
- Wrote another python script that runs through all csv files, analyzes all of them, process everything, then save the results in pdf file, and finally merge all pdf files into ONE pdf file for easily review. Everything is just one click. Refer to [AutoTest.ipynb](../hiep/AutoTest.ipynb), [AutoTest.py](../hiep/AutoTest.py), and [AutoTest Video](../hiep/AutoTest.m4v) for your reference.

## Challenge
- Build/run Machine Learning models where data stays in the database with SQL:
  - Apply machine learning to analyze from [senate_dataset.csv](../hiep/Resources/senate_dataset.csv):
    - First connect to PostgreSQL Database and read the DataFrame. Refer to test result below:
  ![alt text](../hiep/senate_from_SQL.png)
    - Completed data cleaning, rescale data, then apply neural networks model to train model. Refer to [senate_model.ipynb](../hiep/senate_model.ipynb).
    - Also predict the Senate's total votes for each state and predict who will win next election, and finally test the prediction. Refer to [senate_prediction.ipynb](../hiep/Senate_prediction.ipynb) and [Video](../hiep/Senate_Prediction.m4v) for details.
  - Apply deep-learning neural networks model to analyze from [independent_expenditures.csv](../hiep/Resources/independent_expenditures_2004-2020.csv.zip):
    - First connect to PostgreSQL Database and read the DataFrame. Refer to test result below:
  ![alt text](../hiep/fec_independent_expenditures_from_SQL.png)
    - Completed data cleaning, decomposed data, then rescale data. Refer to [fec_independent_expenditures.ipynb](../hiep/fec_independent_expenditures_model.ipynb).
    - Using neural networks model with 2 hidden layers to train the model. Refer to test result below:
  ![alt text](../hiep/independent_expenditures_2020.png)
- Created a SQL database to store data:
  - Wrote a script to store data to SQL_database. Refer to [Dataframe_to_sql.ipynb](../hiep/Dataframe_to_sql.ipynb) and [Video](../hiep/SQL_database.m4v) for details.
  - Also create a ERD with relationships. Refer to [ERD](../hiep/ERD.png) and [Video](../hiep/SQL_ERD.m4v) for details.
 
## Summary
- A single python script that runs through all csv files, analyzes all of them, process everything, and finally merge all test results into ONE pdf file for easily review. Refer to [Elections Result PDF File](../hiep/Results_Elections.pdf) for your reference.
- Here is our Storyboard with details and descriptions on Google Slide(s): [Group 5 Storyboard](https://docs.google.com/presentation/d/1E93kYEQFJNGIZQmk9z00w1K3CHVzehhQ3yrYlhuCUcg/edit?ts=60823a15#slide=id.gd441bd4197_0_6)
- Finally, deploy machine learning model on the website: [2022 senate elections predictions](https://group5.anvil.app/) & [WebApp Video](../hiep/WebApp.m4v)

## Third Segment Project Deliverable
- Deploy machine learning model to the website for predicting the total votes and who will win the elections, also created the dashboard visualization for elections test results. Refer to [Our Website](https://predictsenate.anvil.app/) for details.
- Furthermore, deploy deep learning NeuralNetwork model to analyze vote turn out from [Elections Performance Index Dataset](../Hiep_3rd_Segment/Resources/epi.csv) and directly plot all the graphs on the web app. Refer to [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) for details.

## Challenge
- Deep learning step by step to predict percentage of vote turn out from [epi.csv](../Hiep_3rd_Segment/Resources/epi.csv). Refer to [EPI_NeuraulNetwork.ipynb](../Hiep_3rd_Segment/Machine_Learning/epi_nn.ipynb) for details.
	- Step 1: Read and clean the data:
	![alt text](../Hiep_3rd_Segment/Resources/data.png)
	- Step 2: Exploratory Data Analysis, calculate the coefficient of determination, and Prediction:
	![alt text](../Hiep_3rd_Segment/Resources/step.png)
	![alt text](../Hiep_3rd_Segment/Resources/step1.png)
	![alt text](../Hiep_3rd_Segment/Resources/step2.png)
	![alt text](../Hiep_3rd_Segment/Resources/step3.png)
	- Step 3: Dataset Preparation (Splitting and Scaling)
		- Input (X): The columns that are inserted into our model will be used to make predictions.
		- Prediction (y = vep_turnout): Target variable that will be predicted by the input.
		![alt text](../Hiep_3rd_Segment/Resources/stepP.png)
	- Step 4: Using Keras Regressions Model
		- The model will run in both train and test data along with calculating the loss function.
		![alt text](../Hiep_3rd_Segment/Resources/step8.png)
		![alt text](../Hiep_3rd_Segment/Resources/step4.png)
	- Step 5: Evaluation on Test Data and calculate the R²_score to quantify the model’s performance. 
		![alt text](../Hiep_3rd_Segment/Resources/step7.png)
		![alt text](../Hiep_3rd_Segment/Resources/step5.png)
		![alt text](../Hiep_3rd_Segment/Resources/step6.png)
		
	#### Remark: The RMSE (loss function) is lower for Keras Regression model which shows that our prediction is closer to actual.
		
	### Conclusion: The purpose of neural networks is to find a transformation of a data for making a decision. if we had a large number of vote info as input, along with the vote turnout as output, a neural network could be "trained" on these patterns.
 
## Summary
  - Easily access [Our Website](https://predictsenate.anvil.app/) and [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) from anywhere–computer, tablet, or phone.
  - Create pie charts, graphs, interactive maps, Deep learning and more with just a few clicks.
	
  

