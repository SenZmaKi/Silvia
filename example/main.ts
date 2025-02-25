import { readFile } from "fs/promises";
import { Image } from "./types";
import "dotenv/config"; // Load environment variables from .env file

const HOST = process.env.FLASK_HOST || "127.0.0.1";
const PORT = parseInt(process.env.FLASK_PORT || "5000");

async function getImage(path: string): Promise<Image> {
    const imageContent = await readFile(path);
    const format = path.split(".").pop();
    if (!format) throw new Error("Failed to get image format");
    const base64_data = imageContent.toString("base64");
    return {
        format,
        base64_data,
    };
}

async function main(): Promise<void> {
    const instructions = "Tou are a Financial Assistant"
    const prompt = `
    Extract the following information in the provided receipt images.
    Restrict yourself to the json format provided.
    If you cannot a specific field, set it to null.
    Be as strict as possible, do not make any assumptions or fabricate information.

    The json format is as follows:

    {
        shop_name: string, // The name of the shop
        date: string, // The date of the purchase in YYYY-MM-DD format
        summary: string, // A brief summary of the purchase
        products: {
            price: number, // The price of the product
            quantity: number, // The quantity of the product
            name: string, // The name of the product
            category: string, // The category of the product, you can infer it from the name
        }
    }
    `
    const imagePath = "./receipt.jpg";
    console.log("Getting image");
    const image = await getImage(imagePath);
    const promptParams = {
        prompt,
        instructions,
        images: [image],
    };
    const url = `http://${HOST}:${PORT}/`;
    console.log("Sending request");
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(promptParams),
    });
    if (!response.ok) throw new Error(
        `Failed to run prompt:
        Status code: ${response.status}
        Response text: ${await response.text()}`
    );
    const json = await response.json();
    console.log(`Prompt response: ${JSON.stringify(json, null, 2)}`);
}

await main();