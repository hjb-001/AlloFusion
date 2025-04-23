# PyMOL script to highlight allosteric sites in 5DE1
fetch 5DE1
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 132 and chain A
show surface, resi 132 and chain A
color red, resi 132 and chain A
set transparency, 0.2, resi 132 and chain A
select resi 267 and chain A
show surface, resi 267 and chain A
color red, resi 267 and chain A
set transparency, 0.2, resi 267 and chain A
zoom chain A
