## Third Segment Project Deliverable
- Deploy machine learning model to the website for predicting the total votes and who will win the elections, also created the dashboard visualization for elections test results. Refer to [Our Website](https://predictsenate.anvil.app/) for details.
- Furthermore, deploy deep learning neural network model to analyze total votes of Senate dataset, and directly plot all the graphs on the web app. Refer to [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) for details.

## Challenge
- Deep learning neural network model step by step:
  - Step 1: Exploratory Data Analysis
  ![alt text](../Hiep_3rd_Segment/Resources/step1.png)
  
  - Step 2: Dataset Preparation (Splitting and Scaling)
    - Features (X): The columns that are inserted into our model will be used to make predictions.
    - Prediction (y = totalvotes): Target variable that will be predicted by the features
  - Step 3: Feature scaling will help us see all the variables from the same lens (same scale)
    ![alt text](../Hiep_3rd_Segment//Resources/step3.png)

  - Step 4: Evaluation on Test Data
    ![alt text](../Hiep_3rd_Segment//Resources/step4.png)

  - Step 5: Correlation Matrix
    - The features of interest are the ones with a high correlation with the target variable ‘totalvotes'
    ![alt text](../Hiep_3rd_Segment//Resources/step5.png)
  
  - Step 6: Score the training and the test predictions with r2_score()
    - calculated the r2_score due to R2 is suitable for predicting continuous variable. A higher r-squared indicates a better fit for the model.
    ![alt text](../Hiep_3rd_Segment//Resources/step6.png)
    
    Conclusions: The purpose of neural networks is to find a transformation of a data for making a decision. We built a model that predicts voter preferences. How do we forecast the outcome of an election.
   
 
## Summary
  - Easily access [Our Website](https://predictsenate.anvil.app/) and [Our WebApp](https://share.streamlit.io/hieppham8083/finalproject/main/main.py) from anywhere–computer, tablet, or phone.
  - Create pie charts, graphs, interactive maps, and more with just a few clicks.
	
  
