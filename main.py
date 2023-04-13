import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Settings the warnings to be ignored
warnings.filterwarnings('ignore')




#package สำหรับจัดการ html เรียกว่า BeautifulSoup

def get_soup(url):
    with requests.get(url, verify=False) as r:
        soup = BeautifulSoup(r.text, features='html.parser')
    return soup

class ku_scholar:
  def __init__ (self,url):
    self.head_link = 'https://iad.intaff.ku.ac.th/portal/'
    self.main_link = url
    self.soup = get_soup(self.main_link)
  
  def all_link(self): # get list link of university
    self.link = []
    self.name = []
    for url in self.soup.find_all('tr', class_='row-content'):
      try:
        self.tail_link = (url.find('a').get('href'))
        self.full_link = self.head_link + self.tail_link
        self.link.append(self.full_link)
      except:
        pass
    return self.link
  
  def search_name(self, name):
    self.name_input = name
    self.name_list = self.all_name()
    self.name_list = (list(set(self.name_list))) # convert to set avoid duplicated data
    self.name_list = sorted(self.name_list) # sort alphabet

    self.found_name = []
    self.found = 0

    for name in self.name_list:
      if self.name_input.lower() in name.lower():
          self.found_name.append(name)
          self.found += 1

    if self.found < 1:
        print(f'Error : "{self.name_input}" not found on database.')

    return self.found_name

  def search_detail(self, name): # search_datail (/all for get_all university data)
    self.name_input = name

    if self.name_input == '/all':
      print(f'getting all data.. ({len(self.all_name())} university)')

      self.df_main = self.get_detail(self.all_name()[0])
      
      for i in range(1, len(self.all_name())):
        try:
          self.df_main = self.df_main.append(self.get_detail(self.all_name()[i]))
          print(i ,end=" ")
          if i % 20 == 0:
            print("\n")
        except:
          pass
      
    else:
      self.university_list = self.search_name(name) # get university_name

      if len(self.university_list) > 0:
        if len(self.university_list) == 1:
          return self.get_detail(self.university_list[0])
        else:
          self.df_main = self.get_detail(self.university_list[0])
          for i in range(1, len(self.university_list)):
            try:
              self.df_main = self.df_main.append(self.get_detail(self.university_list[i]))
            except:
              pass
      else:
        print(f'Error ! :{self.name_input} is not found on database.')

    return self.df_main


  def all_name(self): # get list name of university
    self.link = []
    self.name = []
    for url in self.soup.find_all('tr', class_='row-content'):
        #name.append(url.text.strip())
        try:
          self.name.append(str(url.find('a').text.strip()))
        except:
          pass

        # debug duplicated name by add number out of name

    self.count_found = 0

    self.name_duplicated = []
    self.count_duplicated = []

    # Get_duplicated data in list

    for name in self.name:
      self.count_found = self.name.count(name)
      if self.count_found > 1:
        self.name_duplicated.append(name)
        self.count_duplicated.append(self.count_found)

    # Avoid duplicated value
    self.name_duplicated = list(set(self.name_duplicated))
    self.count_duplicated = list(set(self.count_duplicated))

    # rename duplicated item algorihm by using number append
    self.index = 0
    for count_val in (self.count_duplicated):
      for i in range(count_val):
        #self.df.loc[(self.name.index(self.name_duplicated[self.index]),'name')] = str(self.name_duplicated[self.index]) + "_" + str(i+1) # change name on pandas
        self.name[self.name.index(self.name_duplicated[self.index])] = str(self.name_duplicated[self.index]) + "_" + str(i+1) # change name on list_name
      self.index += 1


    return self.name


  def list_all(self): # return as pandas dataframe (name, link)
    self.link = []
    self.name = []
    for url in self.soup.find_all('tr', class_='row-content'):
        #name.append(url.text.strip())
        try:
          self.tail_link = (url.find('a').get('href'))
          self.full_link = self.head_link + self.tail_link
          self.link.append(self.full_link)
          self.name.append(str(url.find('a').text.strip()))
        except:
          pass

    self.df = pd.DataFrame({'name': self.name,'url': self.link})

    # debug duplicated name by add number out of name

    self.count_found = 0

    self.name_duplicated = []
    self.count_duplicated = []

    # Get_duplicated data in list

    for name in self.name:
      self.count_found = self.name.count(name)
      if self.count_found > 1:
        self.name_duplicated.append(name)
        self.count_duplicated.append(self.count_found)

    # Avoid duplicated value
    self.name_duplicated = list(set(self.name_duplicated))
    self.count_duplicated = list(set(self.count_duplicated))

    # rename duplicated item algorihm by using number append
    self.index = 0
    for count_val in (self.count_duplicated):
      for i in range(count_val):
        self.df.loc[(self.name.index(self.name_duplicated[self.index]),'name')] = str(self.name_duplicated[self.index]) + "_" + str(i+1) # change name on pandas
        self.name[self.name.index(self.name_duplicated[self.index])] = str(self.name_duplicated[self.index]) + "_" + str(i+1) # change name on list_name
        #print(name_duplicated[index], i+1)
      self.index += 1

    return self.df

  def get_url_link(self, university_name): # get url university link
    self.url = ""
    self.university_name = university_name
    self.data_list = self.list_all() # get name, url data
    try:
      self.url = (self.data_list.loc[self.data_list['name'] == self.university_name, 'url']).str.cat() # convert to plain str url
      return self.url
    except:
      print(f"Not found '{self.university_name}' in list")
  
  def get_csv_link(self, university_name): # get csv_url university link
    self.university_name = university_name
    self.main_url = self.get_url_link(self.university_name) # get university url
    self.csv_link = ""

    self.soup_csv = get_soup(self.main_url) # get soup from link

    for url in self.soup_csv.find('div', class_='dropdown fixed-position'):
      if 'csv' in str(url):
        self.csv_link = (url.get('href'))
        break

    return (self.head_link + self.csv_link).replace(" ", "%20") # debug space error
  
  def get_detail(self, university_name):
  
    self.university_name = university_name
    self.url_link = self.get_url_link(self.university_name) # get url link
    self.csv_link = self.get_csv_link(self.university_name) # get csv

    #pandas zone (csv)

    self.df = pd.read_csv(self.csv_link)

    self.dic = self.df.to_dict('series') # convert pandas to dict


    # debug error on csv

    for i in range(len(self.dic['No.'])):

      self.dic['Duration'][i] = str(self.dic['Duration'][i]).replace(' ','') # delete space on Duration Column
      if self.dic['MOU Level'][i] == "University": # del subordinating bug on University MOU level
        self.dic['Subordinating Unit of KU'][i] = 'NaN'
        self.dic['Subordinating Unit of Partner'][i] = 'NaN'
      if ("<br>" in str(self.dic['Subordinating Unit of KU'][i])):
        self.dic['Subordinating Unit of KU'][i] = str(self.dic['Subordinating Unit of KU'][i]).replace('<br>', '')


    # get auto - renew data

    self.soup_mou = get_soup(self.url_link)

    self.html_d = str(self.soup_mou.find('tr', class_='row-name')).replace(" ",'_').replace("-","") # convert to str and replace space to underspace
    self.soup_new = BeautifulSoup(self.html_d, 'html.parser') # convert to bs4 type
    #soup_new.text.split() # split_text using space

    self.html_m = str(self.soup_mou.find_all('tr', class_='row-content')).replace(" ",'_').replace('\t','').replace('\n','')
    #html_m


    self.html_m.split('</td>')

    self.pointer = False # Found glyphicon_glyphicon-ok True / False
    # ในกรณีที่ pointer = True จะมีคู่กันใน html (True กับ False เป็นเงื่อนไขคู่กัน แต่สนใจแค่ True) เลยตัดค่า False ออก 1 ตัว

    self.auto_renew = []

    for i in self.html_m.split('</td>'):
      if self.pointer == False:
        if 'glyphicon_glyphicon-ok' in i:
          if '<!--' not in i:
            self.auto_renew.append('Yes')
            self.pointer = True
            #break
          else:
            self.auto_renew.append('No')
            self.pointer = False
      else: # pointer == True | when pointer True skip 1 step
        self.pointer = False
        pass

    self.df_auto_new = pd.DataFrame({'Auto - Renewal' : self.auto_renew})


    self.result = pd.concat([pd.DataFrame.from_dict(self.dic), self.df_auto_new],axis=1)
    return self.result
      
  def count(self):
    return len(self.soup.find_all('tr', class_='row-content')) - 1 # remove labels column

