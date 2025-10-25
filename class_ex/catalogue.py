class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        list_of_word_first_letter = [ word for word in self.products if word.startswith(first_letter)]
        return list_of_word_first_letter


    def __repr__(self):
        pre_text = f"Items in the {self.name} catalogue:\n"
        ending_output = "\n".join(sorted(self.products))
        final_text = pre_text + ending_output
        return final_text
