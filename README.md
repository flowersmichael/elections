# elections
## Second Segment Project Deliverable
- Wrote another python script that runs through all csv files, analyzes all of them, process everything, then save the data in pdf file, and finally merge all pdf files into ONE pdf file for easily review. Everything is just one click. Refer to [AutoTest.ipynb](../hiep/AutoTest.ipynb), [AutoTest.py](../hiep/AutoTest.py), and [AutoTest Video](../hiep/AutoTest.m4v) for your reference.

## Challenge
- Apply machine learning to analyze from [senate_dataset.csv](../hiep/Resources/senate_dataset.csv):
  - First completed data cleaning. Refer to [clean_Senate_data.ipynb](../hiep/clean_Senate_data.ipynb).
  - Predict the Senate's total votes for each state and predict who will win next election, and finally test the prediction. Refer to [Video](../hiep/Senate_Prediction.m4v) for details.
- Apply deep-learning neural networks model to analyze from [independent_expenditures.csv](../hiep/Resources/independent_expenditures_2004-2020.csv.zip):
  - Completed data cleaning, decomposed data, then rescale data. Refer to [independent_expenditures.ipynb](../hiep/independent_expenditures.ipynb).
  - Using neural networks model with 2 hidden layers to train the model. Refer to test result below:
  ![alt text](../hiep/independent_expenditures_2020.png) 
  
  ## Summary
  - A single python script that runs through all csv files, analyzes all of them, process everything, and finally merge all test results into ONE pdf file for easily review. Refer to [Elections Result PDF File](../hiep/Results_Elections.pdf) for your reference.
