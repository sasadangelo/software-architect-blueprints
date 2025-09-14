export class ShoppingCartItem {
    constructor(
        public id: number,
        public shoppingCartId: number,
        public quantity: number,
        public color: string,
        public productId: number,
        public price: number,
        public productName: string
    ) { }
}
