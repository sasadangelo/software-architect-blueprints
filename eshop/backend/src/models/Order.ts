import { ShoppingCartItem } from "./ShoppingCartItem";

export class Order {
    constructor(
        public id: number,
        public userName: string,
        public items: ShoppingCartItem[],
        public total: number,
        public date: Date
    ) { }
}