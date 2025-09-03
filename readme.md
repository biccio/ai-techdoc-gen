# AI TechDoc Gen - Technical Document Generator

**AI techDoc Gen** is an intelligent, AI-powered documentation generator that leverages the capabilities of **Google Gemini 2.5 Pro** to create high-quality, structured developer documentation that adheres to the Diataxis framework. This tool is designed to analyze source code, API specifications, and other technical documents to produce clear, concise, and maintainable documentation.

The application follows a multi-step workflow to ensure the quality and relevance of the generated content:

1.  **Intelligent Pre-processing:** A contextual analysis of each source file is performed to extract key information.
2.  **Draft Index Generation:** A proposed index is created based on the pre-processed summaries, organizing the content according to Diataxis categories (Explanation, Reference, How-To, Tutorial).
3.  **Interactive Review:** A command-line interface (CLI) allows the user to review, modify, and approve the proposed index.
4.  **Final Content Generation:** Once the index is approved, the AI generates the final Markdown files, complete with YAML frontmatter, schema.org metadata, and Mermaid diagrams where appropriate.
5.  **Local Publishing:** The generated files are saved to a local output directory, ready to be integrated into a documentation site or Git repository.

## Project Structure

```
ai_doc_gen/
├── example_project/
│   ├── config.yaml
│   └── source_docs/
├── prompts/
│   ├── 1_preprocess.md
│   ├── 2_generate_index.md
│   ├── 3_refine_index.md
│   ├── 4_generate_content.md
│   ├── gold_standard.md
│   └── system_prompt.md
├── .env
├── .gitignore
├── diataxis_manuale.md
├── main.py
├── mappatura_diataxis_pagopa.md
└── requirements.txt
```

  * **`main.py`**: The core of the application, orchestrating the entire process.
  * **`prompts/`**: A directory containing the prompt templates used to instruct the Gemini model at each stage of the process.
  * **`example_project/`**: An example project demonstrating how to configure and use the generator.
      * **`config.yaml`**: The configuration file for defining the product name, version, input/output paths, etc.
      * **`source_docs/`**: The directory containing the source files from which to generate documentation.
  * **`.env`**: A file for managing API keys and other secrets.
  * **`requirements.txt`**: A list of the necessary Python dependencies.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-user/ai_doc_gen.git
    cd ai_doc_gen
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Configure environment variables:**
    Create a file named `.env` in the project's root directory and add your API keys:
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    GITHUB_TOKEN="YOUR_GITHUB_TOKEN" # Optional, for future integrations
    ```

## Usage

1.  **Configure Your Project:**
    Modify the `example_project/config.yaml` file to match your project's details:
    ```yaml
    product_name: "Your Product"
    version: "1.0.0"
    source_dir: "example_project/source_docs"
    local_output_dir: "generated_docs"
    output_path: "docs/v1.0"
    ```
2.  **Add Your Source Files:**
    Place your source files (e.g., OpenAPI specs, Markdown files, etc.) into the directory specified in `source_dir`.
3.  **Run the Application:**
    Execute the `main.py` script from the root directory:
    ```bash
    python main.py
    ```
4.  **Follow the Interactive Process:**
      * The script will analyze your source files and propose a documentation index.
      * Use the interactive CLI to review the index. You can approve it by typing `!generate` or provide feedback to refine it.
      * Once the index is approved, select the sections you want to generate (e.g., `all`, `il-prodotto,guida-tecnica`).
      * Upon completion, the generated Markdown files will be available in the directory specified by `local_output_dir`.