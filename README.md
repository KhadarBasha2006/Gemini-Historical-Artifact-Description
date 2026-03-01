# Gemini Historical Artifact Description

A web application that leverages Google's Generative AI (Gemini 1.5 Flash) to generate rich, detailed descriptions of historical artifacts. Users can input an artifact name or historical period, specify a desired word count, and optionally upload an image. While the AI generates the content, a random historical fact is displayed to keep the user engaged.


## Features

- **Text-based input**: Describe artifacts by name or historical period (e.g., "Tutankhamun's Golden Mask", "Renaissance").
- **Image support**: Upload an image of the artifact for even more context-aware descriptions.
- **Word count control**: Set the approximate length of the generated description (50–2000 words).
- **Random historical facts**: Learn something new while waiting for the AI to generate content.
- **Clean, intuitive UI**: Built with Streamlit for rapid interaction.
  
## 📄 License
This project is licensed under the MIT License.


## 🔗 Drive 



## 📂 Project Structure
.
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── .env # Environment variables (local only, not committed)
├── .gitignore # Files to exclude from Git
└── README.md # Project documentation

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
   
📄 Detailed Project Description
For a comprehensive overview, including design decisions and implementation details, see the project description on Google Drive:
Project Description – Google Drive

🧰 Technologies Used
Frontend & Backend: Streamlit

AI Model: Google Gemini 1.5 Flash

Image Handling: Pillow (PIL)

Environment Management: python-dotenv

🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

🙏 Acknowledgements
Google Gemini API for the powerful language model.

Streamlit for making web app development so easy.

All the historical facts contributors.
