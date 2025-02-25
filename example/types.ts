export type PromptParams = {
    prompt: string;
    instructions: string;
    images: Image[];
};

export type Image = {
    /**
     * The base64 encoded image data. This is the encoding format OpenAI expects.
    */
    base64_data: string;
    /**
     * The file format of the image, e.g., "jpeg".
     */
    format: string;
};