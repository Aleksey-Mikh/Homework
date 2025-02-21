from setuptools import setup, find_packages

PROGRAM_VERSION = "5.0.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='rss_reader',
    version=PROGRAM_VERSION,
    author='Aleksey Mikhalkevich',
    author_email='lehado67@gmail.com',
    description="RSS reader for feed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aleksey-Mikh/Homework/tree/final_task",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml',
        'Jinja2',
        'fpdf',
        'pytest',
        'pytest-cov',
        'colorama',
    ],
    entry_points={
        "console_scripts": [
            "rss_reader = rss_reader:main",
        ],
    }
)
