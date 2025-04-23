# PyMOL script to highlight allosteric sites in 4DQW
fetch 4DQW
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 118 and chain A
show surface, resi 118 and chain A
color red, resi 118 and chain A
set transparency, 0.2, resi 118 and chain A
select resi 119 and chain A
show surface, resi 119 and chain A
color red, resi 119 and chain A
set transparency, 0.2, resi 119 and chain A
select resi 133 and chain A
show surface, resi 133 and chain A
color red, resi 133 and chain A
set transparency, 0.2, resi 133 and chain A
select resi 134 and chain A
show surface, resi 134 and chain A
color red, resi 134 and chain A
set transparency, 0.2, resi 134 and chain A
select resi 179 and chain A
show surface, resi 179 and chain A
color red, resi 179 and chain A
set transparency, 0.2, resi 179 and chain A
select resi 180 and chain A
show surface, resi 180 and chain A
color red, resi 180 and chain A
set transparency, 0.2, resi 180 and chain A
select resi 181 and chain A
show surface, resi 181 and chain A
color red, resi 181 and chain A
set transparency, 0.2, resi 181 and chain A
select resi 196 and chain A
show surface, resi 196 and chain A
color red, resi 196 and chain A
set transparency, 0.2, resi 196 and chain A
select resi 199 and chain A
show surface, resi 199 and chain A
color red, resi 199 and chain A
set transparency, 0.2, resi 199 and chain A
zoom chain A
