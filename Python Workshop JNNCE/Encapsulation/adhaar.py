class Adhar:

    def __init__(self,name,adhar_number,dob,finger_print,retina):
        self.name=name
        self.adhar_number=adhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina


    def display_userData(self):
        print(f"Retina:{self.__retina},adhar_number:{self.adhar_number}")


    def getRetena(self):
        return self.__retina

var=Adhar("Punith",256583,"1-feb-2020","shsbhasjbsdxjs","sjbkjsdbjskdk")

var.display_userData()
retena_var=var.getRetena()
print(retena_var)



