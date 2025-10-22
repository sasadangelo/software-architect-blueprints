# 📋 System Requirements

## Introduction

This document describes the system requirements for a prototype eShop application. The goal of this prototype is to demonstrate a basic shopping experience where a user can view products, add them to a cart, and place orders. The system is designed to work entirely **in-memory** without a database and focuses on simplicity and usability. It serves as a foundation for further development and enhancement.

## Functional Requirements (FR)

1. **List Products Viewing**
   - The user must be able to view a list of available products.

2. **Product Details Viewing**
   - The user must be able to view the details of a product.
   - For this prototype version, only two products are required.

3. **Add to Cart**
   - The user must be able to select one or more products and add them to the cart.
   - The quantity of a product increases by 1 each time the same product is selected again.

4. **Cart Viewing**
   - The user must be able to view the contents of the cart.
   - The cart should display the product name, unit price, quantity, and total per product.
   - The overall total of the cart should also be displayed.

5. **Checkout**
   - The user must be able to checkout the items in the cart.
   - After checkout, the cart is cleared and the order is stored in memory.
   - The user should receive a confirmation of the order.

6. **Past orders view**
   - The user must be able to see the past orders.

## Non-Functional Requirements (NFR)

1. **Availability**
   - The service must be available on demand when a demo is required.

2. **Performance**
   - The UI must respond to user actions without noticeable delays. For a prototype minimum latency it's not required.

3. **Usability**
   - The interface must be simple and intuitive, with clear navigation between the product list, cart, and order confirmation.

## Constraints & Assumptions

1. **Products**
   - Only two products are available.

2. **Cart**
   - Single selection of products is sufficient.
   - The only allowed operation in the cart is checkout.

3. **Orders**
   - Orders are read-only: they cannot be modified or deleted.

4. **Persistence**
   - All data is handled in memory, with no database.

5. **User**
   - No account or login management is provided; the user is considered unique (e.g., static username "salvatore").
