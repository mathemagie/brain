import re
import requests
import os
import logging
from urllib.parse import urlparse
from send_to_kindle import send_email

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def is_valid_url(url):
    """
    Checks if a URL is valid.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def download_markdown(url):
    """
    Downloads markdown content from a given URL.
    """

    if not is_valid_url(url):
        logging.error(f"Invalid URL: {url}")
        return None

    jina_url = f"https://r.jina.ai/{url}"
    try:
        response = requests.get(jina_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling jina.ai API for {url}: {e}")
        return None


def convert_markdown_to_pdf(md_file_path):
    """
    Converts a markdown file to a PDF file.
    """
    # Log the conversion attempt
    logging.info(f"Converting markdown file {md_file_path} to PDF")

    # Check if input file exists
    if not os.path.exists(md_file_path):
        logging.error(f"Input markdown file not found: {md_file_path}")
        return False

    # Check if CSS file exists

    current_dir = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(current_dir + "/styles.css"):
        logging.warning("styles.css not found, conversion may lack styling")
        return False

    os.system(
        f"md2pdf --css {current_dir}/styles.css {md_file_path} {md_file_path.replace('.md', '.pdf')}"
    )
    return md_file_path.replace(".md", ".pdf")


def save_markdown(content, filename):
    """
    Saves markdown content to a file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Successfully saved markdown to {filename}")
        return True
    except IOError as e:
        logging.error(f"Error saving file {filename}: {e}")
        return False


def get_and_save_md(url):
    """
    Calls the jina.ai API with a URL and saves the markdown result to a file.

    Args:
        url (str): The URL to process

    Returns:
        bool: True if successful, False otherwise
    """

    dir = "agents/ressources/"
    # Extract filename from URL
    filename = dir + url.rstrip("/").split("/")[-1] + ".md"

    # Check if file already exists
    if os.path.exists(filename):
        # logging.info(f"File {filename} already exists, skipping download")
        return True

    # Construct jina.ai API URL
    jina_url = f"https://r.jina.ai/{url}"

    try:
        # Make request to jina.ai API
        response = download_markdown(url)

        # Save markdown content to file
        save_markdown(response, filename)

        # Convert markdown to PDF
        pdf_file = convert_markdown_to_pdf(filename)

        send_email(pdf_file)

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error calling jina.ai API: {e}")
        return False
    except IOError as e:
        print(f"Error saving file: {e}")
        return False


def get_non_youtube_links(file_path):
    """
    Extracts all non-YouTube links from a markdown file.

    Args:
        file_path (str): The path to the markdown file.

    Returns:
        list: A list of non-YouTube links found in the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            markdown_content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

    # Regex to find markdown links
    link_pattern = re.compile(r"\[.*?\]\((.*?)\)")
    links = link_pattern.findall(markdown_content)

    # Filter out YouTube links
    non_youtube_links = [link for link in links if "youtube.com" not in link]

    return non_youtube_links


if __name__ == "__main__":
    file_path = "agents/README.md"
    non_youtube_links = get_non_youtube_links(file_path)

    if non_youtube_links:
        logging.info("Non-YouTube Links:")
        for link in non_youtube_links:
            get_and_save_md(link)
    else:
        logging.info("No non-YouTube links found.")
