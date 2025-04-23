# PyMOL script to highlight allosteric sites in 3PG9
fetch 3PG9
hide everything
show cartoon, chain B
color spectrum, chain B
select resi 67 and chain B
show surface, resi 67 and chain B
color green, resi 67 and chain B
set transparency, 0.2, resi 67 and chain B
select resi 257 and chain B
show surface, resi 257 and chain B
color green, resi 257 and chain B
set transparency, 0.2, resi 257 and chain B
select resi 215 and chain B
show surface, resi 215 and chain B
color green, resi 215 and chain B
set transparency, 0.2, resi 215 and chain B
select resi 256 and chain B
show surface, resi 256 and chain B
color green, resi 256 and chain B
set transparency, 0.2, resi 256 and chain B
select resi 69 and chain B
show surface, resi 69 and chain B
color green, resi 69 and chain B
set transparency, 0.2, resi 69 and chain B
select resi 260 and chain B
show surface, resi 260 and chain B
color green, resi 260 and chain B
set transparency, 0.2, resi 260 and chain B
select resi 214 and chain B
show surface, resi 214 and chain B
color green, resi 214 and chain B
set transparency, 0.2, resi 214 and chain B
select resi 261 and chain B
show surface, resi 261 and chain B
color green, resi 261 and chain B
set transparency, 0.2, resi 261 and chain B
zoom chain B
