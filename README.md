## Third Segment Project Deliverable
- Deploy machine learning model to the website for predicting the total votes and who will win the elections, also created the dashboard visualization for elections test results. Refer to [Our Website](https://predictsenate.anvil.app/) for details.
- Furthermore, deploy deep learning neural network model to analyze total votes of Senate dataset, and directly plot all the graphs on the web app. Refer to [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) for details.

## Challenge
- Deep learning step by step to predict percentage of vote turn out from [Elections Performance Index Dataset](../Hiep_3rd_Segment/Resources/epi.csv).Refer to [EPI_NeuraulNetwork.ipynb](../Hiep_3rd_Segment/Machine_Learning/epi_nn.ipynb) for details.
	- Step 1: Read the data:
	![alt text](../Hiep_3rd_Segment/Resources/data.png)
	- Step 1: Exploratory Data Analysis, calculate the coefficient of determination, and Predict:
	![alt text](../Hiep_3rd_Segment/Resources/step.png)
	![alt text](../Hiep_3rd_Segment/Resources/step1.png)
	![alt text](../Hiep_3rd_Segment/Resources/step2.png)
	![alt text](../Hiep_3rd_Segment/Resources/step3.png)
	- Step 2: Dataset Preparation (Splitting and Scaling)
		- Input (X): The columns that are inserted into our model will be used to make predictions.
		- Prediction (y = vep_turnout): Target variable that will be predicted by the input.
		![alt text](../Hiep_3rd_Segment/Resources/stepP.png
	- Step 3: Using Keras Regressions Model
		- The model will run in both train and test data along with calculating the loss function.
		![alt text](../Hiep_3rd_Segment/Resources/step8.png)
		![alt text](../Hiep_3rd_Segment/Resources/step4.png)
	- Step 4: Evaluation on Test Data and calculate the R²_score to quantify the model’s performance. 
		![alt text](../Hiep_3rd_Segment/Resources/step7.png)
		![alt text](../Hiep_3rd_Segment/Resources/step5.png)
		![alt text](../Hiep_3rd_Segment/Resources/step6.png)
		
	#### Remark: The RMSE (loss function) is lower for Keras Regression model which shows that our prediction is closer to actual.
		
	### Conclusion: The purpose of neural networks is to find a transformation of a data for making a decision. if we had a large number of vote info as input, along with the vote turnout as output, a neural network could be "trained" on these patterns.
 
## Summary
  - Easily access [Our Website](https://predictsenate.anvil.app/) and [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) from anywhere–computer, tablet, or phone.
  - Create pie charts, graphs, interactive maps, Deep learning and more with just a few clicks.
	
  
