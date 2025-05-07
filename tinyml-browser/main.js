async function setupCamera() {
  const video = document.getElementById("video");
  const stream = await navigator.mediaDevices.getUserMedia({
    video: { width: 224, height: 224 },
    audio: false,
  });
  video.srcObject = stream;
  return new Promise((resolve) => {
    video.onloadedmetadata = () => resolve(video);
  });
}

async function run() {
  const video = await setupCamera();
  video.play();

  // 正しいCORS対応モデルURL
  const model = await tf.loadGraphModel(
    "https://storage.googleapis.com/tfjs-models/savedmodel/mobilenet_v2_1.0_224/model.json"
  );

  const resultElem = document.getElementById("result");

  setInterval(async () => {
    const tensor = tf.browser
      .fromPixels(video)
      .resizeNearestNeighbor([224, 224])
      .toFloat()
      .expandDims();
    const predictions = await model.predict(tensor).data();
    const max = predictions.indexOf(Math.max(...predictions));
    resultElem.innerText = `推論結果クラスID: ${max}`;
  }, 2000);
}

run();
