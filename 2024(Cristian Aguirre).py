class IceCreamShop:
    def __init__(self):
        self.menu = {
            "Vanilla": 1.50,
            "Chocolate": 1.75,
            "Strawberry": 2.00,
            "Mint": 1.80,
            "Cookie Dough": 2.50
        }
        self.total_sales = 0.0

    def display_menu(self):
        print("𝐖ｅｌｃｏｍｅ ｔｏ ｏｕｒ Ｉｃｅ Ｃｒｅａｍ Ｓｈｏｐ!\n")  
        print("▂ ▄ ▅ ▆ ▇ █ 𝓜𝓮𝓷𝓾 █ ▇ ▆ ▅ ▄ ▂▁:\n")
        for flavor, price in self.menu.items():
            print(f"{flavor}: ${price:.2f}")

    def order_ice_cream(self, flavor, quantity):
        if flavor in self.menu:
            cost = self.menu[flavor] * quantity
            print(f"You ordered {quantity} {flavor} ice cream(s).")
            print(f"Total cost: ${cost:.2f}")
            self.total_sales += cost
        else:
            print("Sorry, that flavor is not available.")

    def show_total_sales(self):
        print(f"Total sales: ${self.total_sales:.2f}")


# Example usage
def main():
    shop = IceCreamShop()
    shop.display_menu()

    shop.order_ice_cream("Vanilla", 2)
    shop.order_ice_cream("Strawberry", 1)
    shop.order_ice_cream("Cookie Dough", 3)

    shop.show_total_sales()


if __name__ == "__main__":
    main()


