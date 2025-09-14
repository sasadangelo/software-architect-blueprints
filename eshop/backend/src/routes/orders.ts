import { Router } from "express";
import { Order } from "../models/Order";
import { carts } from "./store"; // import condiviso

const router = Router();

const orders: Order[] = [];

router.post("/add", (req, res) => {
    const { userName } = req.body;

    const cart = carts.find(c => c.userName === userName);
    if (!cart || cart.items.length === 0) {
        return res.status(400).json({ error: "Cart is empty" });
    }

    const total = cart.items.reduce((sum, item) => sum + item.price * item.quantity, 0);

    const newOrder = new Order(
        orders.length + 1,
        userName,
        [...cart.items], // copia degli item
        total,
        new Date()
    );

    orders.push(newOrder);

    // svuota carrello dopo ordine
    cart.items = [];

    res.json(newOrder);
});

router.get("/:userName", (req, res) => {
    const userOrders = orders.filter(o => o.userName === req.params.userName);
    res.json(userOrders);
});

export default router;

