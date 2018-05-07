travis:
	[ ! -d .testrepository ] || \
		find .testrepository -name "times.dbm*" -delete
	python setup.py test --coverage \
		--coverage-package-name=it3conv
	flake8 --max-complexity 10 it3conv
clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
