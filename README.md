# KU-Partnership-Database-Analysis
### Access and summarize KU Partnership Database a lot more easier than browsing website by using Python.
### KU Partnership-Database website = https://iad.intaff.ku.ac.th/portal/mou_f02.php

### Database detail. 
  &emsp; -> Name of Partners. (Partnership name) <br />
  &emsp; -> Agreement Name. (Name of MOU) <br />
  &emsp; -> Agreement Level. (University / Facility) <br />
  &emsp; -> Subordinating Unit of KU. (Facility unit name) <br />
  &emsp; -> Effective Date. (MOU agreement start date) <br />
  &emsp; -> Effective Date. (MOU agreement expired date)<br />
  &emsp; -> Duration. (Duration of MOU) <br />
  &emsp; -> Auto - Renewal. (Yes / No)<br />

![image](https://user-images.githubusercontent.com/64496956/231742438-1f514a4c-29fb-48f2-9388-b950207b1a72.png)


### Class feature 
  &emsp; -> Get all parntnership name. <br />
  &emsp; -> Get all data of partnership detail. <br />
  &emsp; -> Get partnership name url and .CSV link <br />
  &emsp; -> Search partnership name for detail on (display to .CSV) . <br />

### Class describe. (ku_scholar)
  #### ku_scholar(url)  <br />
  &emsp;&emsp; -> 1 parameter (url)  <br />
  &emsp;&emsp; -> Define class with url parameter  <br />
  <br />
  &emsp; all_link() <br />
  &emsp;&emsp; -> Show all partnership url link [ list ]  <br />
  <br />
  &emsp; all_name(name) <br />
  &emsp;&emsp; -> Show all partnership name  [ list ]  <br />
  <br />
  &emsp; search_name(name) <br />
  &emsp;&emsp; -> 1 parameter (name)  <br />
  &emsp;&emsp; -> Search and display partnership name that contain character in user input.  [ list ]  <br />
  <br />
  &emsp; search_detail(name) <br />
  &emsp;&emsp; -> 1 parameter (name)  <br />
  &emsp;&emsp; -> Search and display partnership name and detail that parameter contain in database.  [ pandas dataframe ]  <br />
  <br />
  &emsp; list_all() <br />
  &emsp;&emsp; -> Show all partnership name and url link [ pandas dataframe ]  <br />
  <br />
  &emsp; get_url_link(university_name). <br />
  &emsp;&emsp; -> 1 parameter (university_name)   <br />
  &emsp;&emsp; -> Get partnership url link  [ str ]  <br />
  &emsp;&emsp; *** Parameter must be same that contain on all_name(). ***
  <br />
  &emsp; get_csv_link(university_name) <br />
  &emsp;&emsp; -> 1 parameter (university_name)   <br />
  &emsp;&emsp; -> Get partnership csv link  [ str ]  <br />
  &emsp;&emsp; *** Parameter must be same that contain on all_name(). ***
  <br />
  &emsp; get_detail(university_name) <br />
  &emsp;&emsp; -> 1 parameter (university_name)   <br />
  &emsp;&emsp; -> Search and display partnership name and detail.  [ pandas dataframe ]  <br />
  &emsp;&emsp; *** Parameter must be same that contain on database. ***
  <br />
  &emsp; count() <br />
  &emsp;&emsp; -> Show amount of partnership name that contain on database  [ int ]  <br />
  <br />
  

  
