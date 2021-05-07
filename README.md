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
