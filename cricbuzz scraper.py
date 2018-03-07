from IPython.core.display import display, HTML
from bs4 import BeautifulSoup
import urllib.request 
import time

content = urllib.request.urlopen("http://m.cricbuzz.com/cricket-match/live-scores")

soup= BeautifulSoup(content, "lxml" )
soup.prettify()
# basic soup to soup whole document
#cricmain=soup.body.find_all("div", {"class": "cb-col cb-col-100 cb-lv-main"})

cricelement=soup.find_all("h4",{"class":"cb-list-item ui-header ui-branding-header"})
#found all header class which contain cricket match names

x=[]
y=[]
#initialized two lists for future use

j=0
print("****Matches****")
for i in cricelement:
    print(("{0}--{1}\n\t").format(j,i.get_text()))
    j=j+1
#this code is for printing all matches corresponding to their list element number 

match=int(input("select a match: "))
mat=match
#input match in a new variable

cricelement_detail=soup.find_all("div",{"class":"btn-group cbz-btn-group"})[mat]
#new soup to find all buttons associated with a particular match

#match_detail=soup.find_all("a",{"class":"btn btn-default"})[mat]

print(cricelement_detail.get_text("\n"))
#printed all match buttons
q=cricelement_detail.get_text()

#print(q)
l=q.split()
#made a list of all buttons for further use


for z in cricelement_detail:
    y.append("http://m.cricbuzz.com"+z.attrs['href'])
#appended m.cricbuzz with the href of site to get final id
choice=int(input("select one option. Enter 0,1,2,3 corresponding to your choice: "))
print("\nSummary/Commentary may not be available for some matches\n")
ch=choice
#print(str(y[ch]))
#converted the url for string to be souped

content1 = urllib.request.urlopen(str(y[ch]))
soup1= BeautifulSoup(content1, "lxml" )
soup1.prettify()
#souped the given string
if(l[choice]=='Commentary'):
    outputdata=soup1.find_all("div")
    comm=[outputdata.get_text("\n") for outputdata in soup1.select('p')]
#find all text instances where <p> tag is present and print it. 

    for i in range(0,7):
        print(comm[i]+("\n"))
#printed all such instances

#if(l[1]=="Commentary"):
 #   commentary_detail=soup.findall("p",{"class":"commtext"})
  #  print(commentary_detail.get_text("\n"))
#print(cricelement_detail[mat].get_text())

if(l[choice]=='Preview'):
    outputdata=soup1.find_all("div")
    comm=[outputdata.get_text("\n") for outputdata in soup1.select('p')]
    
    for i in range(0,len(comm)):
        print(comm[i]+("\n"))


if(l[choice]=='Summary'):
    outputdata=soup1.find_all("div")
    comm=[outputdata.get_text("\n") for outputdata in soup1.select('p')]
    
    for i in range(0,len(comm)):
        print(comm[i]+("\n"))
        
if(l[choice]=='Scorecard'):
    outputdata=soup1.find_all("div",{"class":"table-responsive"})
    comm=[outputdata.get_text("\t") for outputdata in soup1.select('tr')]
    print("\n")
    for i in range(0,len(comm)-15):
        
        print(comm[i]+("\n\n"))

if(l[choice]=='Summary'):
    outputdata=soup1.find_all("div",{"class":"list-group"})
    comm=[outputdata.get_text("\t") for outputdata in soup1.select('h4')]
    print(comm[0])
    
    outputdata1=soup1.find_all("div",{"class":"col-xs-12 col-lg-12 "}) 
    for i in outputdata1:
        print(i.get_text()+("\n"))
    #for row in table.find_all("tr"):
    #    cells = row[0].find_all("td")
    #    print(cells)
if(l[choice]=='Points'):
    outputdata=soup1.find_all("div",{"class":"list-group"})
    comm=[outputdata.get_text("\t") for outputdata in soup1.select('tr')]
    for i in range(0,len(comm)-14):
        print(comm[i])
    
    