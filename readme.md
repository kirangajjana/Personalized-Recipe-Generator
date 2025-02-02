# Personalized Recipe Generator






## Overview
The **Personalized Recipe Generator** is a Streamlit-based application that generates structured recipes using the Google Gemini API. The app allows users to input recipe-related queries and receives detailed, structured responses including ingredients, cooking time, and step-by-step instructions.

You can check out the live app at:  
[Personalized Recipe Generator App](https://kirangajjana-personalized-recipe-generator-app-rcw117.streamlit.app/)

## Features
- Uses Google Gemini API to generate recipe responses.
- Maintains conversation history using Streamlit chat history.
- Provides structured responses with clear formatting.
- Simple, interactive, and user-friendly interface.

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personalized-recipe-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd personalized-recipe-generator
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the project root and add your Google Gemini API key:
   ```env
   gemini=your_api_key_here
   ```
6. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter a query in the input box (e.g., "Give me a recipe for chocolate cake").
2. Click on **Generate your response**.
3. The app will generate a structured recipe with ingredients, cooking time, and instructions.

## Technologies Used
- **Python**: Backend logic and API integration.
- **Streamlit**: Web framework for UI.
- **LangChain**: To structure and process the conversation.
- **Google Gemini API**: Generates AI-powered responses.
- **Dotenv**: Loads API keys securely from `.env` file.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.



