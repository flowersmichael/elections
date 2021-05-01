# elections
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
- Finally, deploy machine learning model on the website: [2022 senate elections predictions](https://predictsenate.anvil.app/)
