import React, { useEffect, useState } from "react";
import { getProducts, addToCart as apiAddToCart } from "../services/api";
import { useCart } from "../context/CartContext";

const Products = () => {
    const [products, setProducts] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const { items, setItems, userName } = useCart();

    useEffect(() => {
        getProducts()
            .then(res => setProducts(res.data))
            .finally(() => setLoading(false));
    }, []);

    const handleAddToCart = async (product: any) => {
        await apiAddToCart({
            userName,
            productId: product.id,
            productName: product.name,
            price: product.price,
            color: "blue",
        });

        const existing = items.find(i => i.productId === product.id);
        if (existing) {
            existing.quantity++;
            setItems([...items]);
        } else {
            setItems([...items, { ...product, quantity: 1, color: "blue" }]);
        }

        alert(`${product.name} added to cart!`);
    };

    if (loading) return <p>Loading...</p>;

    return (
        <div className="container mt-3">
            <h1>Products</h1>
            <div className="row">
                {products.map(p => (
                    <div className="col-md-3 mb-3" key={p.id}>
                        <div className="card">
                            <img src={`/images/${p.imageUrl}`} className="card-img-top" alt={p.name} />
                            <div className="card-body">
                                <h5 className="card-title">{p.name}</h5>
                                <p className="card-text">${p.price}</p>
                                <button className="btn btn-primary" onClick={() => handleAddToCart(p)}>
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Products;

