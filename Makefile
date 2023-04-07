
virtual-env: 
	#Create virtual environment
	rm -rf venv && python3 -m venv venv


deps:
	#install the requirements: 
	cd dependecies && poetry install

run:
	#Run application
	python3 app.py