# BAZAFARM Technology Assistant

**BAZAFARM Technology Assistant** is a powerful web-based application designed to revolutionize farming through IoT and data analysis. Upload your farm data, create embeddings for efficient retrieval, and interact with your agricultural information through an intelligent Farm Assistant interface. 🚀

## 🛠️ Features

- **📊 Upload Farm Data**: Easily upload and preview your PDF documents containing farm data within the app.
- **🧠 Data Processing**: Generate embeddings for your farm documents to enable efficient search and retrieval.
- **🤖 Farm Assistant Interface**: Interact with your agricultural data using a smart chatbot that leverages the created embeddings.
- **🌡️ Real-time Monitoring**: View and analyze data on water levels, soil temperature, and fertility.
- **☀️ Solar-Powered**: Utilizes solar energy for sustainable operation in the field.
- **🌤️ Weather Forecasts**: Access weather predictions to make informed farming decisions.
- **📱 Mobile Access**: View your farm data on mobile devices, tablets, or PCs via Internet.
- **📧 Contact**: Get in touch with STES GROUP Ltd or contribute to the project on GitHub.
- **🌟 User-Friendly Interface**: Enjoy a sleek and intuitive UI with emojis and responsive design for enhanced user experience.

## 🖥️ Tech Stack

The BAZAFARM Technology App leverages a combination of cutting-edge technologies to deliver a seamless and efficient farming experience. Here's a breakdown of the technologies and tools used:

- **[LangChain](https://langchain.readthedocs.io/)**: Utilized as the orchestration framework to manage the flow between different components, including embeddings creation, vector storage, and Farm Assistant interactions.
- **[Unstructured](https://github.com/Unstructured-IO/unstructured)**: Employed for robust PDF processing, enabling the extraction and preprocessing of text from uploaded farm data documents.
- **[BGE Embeddings from HuggingFace](https://huggingface.co/BAAI/bge-small-en)**: Used to generate high-quality embeddings for the processed documents, facilitating effective semantic search and retrieval of agricultural information.
- **[Qdrant](https://qdrant.tech/)**: A vector database running locally via Docker, responsible for storing and managing the generated embeddings for fast and scalable retrieval of farm data.
- **[GPT-2 via Hugging Face Transformers](https://huggingface.co/gpt2)**: Integrated as the language model to power the Farm Assistant, providing intelligent and context-aware responses based on the farm data embeddings.
- **[Streamlit](https://streamlit.io/)**: The core framework for building the interactive web application, offering an intuitive interface for farmers to upload data, process information, and interact with the Farm Assistant.

- **IoT Sensors**: Custom-built sensors for measuring water levels, soil temperature, and fertility in real-time.

- **Solar Panels**: Integrated solar technology for powering the BAZAFARM devices in the field.

## 🤝 Contributing

Contributions are welcome! Whether it's reporting a bug, suggesting a feature, or submitting a pull request, your input is highly appreciated. Follow these steps to contribute:

1. Fork the Repository: Click on the "Fork" button at the top-right corner of the repository page.
2. Clone Your Fork
3. Create a New Branch:

```
git checkout -b feature/YourFeatureName
```

4. Make Your Changes: Implement your feature or fix.
5. Commit Your Changes:

```
git commit -m "Add Your Feature Description"
```

6. Push to Your Fork:

```
git push origin feature/YourFeatureName
```

7. Create a Pull Request: Navigate to the original repository and create a pull request from your fork.

## 📄 License

This project is licensed under the MIT License.

## 📫 Contact

- Email: info@stesgroup.rw ✉️
- Website: [STES GROUP Ltd](https://www.stesgroup.rw) 🌐

Feel free to reach out for any queries, suggestions, or contributions. Your feedback is invaluable!

© 2024 BAZAFARM TECHNOLOGY by STES GROUP Ltd. All rights reserved. 🛡️

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://langchain.readthedocs.io/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)

Happy farming with BAZAFARM! 🌾🚀✨
