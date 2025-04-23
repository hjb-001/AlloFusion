# PyMOL script to highlight allosteric sites in 1WQW
fetch 1WQW
hide everything
show cartoon, chain A
color spectrum, chain A
select resi 17.527) and chain A
show surface, resi 17.527) and chain A
color green, resi 17.527) and chain A
set transparency, 0.2, resi 17.527) and chain A
zoom chain A
