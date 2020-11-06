import re

s = 'CREATE TABLE swms.abc( abc CHARACTER VARYING(1) NOT NULL days NUMERIC(4,0) NOT NULL) WITH ( OIDS = FALSE);'

# r = re.compile('"^CREATE TABLE://.*\.;$"')
# if r.match(s):
#     print("Hello")
#
# print('Hello1')
if s.startswith('CREATE') and s.endswith(';'):
    print('Hello2')
