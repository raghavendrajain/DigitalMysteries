1. The RAW log file is of format "time,userID,action,objName". Run logsTOCSV.py for getting Output: CSV file which omits the "object" information and creates the files for  "time,userID,action".
2. Using the background information of the nature of performers, I create 2 directories as "HighAchievers" and "LowAchievers". The files are placed according to their nature. 

The files names and their status according to performance are

	1. BDB-WC ---> Subjectively lassified as HIGH
	2. CEL-WC--->HIGH
	3. CLE-AW--->HIGH
	4. CLE-OH---> HIGH
	5. DLE-OH---> LOW
	6. ELD-AW--->LOW
	7. ELD-WC--->LOW
	8. GSA-WC--->LOW  
	9. JCB-WC --->Subjectively classified as LOW
	10. RLL-WC---->Subjectively classified as HIGH

3. I read all the 5 CSV files in each directory and replace the 'Actions' by a single alphabet. This nomenclature is based on the EDM paper. 

The Raw Data Contains the following actions 

	1. Moving: M --> MOVE
	2. Enlarge to maximum size: E ---> ENLARGE
	3. Resizing to medium size: N  ---> NORMAL
	4. Shrinking: S --> SHRINK
	5. Rotating: M  ---> ROTATE
	6. Make unions with other data slips: U ---> UPDATE_RELATION
	7. Add data slip to a group: G   ---> ADD_OBJ_TO_GROUP
	8. Remove the data slip from a group: R ---> REMOVE_OBJ_FROM_GROUP

4. 