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







document.addEventListener('DOMContentLoaded', async () => {
    const stream = await setupCamera();
    const video = document.getElementById('cameraFeed');
    const captureButton = document.getElementById('captureButton');

    // ポップアップウィンドウの閉じるボタン（×ボタン）がクリックされた時の処理
    const popupClose = document.querySelector('.popup-close');
    popupClose.addEventListener('click', function() {
        popup.checked = false; // チェックボックスを非チェック状態にする
        popupOverlay.style.display = 'none'; // ポップアップウィンドウを非表示にする
    });

    document.getElementById('captureButton').addEventListener('click', () => {
        // 結果の表示に関する変数
        const popup = document.getElementById('popup');
        const popupOverlay = document.querySelector('.popup-overlay');

        // カメラ映像に関する変数
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d'); // 白紙のキャンバスを取得
        context.drawImage(video, 0, 0, canvas.width, canvas.height); // キャンバスにカメラの映像を描画

        // キャンバスの内容をBlobデータとして取得
        canvas.toBlob(async (blob) => {
            // BlobをArrayBufferに変換
            const arrayBuffer = await blob.arrayBuffer();
            const binaryData = new Uint8Array(arrayBuffer);

            // 送信するデータをFormDataオブジェクトに格納（形式を揃えるため）
            const formData = new FormData();
            const val = new Blob([binaryData], { type: 'image/png' });
            formData.append('cap', val, 'cap.png');

            // バイナリデータをPOSTリクエストで送信
            try {
                const host = window.location.hostname; // ホスト名を取得 （ポート違いにapiサーバーがあるため取得）
                const url = 'http://'+ host +':3000/cam/search'; // 送信先のURL
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData
                });

                if (response.ok) {
                    const data = response.json();
                    data.then(result => {
                        console.log('Success:', result.item_list);
                        const itemList = result.item_list;
                        for (let i = 0; i < itemList.length; i++) {
                            const item = itemList[i];
                            console.log('item:', item);
                            //
                            // ココに商品情報を表示する処理を追加
                            //
                            // チェックボックスの状態を切り替えることでポップアップウィンドウの表示・非表示を制御
                            popup.checked = !popup.checked;
                            // ポップアップウィンドウのオーバーレイが表示されるようにする
                            if (popup.checked) {
                                popupOverlay.style.display = 'block';
                            } else {
                                popupOverlay.style.display = 'none';
                            }
                        }
                      });
                } else {
                    console.error('ResponceError:', response.statusText);
                }

            } catch (error) {
                // エラー処理
                console.error('Error:', error);
            }

            console.log('captured');
        });
    });
});