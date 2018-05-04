1. Assumptions: a) Uses MySQL b) Install MySQL python SDK
2. Install: make install
   a) creates database connection, reads and installs the data
   b) calculates nearest neighbour per genome_id using kd-tree algorithm combined min dist search
3. Use Cases: src/lib/searchutils.py
   a) search by name (prefix/suffix/substring/exact match)
   b) search nearest neighbour (pre-computed using kd-trees)
4. Check logs
   a) run_log.log: execution log
   b) error_log.log: error log
   c) check for implementation: src/lib/logger.py
5. DB layer
   check src/lib/dbutils.py: python interface built via python mysql sdk
   a) create database
   b) deploy tables
   c) inserts into tables
   d) queries tables and returns data in json format
   e) check table definitions: resource/definition.sql
6. Handling scalability
   a) Since we are pre-calculating our search, querying and getting data is faster
   b) We would expect a monitoring job to keep inserting and pre-computing for faster search
   c) We use kd-tree implementation for faster nearest neighbour computation (src/lib/kd.py)
7. Data Parsing
   a) We are parsing data using two files, city file and shape file
   b) Once parsed the data is combined together to be stored in primer normalized form
8. Few more ideas on implementation
   - Use elastic cache for storing data and doing name based search
   - We can store KD tree information in db and later retrieve the tree to avoid computation always


