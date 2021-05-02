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