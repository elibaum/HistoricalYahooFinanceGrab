
from datetime import date
today = date.today()
print today
print today
import Module
share = Module.Share("600028.SS",'2015-01-01',str(today))
print share.getopen()
'''
print share.gethigh()
print share.getlow()
print share.getclose()
print share.getvolume()
print share.getadj()
'''