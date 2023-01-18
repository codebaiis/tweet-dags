from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='tweet_dags',
    version='0.0.1',
    author='danielx',
    # author_email='',
    description='DAGs for composing and sharing small bits of info (tweets).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/codebaiis/tweet-dags',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-dotenv',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',

        f'baiis_utils @ git+https://github.com/codebaiis/baiis-utils.git'
    ],
)