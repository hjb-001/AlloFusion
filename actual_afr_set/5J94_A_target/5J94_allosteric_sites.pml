# PyMOL script to highlight allosteric sites in 5J94
fetch 5J94
hide everything
show cartoon, chain A
color spectrum, chain A
select resi -2 and chain A
show surface, resi -2 and chain A
color green, resi -2 and chain A
set transparency, 0.2, resi -2 and chain A
select resi -1 and chain A
show surface, resi -1 and chain A
color green, resi -1 and chain A
set transparency, 0.2, resi -1 and chain A
select resi 0 and chain A
show surface, resi 0 and chain A
color green, resi 0 and chain A
set transparency, 0.2, resi 0 and chain A
select resi 1 and chain A
show surface, resi 1 and chain A
color green, resi 1 and chain A
set transparency, 0.2, resi 1 and chain A
select resi 3 and chain A
show surface, resi 3 and chain A
color green, resi 3 and chain A
set transparency, 0.2, resi 3 and chain A
select resi 119 and chain A
show surface, resi 119 and chain A
color green, resi 119 and chain A
set transparency, 0.2, resi 119 and chain A
select resi 122 and chain A
show surface, resi 122 and chain A
color green, resi 122 and chain A
set transparency, 0.2, resi 122 and chain A
select resi 123 and chain A
show surface, resi 123 and chain A
color green, resi 123 and chain A
set transparency, 0.2, resi 123 and chain A
select resi 176 and chain A
show surface, resi 176 and chain A
color green, resi 176 and chain A
set transparency, 0.2, resi 176 and chain A
select resi 198 and chain A
show surface, resi 198 and chain A
color green, resi 198 and chain A
set transparency, 0.2, resi 198 and chain A
select resi 199 and chain A
show surface, resi 199 and chain A
color green, resi 199 and chain A
set transparency, 0.2, resi 199 and chain A
zoom chain A
