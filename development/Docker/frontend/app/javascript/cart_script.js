function addItemsToCart() {
    // 商品情報の配列（例として、商品名と価格を定義）
    let items = [
        { name: "にんじん", price: 100, img: "/img/food1_1.png" },
        { name: "玉ねぎ", price: 80, img: "/img/food1_2.png" },
        { name: "ジャガイモ", price: 120, img: "/img/food1_3.png" }
    ];

    // 商品をカートに追加するループ
    items.forEach(item => {
        // 新しい商品のHTMLコードを作成
        let newItemHtml = `
            <div class="cart_item">
                <img src="${item.img}" alt="">
                <div class="cart_item_name">${item.name}</div>
                <div class="cart_item_price">${item.price}</div>
            </div>
        `;

        // cart_items要素に新しい商品を追加
        let cartItemsDiv = document.querySelector('.cart_items');
        cartItemsDiv.innerHTML += newItemHtml;
    });
}

// ページが読み込まれた後に商品を追加
document.addEventListener('DOMContentLoaded', function() {
    addItemsToCart();
});
