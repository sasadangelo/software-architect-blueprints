import React from "react";
import { useCart } from "../context/CartContext";
import { checkout } from "../services/api";
import { useNavigate } from "react-router-dom";

const Cart = () => {
    const { items, userName, setItems } = useCart();
    const navigate = useNavigate();

    const handleCheckout = async () => {
        await checkout(userName);
        setItems([]);
        alert("Order placed!");
        navigate("/orders");
    };

    const total = items.reduce((sum, i) => sum + i.price * i.quantity, 0);

    return (
        <div className="container mt-3">
            <h1>Shopping Cart</h1>
            {items.length === 0 ? (
                <p>Your cart is empty.</p>
            ) : (
                <>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Product</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            {items.map(i => (
                                <tr key={i.productId}>
                                    <td>{i.productName}</td>
                                    <td>${i.price}</td>
                                    <td>{i.quantity}</td>
                                    <td>${i.price * i.quantity}</td>
                                </tr>
                            ))}
                        </tbody>
                        <tfoot>
                            <tr>
                                <td colSpan={3} className="text-end">
                                    <strong>Total:</strong>
                                </td>
                                <td>${total}</td>
                            </tr>
                        </tfoot>
                    </table>
                    <button className="btn btn-success" onClick={handleCheckout}>
                        Checkout
                    </button>
                </>
            )}
        </div>
    );
};

export default Cart;
