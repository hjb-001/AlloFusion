# PyMOL script to highlight allosteric sites in 4YW8
fetch 4YW8
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 30 and chain A
show surface, resi 30 and chain A
color red, resi 30 and chain A
set transparency, 0.2, resi 30 and chain A
select resi 290 and chain A
show surface, resi 290 and chain A
color red, resi 290 and chain A
set transparency, 0.2, resi 290 and chain A
select resi 435 and chain A
show surface, resi 435 and chain A
color red, resi 435 and chain A
set transparency, 0.2, resi 435 and chain A
select resi 476 and chain A
show surface, resi 476 and chain A
color red, resi 476 and chain A
set transparency, 0.2, resi 476 and chain A
zoom chain A
