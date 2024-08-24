#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import re
text='Python exercises, PHP exercises.'
# Replace space, comma, or dot with a colon
new_text=text.replace(' ',':').replace(',',':').replace('.',':')
print(new_text)


# In[25]:


import pandas as pd
import re
data={'summary': ['Hello, world!', 'xxxxx test', '123 four, five:; six...']}
df=pd.DataFrame(data)
df['summary']=df['summary'].apply(lambda x:re.sub(r'[^\w\s]', '', x))
print(df)


# In[40]:


import re
def find_long_words(string):
    pattern = re.compile(r'{4,}\b')
    long_words = pattern.findall(string)
    return long_words
text='The Elephant is taller than zebra.'
print(re.findall(r'\b\w{4,}\b',text))


# In[57]:


import re
def find_words(string):
    pattern=re.compile(r'{3,5}\b')
    words = pattern.findall(string)
    return words
text='I like to eat icecream any time.'   
print(re.findall(r"\b\w{3,5}\b",text))


# In[137]:


import re
def remove_paranthesis(strings):
    pattern=re.compile(r"\(\)")
    modified_strings=[]
    for string in strings:
        modified_string=re.sub(pattern,"",string)
        modified_strings.append(modified_string)
        return modified_string
sample_text = ["example (.com)","hr@fliprobo (.com)","github (.com)","hello (data science world)","data (scientist)"]

result = (sample_text)
print(result)
  
    


# In[ ]:





# In[154]:


import re
items=["example(.com)","hr@fliprobo(.com)","github(.com)","hello(data science world)","data(scientist)"]
new_item=re.sub(r"\s*\([^)]*\)","",item)
new_item=re.sub("\(.*\)","",item)
for item in items:
    print(re.sub(r"/\([^)]+\)","",item))
    


# In[155]:


import re
text="ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*',text))


# In[72]:


import re
def capital_words_spaces(str1):
    return re.sub(r"(\w)[A-Z]",r"\1 \2",str1)
def insert_spaces(text):
    pattern=r'(\d+)([A-Za-z]+)'
    result=re.sub(pattern, r'\1\2', text)
    return result

text_str="RegularExpression1IsAn2ImportantTopic3InPython"

output=insert_spaces(text_str)
print(output)

import re
def insert_spaces(text):
    pattern=r'([A-z][a-z][0-9]+|\d+)'
    result=re.sub(pattern,r' \1',text)
    result =result.strip()
    return result
sample_text="RegularExpression1IsAn2ImportantTopic3InPython"
result=insert_spaces(sample_text)
print(result)


# In[172]:


import re
def match_string(string):
    patterns=r'^[a-zA-Z0-9_]+$'
    if re.match(pattern,string):
        string1("hello world123")
        match_string(string1)
        result=("string matches the pattern")
        print(result)


# In[174]:


import re
def match_num(string):
    text=re.compile(r"^8")
    if text.match(string):
        return true
    else:
        return false
    print(match_num('5-789123'))
    print(match_num('8-834361'))


# In[187]:


import re
ip="12,04,012,987"
string=re.sub('\^.[0]*','.',ip)
print(string)


# In[5]:


import re
text='On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the country.'
pattern=r"\b([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)? \d{4})\b"
matches=re.findall(pattern,text)
date_string=matches[0] 
print(date_string)


# In[19]:


import re
patterns=['fox','dog','horse']
text='The quick brown fox jump over the lazy dog.'
for pattern in patterns:
    print( '"%s in %s"'%(pattern,text),)
    if re.search(pattern,text):
        print('matched')


# In[48]:


import re
pattern='fox'
text='The quick brown fox jumps over the lazy dog.'
match=re.search(pattern,text)
s=match.start()
e=match.end()
print('found "%s" in "%s" %d in %d' %\
(match.re.pattern,match.string, s,e))


# In[43]:


import re
text='python exercises, PHP exercises, c# exercises'
pattern='exercises'
for match in re.findall(pattern, text):
    print('found "%s"' %match)


# In[41]:


import re
text='python exercises, PHP exercises, c# exercises'
pattern='exercises'
for match in re.finditer(pattern, text):
    s=match.start()
    e=match.end()
    print('found "%s" at %d:%d' % (text[s:e], s,e))


# In[51]:


import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',dt)
dt1="2024-23-08"
print("Date in the format  YYYY-MM-DD format:",dt1)
print("New format date in DD-MM-YYYY format:", change_date_format(dt1))


# In[58]:


import re
def find_decimal_numbers(string):
    pattern=re.compile(r'\d+\.\d{1,2}')
    decimal_numbers=re.findall(pattern,string)
    return decimal_numbers


# In[68]:


import re
text="ten 10 twenty 20 thirty 30"
result= re.split("\d+", text) 
for element in result:
    for m in re.finditer("\d+",text):
        
        print("Index position:",m.start())


# In[69]:


import re
input_string='my marks in each semester are:947,896,926,524,734,950,642'
numeric_values=re.findall(r'\d+', input_string)
numeric_values=[int(value) for value in numeric_values]
max_value=max(numeric_values)
print(max_value)


# In[81]:


import re
def insert_spaces(text):
    pattern=r' ([A-z][a-z][0-9]+|\d+)'
    result = re.sub(pattern, r' \1',text)
    result = result.strip()
    return result
sample_text="RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(sample_text)
print(output)


# In[83]:


import re
pattern =r'[A-Z][a-z]+'
text="This is a Very Nice Drawing"
Uppercase_words = re.findall(pattern,text)
print(Uppercase_words)


# In[ ]:





# In[86]:


import re
def remove_duplicates(sentence):
    pattern = r'\b(\w+)(\s+\1\b)+'
    result=re.sub(pattern, r'\1',sentence)
    return result
sentence="Hello hello world world"
output=remove_duplicates(sentence)
print(output)


# In[87]:


import re
def check_string(string):
    pattern=r"\w$"
    match= re.search(pattern,string)
    input_string= input("Enter a string:")
    if check_string(input_string):
        print("string with an alphanumeric character")


# In[91]:


import re
def extract_hashtags(text):
    hashtags= re.findall(r'#\w+',text)
    return hashtags
text="""RT@kapil_kaushik:#Doltiwal i mean #xyzabc is "hurt" by #Domonetization as the same has rendered USELESS
    <ed><U+OOAO><U+OOBD><ed><U+OOB1><U+oo89>"acquired funds"No wo"""
hashtags = extract_hashtags(text)
print(hashtags)


# In[115]:


import re
def remove_words(string):
    pattern =re.compile(r'\b\w{2,4}\b')
    modified_string = re.sub(pattern,'',string)
    return modified_string
sample_text= "The following example creates an arraylist with a capacityof 50 elements. 4 elements are then added to arraylist and the arraylist is trimmed accordingly."
expected_output = "Following example creates arraylist a capacity elements. 4 elements added arraylist trimmed accordingly."
result= remove_words(sample_text)
print(expected_output)


# In[ ]:





# In[ ]:





# In[ ]:




