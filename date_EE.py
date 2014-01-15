# -*- coding: utf-8 -*-

from datetime import datetime

paev = ('Esmaspäev, ','Teisipäev, ','Kolmapäev, ','Neljapäev, ','Reede, ','Laupäev, ','Pühapäev, ','Esmaspäev, ')
kuu = ('jaanuar ','veebruar ','märts ','aprill ','mai ','juuni ','juuli ','august ','september ','oktoober ','november ','detsember ')

f = open('homme.txt','w')
# f = open('../homme.txt','w')
f.write('<ANSI-WIN>\n<ParaStyle:Kuupäev>' + paev[datetime.now().weekday()+1] + str(datetime.now().day+1) + '. ' + kuu[datetime.now().month-1] + str(datetime.now().year))
f.close()

print 'Homme on ' + paev[datetime.now().weekday()+1].lower() + str(datetime.now().day+1) + '. ' + kuu[datetime.now().month-1] + str(datetime.now().year) + '.'

# Lihtsam, ent pikem versioon

# now = datetime.now()
# kuupaev = paev[now.weekday()+1] + str(now.day+1) + '. ' + kuu[now.month-1] + str(now.year)
# homme = '<ANSI-WIN>\n<ParaStyle:Kuup?ev>' + kuupaev
# f = open('homme.txt','w')
# f.write(homme)
# f.close()
