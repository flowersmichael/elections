--Senate data/ election performance joins
--Joined on LOWER state names to help keep everything in same syntax
SELECT s.year, 
	   state, 
	   office, 
	   district, 
	   candidate, 
	   candidatevotes, 
	   totalvotes,
	   pct_reg_of_vep_vrs,
	   vep_turnout
FROM senate_data AS s
LEFT JOIN election_performace_indicators AS e 
ON LOWER(e.state_fips) = LOWER(s.state)

--Aggregating the senate_data table in a WITH subquery to get in the same table structure as election_performace_indicators
WITH senate_agg AS (
SELECT year,
	   state,
	   party_simplified,
	   COUNT(candidate) AS candidates,
	   SUM(candidatevotes) AS candidatevotes,
	   MAX(totalvotes) AS totalvotes
FROM senate_data
GROUP BY year,
	     state,
	     party_simplified
ORDER BY year, state)

SELECT s.year, 
	   state,  
	   party_simplified, 
	   candidates, 
	   candidatevotes, 
	   totalvotes,
	   pct_reg_of_vep_vrs,
	   vep_turnout
FROM senate_agg AS s
LEFT JOIN election_performace_indicators AS e 
ON LOWER(e.state_fips) = LOWER(s.state)
ORDER BY year, state

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

--CREATE TABLE query
CREATE TABLE Support_Opposition AS (WITH electresults AS (
SELECT state_po,
	   _year,
	   "Results",
	   candidate,
	   party_detailed
FROM senate_model
)

SELECT cand_office_state AS State,
	   report_year AS Year,
	   support_oppose_indicator AS S_or_O,
	   SUM(expenditure_amount) AS expenditure_amount
	   --MAX(CASE WHEN "Results" = 1 THEN 'Win' ELSE 'Lose' END)
FROM fec_independent_expenditures_original AS f
INNER JOIN electresults AS r on state_po = cand_office_state AND _year = report_year 
GROUP BY cand_office_state, S_or_O, year
ORDER BY Cand_office_state, year)