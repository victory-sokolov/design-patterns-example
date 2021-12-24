import requests

class VisitAllPages:

    def __init__(self, base_url):
        self.base_url = base_url

    def visit(self, visitor):
        next_url = self.base_url

        while next_url:
            response = requests.get(next_url).json()
            visitor(response)
            next_url = response['next']

visitor = VisitAllPages("https://pokeapi.co/api/v2/pokemon/")

visitor.visit(lambda results: print(results))
