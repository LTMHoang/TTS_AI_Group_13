from setuptools import setup

setup(
    name="ZaloTTS",
    version="0.0.1",
    description="Zalo Text To Speech",
    long_description_content_type="text/markdown",
    author="Hoang Le",
    author_email="letruongminhhoang2003@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[
        "zalo_tts",
    ],
    include_package_data=True,
    install_requires=[
        "PyAudio==0.2.14",
        "python-dotenv==0.17.0",
    ],
    entry_points={},
)