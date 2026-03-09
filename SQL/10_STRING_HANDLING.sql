# --------------- STRING HANDLING ----------------------------------

SELECT * FROM CUSTOMERS;

1	Ravi Kumar	    ravi.kumar@example.com	    Chennai	    43210
2	Priya Sharma	priya.sharma@example.com	Bangalore	43211
3	Arjun Mehta	    arjun.mehta@example.com	    Hyderabad	43212
4	Meena Gupta	    meena.gupta@example.com	    Mumbai	
5	Karthik Raj	    karthik.raj@example.com	    Chennai	    43213

SELECT CUSTOMER_NAME,
    LENGTH(CUSTOMER_NAME) AS LENGTH_OF_CUSTOMER_NAME,
    UPPER(CUSTOMER_NAME) AS CUSTOMER_NAME_IN_UPPERCASE,
    LOWER(EMAIL) AS EMAIL_IN_LOWERCASE,
    CONCAT(CUSTOMER_NAME,' - ',CITY) AS NAME_CITY_CONCAT,
    SUBSTRING(CUSTOMER_NAME,1,6) AS SUBSTRING_CUSTOMER_NAME_1_6,
    TRIM('     TRIMMING      ') AS TRIMMING,
    LTRIM('     TRIMMING      ') AS LEFT_TRIMMING,
    RTRIM('     TRIMMING      ') AS RIGHT_TRIMMING,
    LPAD(CITY,10,'*') AS LEFT_PADDING,
    RPAD(CITY,10,'#') AS RIGHT_PADDING,
    REPLACE(CUSTOMER_NAME,' ','_') AS CUSTOMER_NAME_REPLACED,
    INSTR(CUSTOMER_NAME,'a') AS POSITION_OF_A,
    LEFT(CUSTOMER_NAME,5) AS FIRST_FIVE_CH_IN_CNAME,
    RIGHT(CUSTOMER_NAME,3) AS LAST_THREE_CH_IN_CNAME,
    REVERSE(CITY) AS REVERSED_CITY,
    FORMAT(PHONE_NUMBER,3) AS FORMATTED_PHONE,
    UPPER(REPLACE(CUSTOMER_NAME,' ','_')) AS INSIDE_UPPER_REPLACED
FROM CUSTOMERS;

CUSTOMER_NAME, LENGTH_OF_CUSTOMER_NAME, CUSTOMER_NAME_IN_UPPERCASE, EMAIL_IN_LOWERCASE,         NAME_CITY_CONCAT,           SUBSTRING_CUSTOMER_NAME_1_6,    TRIMMING,   LEFT_TRIMMING, RIGHT_TRIMMING, LEFT_PADDING,    RIGHT_PADDING,  CUSTOMER_NAME_REPLACED, POSITION_OF_A,  FIRST_FIVE_CH_IN_CNAME, LAST_THREE_CH_IN_CNAME, REVERSED_CITY,  FORMATTED_PHONE,    INSIDE_UPPER_REPLACED

Ravi Kumar	    10	                    RAVI KUMAR	                ravi.kumar@example.com	    Ravi Kumar - Chennai	    Ravi K	                        TRIMMING	TRIMMING      	     TRIMMING	***Chennai	    Chennai###	    Ravi_Kumar	            2	            Ravi 	                mar	                    iannehC	        43,210.000	        RAVI_KUMAR
Priya Sharma	12	                    PRIYA SHARMA	            priya.sharma@example.com	Priya Sharma - Bangalore	Priya 	                        TRIMMING	TRIMMING      	     TRIMMING	*Bangalore	    Bangalore#	    Priya_Sharma	        5	            Priya	                rma	                    erolagnaB	    43,211.000	        PRIYA_SHARMA
Arjun Mehta	    11	                    ARJUN MEHTA	                arjun.mehta@example.com	    Arjun Mehta - Hyderabad	    Arjun 	                        TRIMMING	TRIMMING      	     TRIMMING	*Hyderabad	    Hyderabad#	    Arjun_Mehta	            1	            Arjun	                hta	                    dabaredyH	    43,212.000	        ARJUN_MEHTA
Meena Gupta	    11	                    MEENA GUPTA	                meena.gupta@example.com	    Meena Gupta - Mumbai	    Meena 	                        TRIMMING	TRIMMING      	     TRIMMING	****Mumbai	    Mumbai####	    Meena_Gupta	            5	            Meena	                pta	                    iabmuM		                        MEENA_GUPTA
Karthik Raj	    11	                    KARTHIK RAJ	                karthik.raj@example.com	    Karthik Raj - Chennai	    Karthi	                        TRIMMING	TRIMMING      	     TRIMMING	***Chennai	    Chennai###	    Karthik_Raj	            2	            Karth	                Raj	                    iannehC	        43,213.000	        KARTHIK_RAJ

