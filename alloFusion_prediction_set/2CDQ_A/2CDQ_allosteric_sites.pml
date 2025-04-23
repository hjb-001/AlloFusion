# PyMOL script to highlight allosteric sites in 2CDQ
fetch 2CDQ
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 148 and chain A
show surface, resi 148 and chain A
color red, resi 148 and chain A
set transparency, 0.2, resi 148 and chain A
select resi 234 and chain A
show surface, resi 234 and chain A
color red, resi 234 and chain A
set transparency, 0.2, resi 234 and chain A
select resi 253 and chain A
show surface, resi 253 and chain A
color red, resi 253 and chain A
set transparency, 0.2, resi 253 and chain A
select resi 369 and chain A
show surface, resi 369 and chain A
color red, resi 369 and chain A
set transparency, 0.2, resi 369 and chain A
select resi 377 and chain A
show surface, resi 377 and chain A
color red, resi 377 and chain A
set transparency, 0.2, resi 377 and chain A
select resi 392 and chain A
show surface, resi 392 and chain A
color red, resi 392 and chain A
set transparency, 0.2, resi 392 and chain A
select resi 396 and chain A
show surface, resi 396 and chain A
color red, resi 396 and chain A
set transparency, 0.2, resi 396 and chain A
select resi 422 and chain A
show surface, resi 422 and chain A
color red, resi 422 and chain A
set transparency, 0.2, resi 422 and chain A
zoom chain A
