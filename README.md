ONLINE SALES ANALYSIS

	1. Structura proiectului

product.py
- Clasa Product:
  - Atribute: name, price, quantity
  - Metode:
    - display_info() : afiseaza produsul
    - update_quantity(quantity) : actualizeaza cantitatea

product_manager.py
- Clasa ProductManager:
  - Atribute: products (lista produselor)
  - Metode:
    - add_product(product) : adauga produs
    - show_products() : afiseaza toate produsele
    - total_value() : valoare totala inventar
    - remove_product(name) : sterge produs dupa nume

cart.py
- Clasa Cart:
  - Atribute: cart_items (lista produselor din cos)
  - Metode:
    - add_to_cart(product) : adauga produs in cos
    - show_cart() : afiseaza continutul cosului
    - total_cart_value() : calculeaza valoarea cosului

main.py
- Creeaza ProductManager si adauga produse
- Creeaza Cart si adauga 3 produse aleatorii
- Afiseaza continutul cosului si valoarea totala

	2. Pregatirea mediului
- Creare folder local: online_sales_analysis
- Creare repository pe GitHub
- Configurare Git (user.name si user.email)

Implementare clase
- Product si ProductManager
- Adaugare produse si afisare inventar

Versionare
- Commit-uri si push pe GitHub

Functionalitate stergere produse
- Ramura: add-product-removal
- Metoda remove_product(name)

Merge ramura add-product-removal in main

Adaugare clasa Cart
- Ramura: add-cart-functionality
- Functionalitate cos de cumparaturi

Merge add-cart-functionality in main si rezolvare conflicte

Adaugare .gitignore
- Fisier config.json ignorat

	3. Rulare proiect

Clonare repository:
git clone https://github.com/octavnicul3scu/online_sales_analysis.git
cd online_sales_analysis

Rulare script principal:
python main.py
- Afiseaza produsele si cosul de cumparaturi cu valoarea totala

