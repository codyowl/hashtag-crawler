from setuptools import setup, find_packages

setup(
    name='crawler',
    version='0.0.1',
    author='sampath kumar',
    author_email='mesampathhere@gmail.com',
    description='A simple cli tool to crawl tweets based on hashtags and save it on storage mediums like gitgist, google docs & evernote',
    install_requires=[
        'requests',
        'tweepy',
        'PyYAML'
    ],
    url='https://github.com/codyowl/hashtag-crawler',
    maintainer='sampath kumar',
    maintainer_email='mesampathhere@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='crawler, twittercrawler, hashtagcrawler',
)
