import { ShoppingCartItem } from "./ShoppingCartItem";

export class ShoppingCart {
    constructor(
        public id: number,
        public userName: string,
        public items: ShoppingCartItem[] = []
    ) { }

    get totalPrice(): number {
        return this.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    }
}
