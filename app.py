import os
import random
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Load local .env for development

# Try to get API key from environment or Streamlit secrets
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except:
        st.error("GOOGLE_API_KEY not found. Set it in .env or Streamlit secrets.")
        st.stop()

genai.configure(api_key=api_key)

# ------------------------------
# Model Selection (with fallbacks)
# ------------------------------
def get_available_model():
    """
    Try a list of known Gemini models and return the first working one.
    """
    candidate_models = [
        'gemini-1.5-flash',
        'gemini-1.0-pro',
        'gemini-pro'
    ]
    
    for model_name in candidate_models:
        try:
            model = genai.GenerativeModel(model_name)
            # Quick test to verify the model can generate content
            model.generate_content("test")
            return model
        except Exception as e:
            # Optionally log the error (for debugging)
            # st.write(f"Model {model_name} failed: {e}")
            continue
    
    # If none of the preferred models work, try any model that supports generateContent
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # Use the first available model
                return genai.GenerativeModel(m.name)
    except Exception as e:
        st.error(f"Failed to list models: {e}")
    
    return None

# Initialize the model
model = get_available_model()
if model is None:
    st.error("🚫 No compatible Gemini model found. Please check your API key and ensure the Generative Language API is enabled.")
    st.stop()

# ------------------------------
# Helper Functions
# ------------------------------
def get_gemini_response(input_text, image_data, prompt):
    """
    Send prompt and optional image to Gemini and return the generated text.
    """
    content = [input_text, prompt]
    if image_data:
        content.insert(0, image_data[0])  # image first, then text
    response = model.generate_content(content)
    return response.text

def input_image_setup(uploaded_file):
    """
    Convert uploaded image file to the format expected by Gemini API.
    """
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return None

def get_random_fact():
    """
    Return a random historical fact from a predefined list.
    """
    facts = [
        "The Great Pyramid of Giza was originally covered in highly polished white limestone, making it shine brilliantly in the sun.",
        "Cleopatra lived closer in time to the first moon landing than to the construction of the pyramids.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
        "Napoleon was once attacked by a horde of rabbits during a hunting party.",
        "The Olympics in ancient Greece included events like chariot racing and a foot race where men competed in full armor.",
        "Viking warriors did not actually wear horned helmets; that myth was created by 19th-century artists.",
        "The library of Alexandria was not just a library but a major research center with scholars, botanists, and astronomers.",
        "Medieval knights practiced a form of wrestling called 'Fight Book' and had to be skilled in unarmed combat.",
        "The Bayeux Tapestry is actually an embroidery, not a tapestry, and it is nearly 70 meters long.",
        "Leonardo da Vinci could write with one hand and draw with the other simultaneously."
    ]
    return random.choice(facts)

# ------------------------------
# Streamlit UI Configuration
# ------------------------------
st.set_page_config(
    page_title="Gemini Historical Artifact Description",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏺 Gemini Historical Artifact Description")
st.markdown("Describe any historical artifact by name, period, or even an image. Powered by Google Gemini.")

# Sidebar for word count and extra info
with st.sidebar:
    st.header("Settings")
    word_count = st.number_input(
        "Desired word count",
        min_value=50,
        max_value=2000,
        value=500,
        step=50,
        help="Approximate length of the generated description."
    )
    st.markdown("---")
    st.markdown("### How it works")
    st.markdown(
        "1. Enter an artifact name or historical period.\n"
        "2. Optionally upload an image of the artifact.\n"
        "3. Set the desired word count.\n"
        "4. Click 'Generate Description'.\n"
        "5. While the AI works, enjoy a random historical fact!"
    )
    # Display which model is being used (optional, for debugging)
    st.caption(f"Using model: `{model.model_name}`")

# Main input area
col1, col2 = st.columns([2, 1])

with col1:
    artifact_input = st.text_input(
        "Artifact name or historical period",
        placeholder="e.g., Tutankhamun's Golden Mask, Renaissance, Bayeux Tapestry"
    )

with col2:
    # Optional image upload
    uploaded_file = st.file_uploader(
        "Upload artifact image (optional)",
        type=["jpg", "jpeg", "png"],
        help="If you have an image, upload it for a more detailed description."
    )

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Artifact", use_container_width=True)

# Generate button
generate_button = st.button("✨ Generate Description", type="primary")

# ------------------------------
# Main Generation Logic
# ------------------------------
if generate_button:
    if not artifact_input and not uploaded_file:
        st.warning("Please enter an artifact name/period or upload an image.")
    else:
        # Prepare the prompt with word count instruction
        base_prompt = f"""
        You are an expert historian. Describe the following historical artifact in detail.
        Include its name, origin, approximate time period, historical significance, 
        materials, artistic features, and any interesting anecdotes. 
        The description should be approximately {word_count} words long.
        """

        if artifact_input:
            base_prompt += f"\nArtifact/Period: {artifact_input}"

        # Process image if provided
        image_data = input_image_setup(uploaded_file) if uploaded_file else None

        # Show a random fact while generating
        fact_placeholder = st.empty()
        with st.spinner("Gemini is crafting the description..."):
            # Display a random fact
            fact = get_random_fact()
            fact_placeholder.info(f"📜 **Did you know?** {fact}")

            try:
                response = get_gemini_response(artifact_input, image_data, base_prompt)
                fact_placeholder.empty()  # Remove the fact after generation
                st.subheader("📖 Artifact Description")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred during generation: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io) and [Google Gemini](https://deepmind.google/technologies/gemini/).")
