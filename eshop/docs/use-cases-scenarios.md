# Use Case / Scenario

## 1. Business Context

The eShop prototype is a **minimal in-memory shopping platform** designed to demonstrate the core flow of an online store. Its primary value proposition is to **allow a user to browse products, add them to a cart, and place an order**, without persisting data to a database.

### Strategic Goals:

- Validate the **shopping workflow** from product selection to checkout.
- Provide a **simple user interface** for demonstrating frontend and backend integration.
- Establish a foundation for **future enhancements** such as:
  - Database integration
  - User authentication
  - Multiple product variants
  - Order history and analytics

### Product Philosophy:

Users should experience a **frictionless shopping flow** where the focus is on understanding how a cart-based purchase system works. The prototype emphasizes **simplicity, clarity, and correctness** of operations rather than full-fledged features.

---

## 2. Personas & Usage Patterns

| Persona              | Characteristics                            | Key Features Used                                   |
| -------------------- | ------------------------------------------ | --------------------------------------------------- |
| **Casual Shopper**   | Browses a few products, minimal tech-savvy | View products, add to cart, checkout                |
| **Prototype Tester** | Focused on workflow validation             | Product selection, cart management, order placement |
| **Developer / QA**   | Tests system functionality                 | Verifies UI, backend responses, cart state updates  |

Each persona interacts with the eShop differently, but all workflows involve **real-time updates** of the cart and immediate feedback after checkout.

---

## 3. Use Case Scenario

1. **Viewing Products**
   - The user navigates to the products page.
   - Two products are displayed with name, price, and image.
2. **Adding Products to Cart**
   - The user selects products to add to the cart.
   - Quantity increments if the same product is selected multiple times.
3. **Viewing Cart**
   - The user reviews items in the cart.
   - Each item shows product name, price, quantity, and total.
   - The cart displays a total order amount.
4. **Checkout / Placing Order**
   - The user confirms the order.
   - Cart is cleared after successful checkout.
   - User receives a confirmation message.
   - Orders are stored in memory (read-only).

---

## 4. Expected Scale

Although this is a prototype, it can serve as a reference for **future scaling considerations**:

### User Volume
- Single-user or small group testing.
- No concurrent sessions required in this version.

### Data Footprint
- Two products only.
- Cart and orders managed in memory.
- No database persistence.

### Performance
- All actions respond immediately (≤ 1s) since data is in memory.
- Minimal backend load, mostly API endpoint calls.

---

## Architectural Implications

| Dimension               | Design Implication                                            |
| ----------------------- | ------------------------------------------------------------- |
| **Data Storage**        | In-memory objects for products, cart, and orders              |
| **API Endpoints**       | Simple REST endpoints: `/products`, `/cart`, `/orders`        |
| **State Management**    | Frontend uses React Context API to track cart state           |
| **UI Responsiveness**   | Bootstrap used for layout; immediate feedback for all actions |
| **Persistence**         | None in this prototype; all data lost on server restart       |
| **Future Enhancements** | Add database, authentication, product catalog, order history  |
