import { Router } from "express";
import { ShoppingCart } from "../models/ShoppingCart";
import { ShoppingCartItem } from "../models/ShoppingCartItem";
import { carts } from "./store"; // import condiviso

const router = Router();

router.post("/add", (req, res) => {
    const { userName, productId, productName, price, color } = req.body;

    let cart = carts.find(c => c.userName === userName);
    if (!cart) {
        cart = new ShoppingCart(carts.length + 1, userName);
        carts.push(cart);
    }

    const existingItem = cart.items.find(i => i.productId === productId);
    if (existingItem) {
        existingItem.quantity++;
    } else {
        const newItem = new ShoppingCartItem(
            cart.items.length + 1,
            cart.id,
            1,
            color,
            productId,
            price,
            productName
        );
        cart.items.push(newItem);
    }

    res.json(cart);
});

router.get("/:userName", (req, res) => {
    const cart = carts.find(c => c.userName === req.params.userName);
    res.json(cart || { items: [] });
});

export default router;

