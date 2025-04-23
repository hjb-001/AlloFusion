# PyMOL script to highlight allosteric sites in 1WQW
fetch 1WQW
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 228 and chain A
show surface, resi 228 and chain A
color red, resi 228 and chain A
set transparency, 0.2, resi 228 and chain A
select resi 103 and chain A
show surface, resi 103 and chain A
color red, resi 103 and chain A
set transparency, 0.2, resi 103 and chain A
select resi 48 and chain A
show surface, resi 48 and chain A
color red, resi 48 and chain A
set transparency, 0.2, resi 48 and chain A
select resi 227 and chain A
show surface, resi 227 and chain A
color red, resi 227 and chain A
set transparency, 0.2, resi 227 and chain A
select resi 229 and chain A
show surface, resi 229 and chain A
color red, resi 229 and chain A
set transparency, 0.2, resi 229 and chain A
select resi 116 and chain A
show surface, resi 116 and chain A
color red, resi 116 and chain A
set transparency, 0.2, resi 116 and chain A
select resi 230 and chain A
show surface, resi 230 and chain A
color red, resi 230 and chain A
set transparency, 0.2, resi 230 and chain A
select resi 102 and chain A
show surface, resi 102 and chain A
color red, resi 102 and chain A
set transparency, 0.2, resi 102 and chain A
zoom chain A
