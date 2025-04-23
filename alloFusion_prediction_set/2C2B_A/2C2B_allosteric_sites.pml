# PyMOL script to highlight allosteric sites in 2C2B
fetch 2C2B
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 102 and chain A
show surface, resi 102 and chain A
color red, resi 102 and chain A
set transparency, 0.2, resi 102 and chain A
select resi 127 and chain A
show surface, resi 127 and chain A
color red, resi 127 and chain A
set transparency, 0.2, resi 127 and chain A
select resi 192 and chain A
show surface, resi 192 and chain A
color red, resi 192 and chain A
set transparency, 0.2, resi 192 and chain A
select resi 295 and chain A
show surface, resi 295 and chain A
color red, resi 295 and chain A
set transparency, 0.2, resi 295 and chain A
zoom chain A
