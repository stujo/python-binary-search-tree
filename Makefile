init:
	pip install -r requirements.txt

htmldocs:
	make -C docs html

test:
	nosetests tests
