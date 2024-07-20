document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.check').forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
            const ingredientsList = this.closest('.ingredients_list');
            
            if (this.checked) {
                ingredientsList.classList.add('overlay');
                // クラスの追加後に、少し待機してからoverlay-activeクラスを追加する
                setTimeout(() => {
                    ingredientsList.classList.add('overlay-active');
                }, 50); // 50ミリ秒の待機時間を設定
            } else {
                ingredientsList.classList.remove('overlay-active');
            }
        });
    });
});



