import fs from "fs";
import path from "path";    

export default defineEventHandler(async (event) => {
    const body = await readFormData(event)

    interface DetectBirdResponse {
        image: string;
        prediction: string;
        filename: string;
    }

    const res = await $fetch<DetectBirdResponse>("http://127.0.0.1:8000/detect-bird/", {
        method: "POST",
        body: body
    });

    const { image, prediction, filename } = res

    const buffer = Buffer.from(image, 'base64')

    // Save the file in the `public/processed-images` folder
    const savePath = path.join(process.cwd(), "public/processed-images", filename);
    fs.writeFileSync(savePath, buffer);

    return {
        image_path: `/processed-images/${filename}`,
        prediction
    }
})