# PyMOL script to highlight allosteric sites in 3PG9
fetch 3PG9
hide everything
show cartoon, chain B
color spectrum, chain B
select resi 34 and chain B
show surface, resi 34 and chain B
color red, resi 34 and chain B
set transparency, 0.2, resi 34 and chain B
select resi 35 and chain B
show surface, resi 35 and chain B
color red, resi 35 and chain B
set transparency, 0.2, resi 35 and chain B
zoom chain B
