import React, { useEffect, useState } from "react";
import { useCart } from "../context/CartContext";
import { getOrders } from "../services/api";

interface OrderItem {
    productName: string;
    price: number;
    quantity: number;
}

interface Order {
    id: number;
    items: OrderItem[];
    totalPrice: number;
}

const Orders = () => {
    const { userName } = useCart();
    const [orders, setOrders] = useState<Order[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await getOrders(userName);
                setOrders(response.data);
            } catch (error) {
                console.error(error);
                alert("Failed to load orders");
            } finally {
                setLoading(false);
            }
        };
        fetchOrders();
    }, [userName]);

    if (loading) return <p className="container mt-3">Loading orders...</p>;

    return (
        <div className="container mt-3">
            <h1>Your Orders</h1>
            {orders.length === 0 ? (
                <p>No orders yet.</p>
            ) : (
                orders.map(order => (
                    <div key={order.id} className="card mb-3">
                        <div className="card-header">
                            <strong>Order #{order.id}</strong> - Total: ${order.totalPrice}
                        </div>
                        <ul className="list-group list-group-flush">
                            {order.items.map((item, idx) => (
                                <li key={idx} className="list-group-item">
                                    {item.productName} - ${item.price} × {item.quantity}
                                </li>
                            ))}
                        </ul>
                    </div>
                ))
            )}
        </div>
    );
};

export default Orders;
