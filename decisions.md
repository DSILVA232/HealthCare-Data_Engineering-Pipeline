 do data profiling with polar rather than pandas , reason being pandas does row wise operation but polar does column based operations , pandas is fine for small datasets but will strugglue with large ,  since our data profiling is all column based operations  even tho is a small dataset will user polar 


 decided to seperate sql folder files as follows initialization will have boot_strap which will have 1 file that will need to be ran once because of that that file contains only the following Roles
-Warehouse
-Database
-Schemas
-Permissions
Things taht rarely or sometimes change , this being a once a year file means they wont change .
the ingestion folder will contain the table creation of the raw table as well as ingestions scripts to connect snowflake to google cloud bucket and retrive the raw data , i will also create dbt folder that will hold stuff for that but will decide when i get there the structure for that 



comand to RESET gx folder inside cotnaienr rm -rf /opt/airflow/health_care_project/gx_context/gx/*, its usfeull if set up was ran once wrong
just use this and run set up again, it will save a lot of headdache