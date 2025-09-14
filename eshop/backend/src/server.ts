import express from "express";
import bodyParser from "body-parser";
import productsRouter from "./routes/products";
import cartRouter from "./routes/cart";
import ordersRouter from "./routes/orders";

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use("/api/products", productsRouter);
app.use("/api/cart", cartRouter);
app.use("/api/orders", ordersRouter);

app.listen(port, () => {
    console.log(`Eshop API running at http://localhost:${port}`);
});
