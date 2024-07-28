// スクリプト間で共有する変数を定義
import itemList from './data.js';
console.log('itemList:', itemList[0]); // データが取得できているか確認

if (itemList.length === 0) {
    console.log('itemList is empty');
}

// APIから取得したレシピデータ（仮のデータ）
var recipes = [
    {
        "title": "ノンフライヤーで簡単☆",
        "sample_cost": "1300",
        "image_url": "https://image.space.rakuten.co.jp/d/strg/ctrl/3/ddbb98ffc3216bffea80f327baf40649f0786beb.16.9.3.3.jpg",
        "about": "一晩漬け込んだお肉をノンフライヤーに入れるだけ！とっても簡単なスペアリブの作り方です！"
    },
    {
        "title": "国産レモンで♪爽やかレモン",
        "sample_cost": "2300",
        "image_url": "https://image.space.rakuten.co.jp/d/strg/ctrl/3/146b28247bc0fcee198705760f86d80aa1a498d9.34.2.3.2.jpg",
        "about": "国産レモンが手に入ったら作るジャムです♥スコーン、パン、紅茶に入れて、ハチミツと一緒にお湯で割っても♪"
    }
];

// レシピカードを生成して追加する関数
async function addRecipeCards() {
    // recipe_page要素を取得
    let recipePage = document.querySelector('.recipe_page');
    
    const item = itemList[0]; // itemListから商品情報を取得（1件）
    // レシピ情報を取得
    try {
        const host = window.location.hostname;
        const url = 'https://' + host + '/api/recipe/search';
        const params = new URLSearchParams({
            interval_sec: 1
        });
        const response = await fetch(`${url}?${params}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(item)
        });

        if (response.ok) {
            const data = response.json();
            data.then(result => {
                console.log('Success:', result.recipe_list);
                recipes = result.recipe_list;
                recipes.length = 10; // recipesの数量を 10 件以下に制限

                // レシピカードを生成
                recipes.forEach((recipe,index) => {
                    console.log('recipe:', recipe);
                    // 新しいレシピカードのHTMLを作成
                    let newRecipeCard = document.createElement('a');
                    newRecipeCard.setAttribute('href', recipe.url);
                    newRecipeCard.classList.add('recipe_card');

                    // card_id を追加
                    const card_id = "recipe_card_" + index;
                    newRecipeCard.setAttribute('id', card_id);

                    newRecipeCard.innerHTML = `
                        <div class="recipe_name">${recipe.title}</div>
                        <div class="recipe_card_main">
                            <div>
                                <div class="recipe_detail">${recipe.about}</div>
                                <div class="recipe_price_set">
                                    <div class="recipe_price">${recipe.sample_cost}</div>
                                    <div class="recipe_yen">円</div>
                                </div>
                            </div>
                            <div class="recipe_img">
                                <img src="${recipe.image_url}" alt="${recipe.title}の画像">
                            </div>
                        </div>
                    `;

                    // recipePageに新しいレシピカードを追加
                    recipePage.appendChild(newRecipeCard);

                    const card = document.querySelector("#" + card_id)
                    if (window.getComputedStyle(card.querySelector(".recipe_name")).height > '30px') {
                        card.style.height = '230px';
                    }
                    
                    // bodyの高さを調整
                    body_height = 900 + 230 * (index + 1);
                    document.querySelector('body').style.height = String(body_height) + 'px';
                });
            });
        } else {
            // エラー処理（レスポンスが受け取れない場合）
            console.error('ResponceError:', response.statusText);
        }
    } catch (error) {
        // エラー処理
        console.error('Error:', error);
    }
}



// ページが読み込まれた後にレシピカードを追加
document.addEventListener('DOMContentLoaded', function() {
    addRecipeCards();
});