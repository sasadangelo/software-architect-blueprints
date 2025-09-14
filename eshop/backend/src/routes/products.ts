import { Router } from "express";
import { Product } from "../models/Product";

const router = Router();

// memoria
const products: Product[] = [
    new Product(1, "Tent", "Outdoor tent", 120, "tent.jpg"),
    new Product(2, "Backpack", "Hiking backpack", 80, "backpack.jpg")
];

router.get("/", (req, res) => {
    res.json(products);
});

export default router;
