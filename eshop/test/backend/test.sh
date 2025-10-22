#!/bin/bash
# test_backend.sh
# A simple bash script to test the eShop backend API.
# Requirements: curl installed

BASE_URL="http://localhost:3000/api"
USERNAME="salvatore"

echo "Testing eShop Backend..."

# 1. Get Products
echo -e "\n1. GET /products"
curl -s -X GET "$BASE_URL/products" | jq .

# 2. Get Cart (should be empty)
echo -e "\n2. GET /cart/$USERNAME"
curl -s -X GET "$BASE_URL/cart/$USERNAME" | jq .

# 3. Add a product to the cart
echo -e "\n3. POST /cart/add"
curl -s -X POST "$BASE_URL/cart/add" \
  -H "Content-Type: application/json" \
  -d '{
        "userName": "'"$USERNAME"'",
        "productId": 1,
        "productName": "Tent",
        "price": 99.99,
        "color": "blue"
      }' | jq .

# 4. Get Cart again
echo -e "\n4. GET /cart/$USERNAME (after adding a product)"
curl -s -X GET "$BASE_URL/cart/$USERNAME" | jq .

# 5. Checkout
echo -e "\n5. POST /orders/add (checkout)"
curl -s -X POST "$BASE_URL/orders/add" \
  -H "Content-Type: application/json" \
  -d '{"userName": "'"$USERNAME"'"}' | jq .

# 6. Get Orders
echo -e "\n6. GET /orders/$USERNAME"
curl -s -X GET "$BASE_URL/orders/$USERNAME" | jq .

echo -e "\nBackend test completed."
