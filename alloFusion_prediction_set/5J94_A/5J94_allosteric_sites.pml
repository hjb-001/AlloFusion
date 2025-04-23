# PyMOL script to highlight allosteric sites in 5J94
fetch 5J94
hide everything
show cartoon, chain A
color spectrum, chain A
select resi -7 and chain A
show surface, resi -7 and chain A
color red, resi -7 and chain A
set transparency, 0.2, resi -7 and chain A
select resi -5 and chain A
show surface, resi -5 and chain A
color red, resi -5 and chain A
set transparency, 0.2, resi -5 and chain A
select resi 1 and chain A
show surface, resi 1 and chain A
color red, resi 1 and chain A
set transparency, 0.2, resi 1 and chain A
select resi 17 and chain A
show surface, resi 17 and chain A
color red, resi 17 and chain A
set transparency, 0.2, resi 17 and chain A
select resi 63 and chain A
show surface, resi 63 and chain A
color red, resi 63 and chain A
set transparency, 0.2, resi 63 and chain A
select resi 67 and chain A
show surface, resi 67 and chain A
color red, resi 67 and chain A
set transparency, 0.2, resi 67 and chain A
select resi 119 and chain A
show surface, resi 119 and chain A
color red, resi 119 and chain A
set transparency, 0.2, resi 119 and chain A
select resi 122 and chain A
show surface, resi 122 and chain A
color red, resi 122 and chain A
set transparency, 0.2, resi 122 and chain A
select resi 123 and chain A
show surface, resi 123 and chain A
color red, resi 123 and chain A
set transparency, 0.2, resi 123 and chain A
select resi 162 and chain A
show surface, resi 162 and chain A
color red, resi 162 and chain A
set transparency, 0.2, resi 162 and chain A
select resi 167 and chain A
show surface, resi 167 and chain A
color red, resi 167 and chain A
set transparency, 0.2, resi 167 and chain A
select resi 198 and chain A
show surface, resi 198 and chain A
color red, resi 198 and chain A
set transparency, 0.2, resi 198 and chain A
select resi 199 and chain A
show surface, resi 199 and chain A
color red, resi 199 and chain A
set transparency, 0.2, resi 199 and chain A
zoom chain A
