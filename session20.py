import streamlit as st
import requests
import time


#time.sleep(seconds)

def show_image(url,date):
	res = requests.get(url)

	img = date+'jpg'
	
	with open(img, 'wb') as f:
		f.write(res.content)

	st.image(img)


def print_better(content):
	copyright = 'NOT MENTIONED'
	date = 'NOT MENTIONED'
	explanation= 'NOT MENTIONED'
	title = 'NOT MENTIONED'
	url = 'NOT MENTIONED'

	if('copyright' in content):
		copyright=content['copyright']
	if('date' in content):
		date=content['date']
	if('explanation' in content):
		explanation=content['explanation']
	if('title' in content):
		title=content['title']
	if('url' in content):
		url=content['url']

	st.write('Copyright : ', copyright)
	st.write('Date : ', date)
	st.write('Explanation : ', explanation)
	st.subheader(title)

	show_image(url,date)


API = "https://api.nasa.gov/planetary/apod"
key = "nxvh9Cx4oWKi97W1BeHBFHAsSIBH3A6ftVdcasXL"

data = {
	'api_key':key
}


st.title('NASA Picture of the Day')

#time.sleep(3)

option = st.selectbox("Select : ", ['Latest', 'Specific Date'])

if(option=='Latest'):
	res = requests.get(API, params=data)
	print_better(res.json())

elif(option=='Specific Date'):
	date = st.date_input('Select date : ')
	data['date'] = date
	res = requests.get(API, params=data)
	print_better(res.json())