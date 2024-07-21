import subprocess

def install_packages(packages):
    for package in packages:
        subprocess.run(['pip', 'install', package])

if __name__ == "__main__":
    required_packages = [
        'requests', 
        'mechanize', 
        'beautifulsoup4',  # This is bs4 (BeautifulSoup4)
        'rich', 
        'numpy', 
        'pandas', 
        'matplotlib', 
        'seaborn', 
        'scikit-learn', 
        'tensorflow', 
        'torch', 
        'transformers'
    ]  # Add more packages as needed
    install_packages(required_packages)
    print("Packages installed successfully.")
