# PyMOL script to highlight allosteric sites in 4NHV
fetch 4NHV
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 235 and chain A
show surface, resi 235 and chain A
color green, resi 235 and chain A
set transparency, 0.2, resi 235 and chain A
select resi 236 and chain A
show surface, resi 236 and chain A
color green, resi 236 and chain A
set transparency, 0.2, resi 236 and chain A
select resi 260 and chain A
show surface, resi 260 and chain A
color green, resi 260 and chain A
set transparency, 0.2, resi 260 and chain A
select resi 264 and chain A
show surface, resi 264 and chain A
color green, resi 264 and chain A
set transparency, 0.2, resi 264 and chain A
zoom chain A
