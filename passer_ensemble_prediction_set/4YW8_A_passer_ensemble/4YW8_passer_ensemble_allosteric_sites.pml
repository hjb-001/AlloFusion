# PyMOL script to highlight allosteric sites in 4YW8
fetch 4YW8
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 0.544 and chain A
show surface, resi 0.544 and chain A
color green, resi 0.544 and chain A
set transparency, 0.2, resi 0.544 and chain A
select resi 1.293) and chain A
show surface, resi 1.293) and chain A
color green, resi 1.293) and chain A
set transparency, 0.2, resi 1.293) and chain A
zoom chain A
