# Django ECommerce Project
***

# Introduction
*This project demonstrates a simple E-commerce website using the Django Framework.*


# Getting Started
Here are instructions in getting your code up and running on your own system. 
1. Installation
2. Package dependencies
3. Latest releases

## Installations
After cloning or downloading the repo I highly recommend creating a virtual environment to avoid any errors.

Use this command to clone:
```console
git clone https://github.com/Ayobamidele/django_ecommerce_project.git
```
or

use the link for download
``` console
https://github.com/Ayobamidele/django_ecommerce_project.git
```

You must have installed Python and Django to run the project and most importantly Pip for the next instruction.

## Package dependencies
To run the program you'll need to download some packages first. Run this command to install the packages in requirements.txt:
```shell
pip install -r requirements.txt
```
## Latest releases
During the creation of this project python 3.10 was available but python 3.8 was used to avoid any issues with support. All version above 3.8 will work.

# Build and Test
Testing the project is made easy with pytest and coverage package to ensure all functions are up and running to avoid by error and early detection.

Once all packages are installed Pytest should already be installed. to do a quick checkup run this command:

```shell
pytest
```


# Features
1. Products
2. Payment
3. Admin
4. User
5. Orders

### Products

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The database allows for multiple products to have multiple attributes. Allowing for a product to have different attributes. Products can have categories, picture, quantity, price and discount price by default. Products can also be deactivated or activated to display when needed.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The website loads products from a SQLite database and displays them. Users can select display products in a single category - *which are set active in the database*. Users can click on any product to get more information including pricing and other available details. Users can select items and add them to their shopping cart. There they can checkout having the options to pay with Paypal or email. If you don't want to buy yet, you could save to your wishlist for later

### Payment

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Your payment address and card details is saved on the site for fast checkout. You have the options to pay with:

- Paypal
- Email

### Admin


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users with superuser status can access the admin page. The page is enabeled with filtering and ordering, so searching through objects is fast and easy.

### User


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users have easy access to the login and register page and if any issue with their password they have the option to reset it from their email. Some personal details can also be added.

> **Note:** Once users register their account, the email won't be removed from the database if you try to delete the account. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Also after registering you can't change the email used to register.


### Orders


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users can see previous items they bought in their orders page as well as the price and quantity of the orde0

# Contribute
This project welcomes contributions and suggestions. But at present, we are not accepting any code contributions. If you find any errors or have trouble with any of our code - please put it on issues on Github.

