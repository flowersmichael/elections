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

## Key Links

### Link to Google Slides presentation, including Storyboard: https://docs.google.com/presentation/d/1E93kYEQFJNGIZQmk9z00w1K3CHVzehhQ3yrYlhuCUcg/edit#slide=id.gd85dd7db60_0_6

### Link to Tableau dashboard:
https://public.tableau.com/profile/jason6879#!/vizhome/SenateRace_16205139382310/Dashboard1?publish=yes

### Link to website:
https://predictsenate.anvil.app/

### Link to web app:
https://share.streamlit.io/hieppham8083/finalproject/main/main.py


## Key Tools

Hiep wrote a Python script that, in just one click:
1. Reads in csv files, 
2. Analyzes the file, 
3. Processes everything, 
4. Saves the results in pdf file, and finally 
5. Merge all pdf files into ONE pdf file for easy review. 

For your reference:

[AutoTest.ipynb](../hiep/AutoTest.ipynb),
[AutoTest.py](../hiep/AutoTest.py), and
[AutoTest Video](../hiep/AutoTest.m4v)
[Elections Result PDF File](../hiep/Results_Elections.pdf)

Hiep also wrote a Python script to store data to SQL_database. This script also creates an ERD with relationships.

For your reference:

[Dataframe_to_sql.ipynb](../hiep/Dataframe_to_sql.ipynb) and 
[Video](../hiep/SQL_database.m4v)

[ERD](../hiep/ERD.png) and 
[Video](../hiep/SQL_ERD.m4v)



## Machine Learning Results


### Previous U.S. Senate Election Results Model
Hiep also built Machine Learning models that work directly with the data in the SQL database. These models apply Machine Learning to analyze: [senate_dataset.csv](../hiep/Resources/senate_dataset.csv)

Process:
1. First, connect to PostgreSQL Database and read the DataFrame. Refer to test result below:
![alt text](../hiep/senate_from_SQL.png)
  
2. Clean and rescale the data, then apply neural networks model to train model. Refer to:
[senate_model.ipynb](../hiep/senate_model.ipynb)

3. Predict the Senate's total votes for each state, and predict who will win next election.

4. Test the prediction. Refer to the following:
[senate_prediction.ipynb](../hiep/Senate_prediction.ipynb)
[Video](../hiep/Senate_Prediction.m4v)


### Independent Expenditures Model
Hiep also applied a deep-learning neural networks model to analyze:
[independent_expenditures.csv](../hiep/Resources/independent_expenditures_2004-2020.csv.zip)

Process:
1. First connect to PostgreSQL Database and read the DataFrame. Refer to test result below:
![alt text](../hiep/fec_independent_expenditures_from_SQL.png)

2. Completed data cleaning, then decomposed and rescale the data. Refer to: 
[fec_independent_expenditures.ipynb](../hiep/fec_independent_expenditures_model.ipynb)

3. Use neural networks model with 2 hidden layers to train the model. Refer to test result below:
![alt text](../hiep/independent_expenditures_2020.png)

4. Finally, deploy machine learning model on the website: 
[2022 senate elections predictions](https://group5.anvil.app/)
[WebApp Video](../hiep/WebApp.m4v)


### Turnout Model
Hiep also deployed a deep learning NeuralNetwork model to analyze vote turnout from [Elections Performance Index Dataset](../Hiep_3rd_Segment/Resources/epi.csv) and directly plot all the graphs on the web app. Refer to [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) for details. The model also predicts percentage of vote turn out from [epi.csv](../Hiep_3rd_Segment/Resources/epi.csv). Refer to [EPI_NeuraulNetwork.ipynb](../Hiep_3rd_Segment/Machine_Learning/epi_nn.ipynb) for details.

Process:
1. Read and clean the data:
![alt text](../Hiep_3rd_Segment/Resources/data.png)

2. Exploratory data analysis, calculating the coefficient of determination, and prediction:
![alt text](../Hiep_3rd_Segment/Resources/step.png)
![alt text](../Hiep_3rd_Segment/Resources/step1.png)
![alt text](../Hiep_3rd_Segment/Resources/step2.png)
![alt text](../Hiep_3rd_Segment/Resources/step3.png)

3. Dataset Preparation (Splitting and Scaling)
Input (X): The columns that are inserted into our model will be used to make predictions.
Prediction (Y = vep_turnout): Target variable that will be predicted by the input.
![alt text](../Hiep_3rd_Segment/Resources/stepP.png)
	
4. Using Keras Regressions Model:
The model will run in both train and test data along with calculating the loss function.
![alt text](../Hiep_3rd_Segment/Resources/step8.png)
![alt text](../Hiep_3rd_Segment/Resources/step4.png)
	
5. Evaluation on Test Data and calculate the R²_score to quantify the model’s performance. 
![alt text](../Hiep_3rd_Segment/Resources/step7.png)
![alt text](../Hiep_3rd_Segment/Resources/step5.png)
![alt text](../Hiep_3rd_Segment/Resources/step6.png)
		
*Remark: The RMSE (loss function) is lower for Keras Regression model which shows that our prediction is closer to actual.

		
### Machine Learning Conclusion

The purpose of neural networks is to find a transformation of a data for making a decision. If we had a large number of vote info as input, along with the vote turnout as output, a neural network could be "trained" on these patterns.
 
## Summary
Easily access [Our Website](https://predictsenate.anvil.app/) and [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) from anywhere–computer, tablet, or phone.

Create pie charts, graphs, interactive maps, Deep learning and more with just a few clicks.
