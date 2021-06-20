from pprint import pprint

from dml import delete, insert, select, update

insert('Regis', '98989898', 'regis_@gmail.com')
insert('Fabricio', '98989898', 'fabricio_@gmail.com')
insert('Mazinho', '98989898', 'mazinho_@gmail.com')

update('Fabricião', 'fabricio_@gmail.com')

delete('regis_@gmail.com')

pprint(select('phone', '98989898'))
