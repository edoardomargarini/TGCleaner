from setuptools import setup, find_packages

setup(
    name="TGCleaner",
    version="0.1",
    author="edoardomargarini",
    author_email="edoardo.margarini@mail.polimi.it",
    description="TGCleaner is a powerful tool designed to quickly clean up your Telegram groups, channels, and chats. Whether through a command-line interface (CLI) or a local web interface, TGCleaner automates the process of leaving multiple groups or chats, saving you from repetitive manual actions.",
    long_description_content_type="text/markdown",
    url="https://github.com/edoardomargarini/tgcleaner",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versione minima di Python richiesta
)