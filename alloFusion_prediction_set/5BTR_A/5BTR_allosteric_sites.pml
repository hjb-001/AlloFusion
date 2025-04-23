# PyMOL script to highlight allosteric sites in 5BTR
fetch 5BTR
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 262 and chain A
show surface, resi 262 and chain A
color red, resi 262 and chain A
set transparency, 0.2, resi 262 and chain A
select resi 273 and chain A
show surface, resi 273 and chain A
color red, resi 273 and chain A
set transparency, 0.2, resi 273 and chain A
select resi 345 and chain A
show surface, resi 345 and chain A
color red, resi 345 and chain A
set transparency, 0.2, resi 345 and chain A
select resi 363 and chain A
show surface, resi 363 and chain A
color red, resi 363 and chain A
set transparency, 0.2, resi 363 and chain A
zoom chain A
