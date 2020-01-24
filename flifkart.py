import requests
from bs4 import BeautifulSoup
from pprint import pprint

url="https://www.flipkart.com/search?q=mi%20phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")

flifkart=[]
def scrap_flifkart_data():
	main_div = soup.find("div",class_="_1UoZlX")

	div_class = main_div.find("div",class_="_1-2Iqu row")
	redme=div_class.find("div",class_="col col-7-12")
	name=redme.find("div",class_="_3wU53n").get_text()
	star=redme.find("div",class_="hGSR34").get_text()
	rating=redme.find("span",class_="_38sUEc").get_text()
	storag=redme.find("li",class_="tVe95H").get_text()
	data=redme.find_all("li",class_="tVe95H")

	list1=[]
	dic={}
	for i in data:

		a=(i.text)
		list1.append(a)

	dic["name"]=name
	dic["star"]=star
	dic["rating"]=rating
	dic["storag"]=storag
	dic["display"]=list1[1]
	dic["Camera"]=list1[2]
	dic["Battery"]=list1[3]
	dic["Processor"]=list1[4]
	dic["Accessories"]=list1[5]
	flifkart.append(dic)
	print(flifkart)


scrap_flifkart_data()