# Gemini Historical Artifact Description

A web application that leverages Google's Generative AI (Gemini 1.5 Flash) to generate rich, detailed descriptions of historical artifacts. Users can input an artifact name or historical period, specify a desired word count, and optionally upload an image. While the AI generates the content, a random historical fact is displayed to keep the user engaged.

![App Screenshot](screenshot.png) *(Add a screenshot of your app here)*

## Features

- **Text-based input**: Describe artifacts by name or historical period (e.g., "Tutankhamun's Golden Mask", "Renaissance").
- **Image support**: Upload an image of the artifact for even more context-aware descriptions.
- **Word count control**: Set the approximate length of the generated description (50–2000 words).
- **Random historical facts**: Learn something new while waiting for the AI to generate content.
- **Clean, intuitive UI**: Built with Streamlit for rapid interaction.

## How It Works

1. The user enters an artifact name/period and optionally uploads an image.
2. A prompt is constructed with the desired word count and sent to the Gemini 1.5 Flash model.
3. While the model processes the request, a random historical fact is displayed.
4. The generated description is shown in the app and can be copied or exported.

## Technologies Used

- **Frontend/Backend**: [Streamlit](https://streamlit.io)
- **AI Model**: [Google Gemini 1.5 Flash](https://deepmind.google/technologies/gemini/)
- **Image Handling**: PIL (Pillow)
- **Environment Management**: python-dotenv

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemini-historical-artifact.git
   cd gemini-historical-artifact