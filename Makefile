clean:
	rm -rf dist/
	rm -rf build/
	rm -rf src/jpaye.egg-info

build:
	python -m build --wheel

pytest:
	pytest

.PHONY: clean build
