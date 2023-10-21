import re

s = '''
МОСКВА, 4 окт — РИА Новости. В этому году Нобелевский комитет решил присудить премию по химии за работы в области нанотехнологий. Одиннадцать миллионов крон разделят трое ученых из США, открывшие квантовые точки и разработавшие методы их стабилизации и производства, — '''

new_str = re.sub(r'^(.*\w)[^\w]*$', r'\1', s, flags=re.DOTALL)


print(new_str)