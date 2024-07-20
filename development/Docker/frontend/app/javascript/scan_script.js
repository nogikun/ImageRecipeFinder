// カメラにアクセスする関数
async function setupCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: true
        });
        const videoElement = document.getElementById('cameraFeed');
        videoElement.srcObject = stream;
    } catch (error) {
        console.error('カメラのアクセスに失敗しました:', error);
    }
}


// 例として、点数と合計金額を適当に計算する関数を定義する
function calculateCart() {
    // ここでは仮に計算結果を設定していますが、実際のアプリケーションではデータベースやユーザー入力を基に計算することになります
    let itemCount = 10; // 仮の点数
    let totalAmount = 10000; // 仮の合計金額

    // HTMLの要素に計算結果を反映する
    document.getElementById('incart_num').textContent = itemCount;
    document.getElementById('incart_money').textContent = totalAmount.toLocaleString(); // 金額を通貨形式にフォーマットして表示する場合
}

// ページが読み込まれた時
window.onload = function() {
    setupCamera();
    calculateCart();
};