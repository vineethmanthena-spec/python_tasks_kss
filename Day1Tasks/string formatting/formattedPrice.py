Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:. Print a formatted price value
price=12345.6
print(f"price if rs.{price,.2f}")
SyntaxError: invalid decimal literal
print(f"price is rs. {price:,.2f}")
price is rs. 12,345.60
