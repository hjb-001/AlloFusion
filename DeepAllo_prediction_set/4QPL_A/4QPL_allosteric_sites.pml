# PyMOL script to highlight allosteric sites in 4QPL
fetch 4QPL
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 65 and chain A
show surface, resi 65 and chain A
color red, resi 65 and chain A
set transparency, 0.2, resi 65 and chain A
select resi 82 and chain A
show surface, resi 82 and chain A
color red, resi 82 and chain A
set transparency, 0.2, resi 82 and chain A
select resi 179 and chain A
show surface, resi 179 and chain A
color red, resi 179 and chain A
set transparency, 0.2, resi 179 and chain A
select resi 61 and chain A
show surface, resi 61 and chain A
color red, resi 61 and chain A
set transparency, 0.2, resi 61 and chain A
select resi 181 and chain A
show surface, resi 181 and chain A
color red, resi 181 and chain A
set transparency, 0.2, resi 181 and chain A
select resi 57 and chain A
show surface, resi 57 and chain A
color red, resi 57 and chain A
set transparency, 0.2, resi 57 and chain A
select resi 83 and chain A
show surface, resi 83 and chain A
color red, resi 83 and chain A
set transparency, 0.2, resi 83 and chain A
select resi 114 and chain A
show surface, resi 114 and chain A
color red, resi 114 and chain A
set transparency, 0.2, resi 114 and chain A
zoom chain A
