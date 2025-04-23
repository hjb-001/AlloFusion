# PyMOL script to highlight allosteric sites in 4OYA
fetch 4OYA
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 13.089 and chain A
show surface, resi 13.089 and chain A
color green, resi 13.089 and chain A
set transparency, 0.2, resi 13.089 and chain A
select resi 14.138) and chain A
show surface, resi 14.138) and chain A
color green, resi 14.138) and chain A
set transparency, 0.2, resi 14.138) and chain A
zoom chain A
