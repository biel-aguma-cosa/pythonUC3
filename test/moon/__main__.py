import numpy as np, datetime
from scipy.constants import G
from dateutil.relativedelta import relativedelta
class moon:
    spd = np.array([3.683,0])
    w = 7.3*10**22
    r = 1.740
class earth:
    w = 5.972*10**24
    r = 6.380

birth = datetime.date(2007,11,21)
today = datetime.date.today()
age = relativedelta(today,birth)
print(age.years)