class Mobil:
    _merk = ""
    _tipe = ""
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def _init_(self,merk,tipe):
        self._merk = merk
        self._tipe = tipe
        # self._kapasitasBBM = kapasitasBBM
        # self._jenisBahanBakar = jenisBahanBakar

    def printInfo(self):
        print("============INFO============")
        print("Merk       :",self.getmerk())
        print("Tipe       :",self.gettipe())
        print("Bahan Bakar    :",self.getjenisBahanBakar())
        print("Kapasitas BBM  :",self.getkapasitasBBM())
    
    def setkapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM
    
    def setjenisBahanBakar(self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def getmerk(self,merk):
        return self._merk

    def gettipe(self,tipe):
        return self._tipe 

    def getjenisBahanBakar(self, jenisBahanBakar):
        return self._getjenisBahanBakar 


    def getkapasitasBBM(self, kapasitasBBM):
        return self._getkapasitasBBM 
        
    def setjenisBahanBakar(self, jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def setkapasitasBBM(self, kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    
    
    def isiBBM(self,harga):
        if self._kapasitasBBM == None or self._jenisBahanBakar == None:
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bkar belum di inputkan")
        else:
            n = harga * self._kapasitasBBM
            
            print("Total Harga : ", n)


    # def getmerk(self,merk):
    #     self._merk = merk

    # def gettipe(self,tipe):
    #     self._tipe = tipe

    # def getjenisBahanBakar(self, jenisBahanBakar):
    #     self._getjenisBahanBakar = jenisBahanBakar


    # def getkapasitasBBM(self, kapasitasBBM):
    #     self._getkapasitasBBM = kapasitasBBM
        
    # def setjenisBahanBakar(self, jenisBahanBakar):
    #     self._jenisBahanBakar = jenisBahanBakar

    # def setkapasitasBBM(self, kapasitasBBM):
    #     self._kapasitasBBM = kapasitasBBM

    


if __name__ == "__main__":
    m1 = Mobil("Toyota", "Avanza")
    m1.printInfo()
    m2 = Mobil("Nissan", "Grand Livina")
    m2.setjenisBahanBakar("Bensin")
    m2.setkapasitasBBM(20)
    m2.printInfo()
    m1.isiBBM(14500)
    m2.isiBBM(14500)  

    

