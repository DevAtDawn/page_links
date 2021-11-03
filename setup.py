from setuptools import setup
setup(
    name='scrape_links',
    version='0.0.1',
    packages=['scrape_links'],
    entry_points={
        'console_scripts': [
            'scrape_links=scrape_links.scrape_links:main'
        ]
    }
)
