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
	   district,
	   candidate,
	   candidatevotes,
	   totalvotes
FROM senate_data
	   )

SELECT s.year, 
	   state,  
	   district, 
	   candidate, 
	   candidatevotes, 
	   totalvotes,
	   pct_reg_of_vep_vrs,
	   vep_turnout
FROM senate_data AS s
LEFT JOIN election_performace_indicators AS e 
ON LOWER(e.state_fips) = LOWER(s.state)
GROUP BY s.year, state, district, candidate