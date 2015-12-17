all: Draft.pdf

latex:
	scholdoc pandoc/meta.yml Draft.md --template=pandoc/scholmdTemplate.latex --bibliography=biblio.bib --natbib --output=Draft.tex

# Need the `latexmk` program to automate LaTeX builds (included with texlive)
pdf:
	pdflatex Draft
# make bib refs
	bibtex Draft
# update refs
	pdflatex Draft
# actually build the pdf
	pdflatex Draft

clean:
	rm -rf *.pdf *.docx *.odt tmp/*

.PHONY: pdf clean
