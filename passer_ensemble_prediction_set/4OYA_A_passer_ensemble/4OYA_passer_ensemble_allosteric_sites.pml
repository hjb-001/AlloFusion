# PyMOL script to highlight allosteric sites in 4OYA
fetch 4OYA
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 32.346 and chain A
show surface, resi 32.346 and chain A
color green, resi 32.346 and chain A
set transparency, 0.2, resi 32.346 and chain A
select resi 33.018 and chain A
show surface, resi 33.018 and chain A
color green, resi 33.018 and chain A
set transparency, 0.2, resi 33.018 and chain A
select resi 32.591 and chain A
show surface, resi 32.591 and chain A
color green, resi 32.591 and chain A
set transparency, 0.2, resi 32.591 and chain A
select resi 32.778 and chain A
show surface, resi 32.778 and chain A
color green, resi 32.778 and chain A
set transparency, 0.2, resi 32.778 and chain A
select resi 31.760) and chain A
show surface, resi 31.760) and chain A
color green, resi 31.760) and chain A
set transparency, 0.2, resi 31.760) and chain A
zoom chain A
