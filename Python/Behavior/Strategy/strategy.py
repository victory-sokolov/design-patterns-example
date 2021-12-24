class Fedex:
    def calculate(self, package):
        return 2.45


class UPS:
    def calculate(self, package):
        return 1.56

class USPS:
    def calculate(self, package):
        return 4.5

class Shipping:
    def __init__(self, comapny):
        self.company = comapny

    def calculate(self, package):
        return self.company.calculate(package)


fedex = Fedex()
ups = UPS()
usps = USPS()

package = {
    'from': "Latvia",
    'to': 'Russian',
    'weight': 1.56
}

fedex.calculate(package)
ups.calculate(package)
usps.calculate(package)

shipping = Shipping(fedex)
price = shipping.calculate(package)
print(f"Fedex: {price}")
