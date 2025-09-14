import React, { createContext, useContext, useState, ReactNode } from "react";

interface CartItem {
    productId: number;
    productName: string;
    price: number;
    quantity: number;
    color: string;
}

interface CartContextType {
    userName: string;
    items: CartItem[];
    setItems: React.Dispatch<React.SetStateAction<CartItem[]>>;
    clearCart: () => void;
}

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider = ({ children }: { children: ReactNode }) => {
    const [items, setItems] = useState<CartItem[]>([]);
    const userName = "salvatore"; // statico per esempio

    const clearCart = () => setItems([]);

    return (
        <CartContext.Provider value={{ userName, items, setItems, clearCart }}>
            {children}
        </CartContext.Provider>
    );
};

export const useCart = () => {
    const context = useContext(CartContext);
    if (!context) throw new Error("useCart must be used within CartProvider");
    return context;
};
