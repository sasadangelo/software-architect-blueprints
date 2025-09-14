import axios from "axios";

const api = axios.create({
    baseURL: "/api", // il proxy si occuperà di aggiungere localhost:3000
});

export const getProducts = () => api.get("/products");
export const getCart = (userName: string) => api.get(`/cart/${userName}`);
export const addToCart = (item: any) => api.post("/cart/add", item);
export const checkout = (userName: string) => api.post("/orders/add", { userName });
export const getOrders = (userName: string) => api.get(`/orders/${userName}`);