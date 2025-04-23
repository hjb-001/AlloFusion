# PyMOL script to highlight allosteric sites in 4NHV
fetch 4NHV
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 233 and chain A
show surface, resi 233 and chain A
color red, resi 233 and chain A
set transparency, 0.2, resi 233 and chain A
select resi 235 and chain A
show surface, resi 235 and chain A
color red, resi 235 and chain A
set transparency, 0.2, resi 235 and chain A
select resi 236 and chain A
show surface, resi 236 and chain A
color red, resi 236 and chain A
set transparency, 0.2, resi 236 and chain A
select resi 237 and chain A
show surface, resi 237 and chain A
color red, resi 237 and chain A
set transparency, 0.2, resi 237 and chain A
select resi 238 and chain A
show surface, resi 238 and chain A
color red, resi 238 and chain A
set transparency, 0.2, resi 238 and chain A
select resi 260 and chain A
show surface, resi 260 and chain A
color red, resi 260 and chain A
set transparency, 0.2, resi 260 and chain A
select resi 262 and chain A
show surface, resi 262 and chain A
color red, resi 262 and chain A
set transparency, 0.2, resi 262 and chain A
select resi 263 and chain A
show surface, resi 263 and chain A
color red, resi 263 and chain A
set transparency, 0.2, resi 263 and chain A
zoom chain A
