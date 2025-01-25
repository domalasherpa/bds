// composables/useBirdDetection.js

export default function useBirdDetection() {
  const previewImageUrl = ref('')        // For storing the preview image URL
  const resultImage = ref('')            // For storing the result image URL
  const resultText = ref('')             // For storing the result text
  const loading = ref(false)             // For showing the loading spinner

  // Method to preview the uploaded image
  const previewImage = (event: any) => {
    const file = event.target.files[0]
    if (file) {
      previewImageUrl.value = URL.createObjectURL(file)
    }
  }

  // Method to handle image upload and detection
  const uploadImage = async (file: string | Blob) => {
    if (!file) {
      alert("Please select an image.")
      return
    }

    loading.value = true
    resultImage.value = ''
    resultText.value = ''

    const formData = new FormData()
    formData.append('file', file)

    try {
      // API call to backend for bird detection using $fetch
      const data = await $fetch<{ image_path: string, prediction: { class: string, confidence: number }[] }>('/detect-bird/', {
        method: 'POST',
        body: formData
      })

      // Set result image and text
      resultImage.value = `./${data.image_path}`
      resultText.value = `<strong>Detection Result:</strong> ${data.prediction[0]['class']} (Confidence: ${(data.prediction[0]['confidence']).toFixed(2)}%)`
    } catch (error) {
      resultText.value = 'No birds Detected!'
    } finally {
      loading.value = false
    }
  }

  return {
    previewImageUrl,
    resultImage,
    resultText,
    loading,
    previewImage,
    uploadImage,
  }
}
