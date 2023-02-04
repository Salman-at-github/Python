class ElectronicDevice:
    storageGB = 500
    body = ["metallic", "plastic"]
    weight = 1000


class PocketDevice(ElectronicDevice):
    weight = 100
    battery = "removable"


class Phone(PocketDevice):
    weight = 50

    def info(self):
        return f"It has {self.storageGB} GB, weigth is {self.weight} grams with {self.battery} battery and {self.body} body."

def show_details(self,*blah):
    print(self,*blah)


nokia = Phone()
nokia.body = ["metallic"]


# print(nokia.info())
# print(nokia.body)
show_details(nokia.info())
