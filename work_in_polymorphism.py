class Elma():
    
    def __init__(self, isim):
        self.isim = isim
        
    def bilgiVer(self):
        return self.isim + " 100 kaloridir"
    
class Muz():
    
    def __init__(self, isim):
        self.isim = isim
        
    def bilgiVer(self):
        return self.isim + " 150 kaloridir"
    
elma1 = Elma('elma')
muz1 = Muz('muz')

meyveListesi = [elma1, muz1]

for meyve in meyveListesi:
    print(meyve.bilgiVer())