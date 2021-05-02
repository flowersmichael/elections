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