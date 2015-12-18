all: Draft.pdf

latex:
	scholdoc pandoc/meta.yml ITAME/Draft/Draft.md --template pandoc/scholmdTemplate.latex --bibliography resources/biblio.bib --natbib --output=Draft.tex

# Need the `latexmk` program to automate LaTeX builds (included with texlive)
pdf:
	latexmk -f -interaction=nonstopmode -pdf Draft
	#pdflatex Draft
# make bib refs
	#bibtex Draft
# update refs
	#pdflatex Draft
# actually build the pdf
	#pdflatex Draft

clean:
	rm -rf *.pdf *.docx *.odt tmp/*

.PHONY: pdf clean
