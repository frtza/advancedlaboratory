all: build/main.pdf

# python scripts
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	# allow matplotlib to find tex header file in main directory when running latex in tmp directory
	# set matplotlibrc in main directory
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

# jupyter notebook kompilieren
build/notes.pdf: note.ipynb | build
	jupyter execute note.ipynb

# dependencies
build/main.pdf: build/plot.pdf build/notes.pdf

build/main.pdf: FORCE | build
	# find header file in main directory
	# find bib file in main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
		--lualatex \
		--output-directory=build \
		--interaction=batchmode \
		--halt-on-error \
	main.tex
	cp build/main.pdf V01.pdf

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
