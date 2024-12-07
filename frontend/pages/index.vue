<template>
  <div class="space-y-20">
    <div class="flex">
      <div class="flex-1 flex flex-col justify-center px-4 space-y-4 bg-gradient-to-r from-green-300">
        <h1 class="text-8xl">Bird Vision <br />Tech:</h1>
        <p class="text-3xl italic">
          Our mission is to provide a platform for birdwatchers to identify birds in real-time using machine learning.
        </p>
      </div>
      <div class="flex-1">
        <img src="/public/heroBird.jpg" alt="" class="h-full w-full">
      </div>
    </div>

    <div class="min-h-screen">
      <div class="flex flex-col items-center space-y-10 bg-white px-10">
        <h1>Experience the magic of learning by cutting-edge Ai technology</h1>
        <p>
          Bird Vision tech allows bird enthusiasta to identify birds in real-time using machine learning.
          Just take a picture of a bird and our Ai will identify the bird for you.
        </p>
      </div>
      <div>
        <div>

        </div>
        <div>

        </div>
        <div>

        </div>
      </div>

    </div>

    <div class="min-h-screen">
      <h1>How it works</h1>
      <p>
        Bird Vision tech uses a machine learning model to identify birds in real-time.
        The model is trained on a dataset of 1000+ bird species and can identify birds with an accuracy of 90%.
      </p>
    </div>

    <div>
      <h1>Get started</h1>
      <p>
        Experience the joy of bird-watching and let Bird Vision tech help you identify birds in real-time.
        Get started by signing up for an account and start using our platform today.
      </p>
      <UButton label="Sign up" @click="signUp"/>
    </div>
  </div>
</template>

<style scoped>

.customGradient{
  /* background-color: linear-gradient(to right bottom, #3e5703, #577905, #719e08, #8cc40d, #a8eb12); */
  background-color: yellow;
}
</style>