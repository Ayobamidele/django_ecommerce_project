
# Django ECommerce Project
***
*This project demonstrates a simple E-commerce website using the Django Framework.*

## Features
***

### Payment

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Your payment address and card details is saved on the site for fast checkout. You have the options to pay with:

- Paypal
- Email.


### Products


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The database allows for multiple products to have multiple attributes. Allowing for a product to have different attributes.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Products can have categories, picture, quantity, price and discount price. Products can also be deactivated or activated to display when needed.


### Admin


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users with superuser status can access the admin page. The page is enabeled with filtering and ordering, so searching through objects is fast and easy.

### Users


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users have easy access to the login and register page and if any issue with their password they have the option to reset it from their email. Some personal details can also be added.

> **Note:** Once users register their account, the email won't be removed from the database if you try to delete the account. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Also after registering you can't change the email used to register.

### Wishlist


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users can save Products to their wishlist to view later.

### Orders


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users can see previous items they bought in their orders page as well as the price and quantity of the ordered item.



## Summary
***
> The website loads products from a SQLite database and displays them. Users can select display products in a single category - *which are set active in the database*. Users can click on any product to get more information including pricing and other available details. Users can select items and add them to their shopping cart. There they can checkout having the options to pay with Paypal or email. If you don't want to buy yet, you could save to your wishlist for later


