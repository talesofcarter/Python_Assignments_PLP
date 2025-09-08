import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def calculate_file_hash(filepath):
    """Calculate MD5 hash of a file to check for duplicates."""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except IOError:
        return None

def is_safe_to_download(response):
    """Check if the response content appears to be safe for download."""
    content_type = response.headers.get('Content-Type', '')
    
    # Only allow image content types
    allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp', 
                    'image/tiff', 'image/bmp', 'image/svg+xml']
    
    if not any(ct in content_type for ct in allowed_types):
        return False, f"Unsupported content type: {content_type}"
    
    # Check content length to avoid extremely large files
    content_length = response.headers.get('Content-Length')
    if content_length and int(content_length) > 50 * 1024 * 1024:  # 50MB limit
        return False, f"File too large: {content_length} bytes"
    
    return True, "Safe to download"

def download_image(url, download_dir):
    """Download an image from a URL and save it to the specified directory."""
    try:
        # Set a user-agent header to identify ourselves
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (Community Project)'
        }
        
        # Make the request with timeout
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Security check
        safe, message = is_safe_to_download(response)
        if not safe:
            return False, message
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            # Get extension from content type if possible
            content_type = response.headers.get('Content-Type', '')
            ext = content_type.split('/')[-1] if '/' in content_type else 'bin'
            filename = f"downloaded_image.{ext}"
        
        filepath = os.path.join(download_dir, filename)
        
        # Check if file already exists and avoid duplicates
        if os.path.exists(filepath):
            # Compare content hashes to determine if it's a true duplicate
            existing_hash = calculate_file_hash(filepath)
            
            # Calculate hash of the new content
            new_content_hash = hashlib.md5(response.content).hexdigest()
            
            if existing_hash == new_content_hash:
                return True, f"Image already exists: {filename}"
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        return True, f"Successfully fetched: {filename}"
        
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"
    except Exception as e:
        return False, f"An error occurred: {e}"

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    print("Ubuntu: I am because we are")
    print("We connect to the global community with respect and gratitude\n")
    
    # Create directory if it doesn't exist
    download_dir = "Fetched_Images"
    os.makedirs(download_dir, exist_ok=True)
    
    # Get URLs from user
    urls_input = input("Please enter image URLs (separated by commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    if not urls:
        print("No URLs provided. Exiting.")
        return
    
    successful_downloads = 0
    total_urls = len(urls)
    
    print(f"\nAttempting to fetch {total_urls} image(s)...\n")
    
    for i, url in enumerate(urls, 1):
        print(f"Processing URL {i} of {total_urls}: {url}")
        success, message = download_image(url, download_dir)
        
        if success:
            print(f"✓ {message}")
            successful_downloads += 1
        else:
            print(f"✗ {message}")
    
    print(f"\nDownload summary: {successful_downloads} of {total_urls} succeeded")
    
    if successful_downloads > 0:
        print("\nConnection strengthened. Community enriched.")
        print("These images are now available for sharing in the spirit of Ubuntu.")
    else:
        print("\nNo images were downloaded, but we remain connected to our community.")

if __name__ == "__main__":
    main()