<template>
  <div>
    <div v-if="isLive">
      <video ref="videoElement" autoplay playsinline width="640" height="480"></video>
      <canvas ref="canvasElement" width="640" height="480" style="position: absolute; top: 0; left: 0;"></canvas>
    </div>
    <UButton @click="isLive = false">Stop Camera</UButton>
  </div>
</template>

<script setup>
// Refs for video and canvas elements
const isLive = ref(true);
const videoElement = ref(null);
const canvasElement = ref(null);

// Initialize the model and set up webcam
let model;
let stream;
const startWebcam = async () => {
  if (!videoElement.value) {
    console.error('Video element not found!');
    return;
  }

  try {
    // Start the webcam
    stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoElement.value.srcObject = stream;

    // Load the pre-trained model
    // model = await cocoSsd.load();
    console.log("Model loaded successfully");

    // Start the object detection process
    // detectObjects();
    drawPredictions([{bbox: [10,10, 100, 100], class: "Loading...", score: 0}]);
  } catch (error) {
    console.error('Error accessing webcam or loading model:', error);
  }
};

// Function to detect objects in the video stream
const detectObjects = async () => {
  if (!videoElement.value || !canvasElement.value || !model) {
    return;
  }

  // Get the video frame as an image tensor
  const predictions = await model.detect(videoElement.value);


  // Draw the detections on the canvas
  drawPredictions(predictions);

  // Continue detecting objects in the next frame
  requestAnimationFrame(detectObjects);
};

// Draw the predictions (bounding boxes and labels)
const drawPredictions = (predictions) => {
  const ctx = canvasElement.value.getContext('2d');
  ctx.clearRect(0, 0, canvasElement.value.width, canvasElement.value.height);
  predictions.forEach(prediction => {
    ctx.beginPath();
    ctx.rect(...prediction.bbox);
    ctx.lineWidth = 2;
    ctx.strokeStyle = 'red';
    ctx.fillStyle = 'red';
    ctx.stroke();
    ctx.fillText(`${prediction.class} (${Math.round(prediction.score * 100)}%)`, prediction.bbox[0], prediction.bbox[1] > 10 ? prediction.bbox[1] - 5 : 10);
  });
};

onMounted(() => {
  startWebcam();
});

onUnmounted(() => {
  if (stream) {
    stream.getTracks().forEach(track => track.stop()); // Stop webcam stream when component unmounts
  }
});
</script>