# -------------------- STRING FUNCTION DEFENITION -------------------------------------------------------------------------------------------

1. LENGTH          -> IT IS USED TO FIND THE LENGTH                          -> LENGTH(FIELD_NAME)                             -> LENGTH(CUSTOMER_NAME) AS LENGTH_OF_CUSTOMER_NAME.
2. UPPER           -> IT IS USED TO CONVERT UPPER CASE                       -> UPPER(FIELD_NAME)                              -> UPPER(CUSTOMER_NAME) AS CUSTOMER_NAME_IN_UPPERCASE.
3. LOWER           -> IT IS USED TO CONVERT LOWER CASE                       -> LOWER(FIELD_NAME)                              -> LOWER(EMAIL) AS EMAIL_IN_LOWERCASE.
4. CONCAT          -> IT IS USED TO CONCAT TWO OR MORE STRING USING DELIMITS -> CONCAT(FIELD_NAME,'DELIMITS',FIELD_NAME,.....) -> CONCAT(CUSTOMER_NAME,' - ',CITY) AS NAME_CITY_CONCAT.
5. SUBSTRING       -> IT IS USED TO EXTRACT SUBSTRING FROM STRING            -> SUBSTRING(FIELD_NAME,START_INDEX,END_INDEX)    -> SUBSTRING(CUSTOMER_NAME,1,6) AS SUBSTRING_CUSTOMER_NAME_1_6.
6. TRIM            -> IT IS USED TO REMOVE UNUSED SPACE FROM STRING          -> TRIM(FIELD_NAME)                               -> TRIM('     TRIMMING      ') AS TRIMMING.
7. LTRIM           -> IT IS USED TO REMOVE LEFT SIDE UNWANTED SPACE          -> LTRIM(FIELD_NAME)                              -> LTRIM('     TRIMMING      ') AS LEFT_TRIMMING.
8. RTRIM           -> IT IS USED TO REMOVE RIGHT SIDE UNWANTED SPACE         -> RTRIM(FIELD_NAME)                              -> RTRIM('     TRIMMING      ') AS RIGHT_TRIMMING.
9. LPAD            -> IT IS USED TO ADJUST PAD AT LEFT SIDE                  -> LPAD(FIELD_NAME,TOTAL_COUNT,'DELIMITS')        -> LPAD(CITY,10,'*') AS LEFT_PADDING.
10. RPAD           -> IT IS USED TO ADJUST PAD AT RIGHT SIDE                 -> RPAD(FIELD_NAME,COUNT,'DELIMITS')              -> RPAD(CITY,10,'#') AS RIGHT_PADDING.
11. REPLACE        -> IT IS USED TO REPLACE OLD TO NEW                       -> REPLACE(FIELD_NAME,OLD,NEW)                    -> REPLACE(CUSTOMER_NAME,' ','_') AS CUSTOMER_NAME_REPLACED.
12. INSTR          -> IT IS USED TO CHECK POSITION (FIRST OCCURENCE)         -> INSTR(FIELD_NAME,'CHARACTER')                  -> INSTR(CUSTOMER_NAME,'a') AS POSITION_OF_A.
13. LEFT           -> IT IS USED TO EXTRACT FIRST POSITIONED CHARACTER       -> LEFT(FIELD_NAME,COUNT)                         -> LEFT(CUSTOMER_NAME,5) AS FIRST_FIVE_CH_IN_CNAME.
14. RIGHT          -> IT IS USED TO EXTRACT LAST POSITIONED CHARACTER        -> RIGHT(FIELD_NAME,COUNT)                        -> RIGHT(CUSTOMER_NAME,3) AS LAST_THREE_CH_IN_CNAME.
15. REVERSE        -> IT IS USED TO REVERSE THE STRING                       -> REVERSE(FIELD_NAME)                            -> REVERSE(CITY) AS REVERSED_CITY.
16. FORMAT         -> IT IS USED TO FORMATTED THE STRING                     -> FORMAT(FIELD_NAME,COUNT)                       -> FORMAT(PHONE_NUMBER,3) AS FORMATTED_PHONE.
17. UPPER(REPLACE) -> WE CAN USE NESTED STRING FUNCTION ALSO LIKE THIS       -> UPPER(REPLACE(CUSTOMER_NAME,' ','_')) AS INSIDE_UPPER_REPLACED.