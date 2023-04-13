# KU-Partnership-Database-Analysis
### Access and summarize KU Partnership Database a lot more easier than browsing website by using Python.
### KU Partnership-Database website = https://iad.intaff.ku.ac.th/portal/mou_f02.php

#### Class feature 
  &emsp; -> Get all parntnership name. <br />
  &emsp; -> Get all data of partnership detail. <br />
  &emsp; -> Get partnership name url and .CSV link <br />
  &emsp; -> Search partnership name for detail on (display to .CSV) . <br />

#### Class describe. (ku_scholar)
  #### ku_scholar(url)  <br />
  &emsp;&emsp; -> 1 parameter (url)  <br />
  &emsp;&emsp; -> Define class with url parameter  <br />
  &emsp; all_link() <br />
  &emsp;&emsp; -> Show all partnership url link [ list ]  <br />
  &emsp; all_name(name) <br />
  &emsp;&emsp; -> Show all partnership name  [ list ]  <br />
  &emsp; search_name(name) <br />
  &emsp;&emsp; -> 1 parameter (name)  <br />
  &emsp;&emsp; -> Search and display partnership name that contain character in user input.  [ list ]  <br />
  &emsp; search_detail(name) <br />
  &emsp;&emsp; -> 1 parameter (name)  <br />
  &emsp;&emsp; -> Search and display partnership name and detail that contain character in user input.  [ pandas dataframe ]  <br />
  &emsp; list_all() <br />
  &emsp;&emsp; -> Show all partnership name and url link [ pandas dataframe ]  <br />
  &emsp; get_url_link(university_name). <br />
  &emsp; get_csv_link(university_name) <br />
  &emsp; get_detail(university_name) <br />
  &emsp; count() <br />
  
#### Database detail. 
  &emsp; -> Name of Partners. (Partnership name) <br />
  &emsp; -> Agreement Name. (Name of MOU) <br />
  &emsp; -> Agreement Level. (University / Facility) <br />
  &emsp; -> Subordinating Unit of KU. (Facility unit name) <br />
  &emsp; -> Effective Date. (MOU agreement start date) <br />
  &emsp; -> Effective Date. (MOU agreement expired date)<br />
  &emsp; -> Duration. (Duration of MOU) <br />
  &emsp; -> Auto - Renewal. (Yes / No)<br />
  
