from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple math quiz application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List dependencies here, e.g., 'numpy>=1.19.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",  # Replace `main` with the function you want to run
        ],
    },
)
