// APIから取得したレシピデータ（仮のデータ）
let recipes = [
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
function addRecipeCards() {
    // recipe_page要素を取得
    let recipePage = document.querySelector('.recipe_page');

    // recipes配列の各要素に対して処理を行う
    recipes.forEach(recipe => {
        // 新しいレシピカードのHTMLを作成
        let newRecipeCard = document.createElement('a');
        newRecipeCard.setAttribute('href', recipe.url);
        newRecipeCard.classList.add('recipe_card');

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
    });
}

// ページが読み込まれた後にレシピカードを追加
document.addEventListener('DOMContentLoaded', function() {
    addRecipeCards();
});